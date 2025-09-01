from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
import pandas as pd
from django.http import HttpResponse
import io

from apps.policy.models import PolicyModel, TranscationLedger
from apps.policy.serializers.policy_serializer import PolicySerializer
from apps.policy.utils import get_total_profit, get_average_rates


class DownloadReportView(APIView):
    """
    View to download a report of policies.
    """

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to download the report.
        """
        # Get policies data
        queryset = PolicyModel.objects.all()

        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        status_filter = self.request.query_params.get('status', None)
        insured_name = self.request.query_params.get('insured_name', None)
        agent_name = self.request.query_params.get('agent_name', None)
        insurance_company= self.request.query_params.get('insurance_company', None)

        # insured_name, agent_name and insurance_company are primary values
        if insured_name:
            queryset = queryset.filter(client=insured_name)
        
        if agent_name:
            queryset = queryset.filter(agent=agent_name)
        
        if insurance_company:
            queryset = queryset.filter(insurance_company=insurance_company)

        if start_date:
            queryset = queryset.filter(issue_date__gte=start_date)
        
        if end_date:
            queryset = queryset.filter(issue_date__lte=end_date)

        if status_filter:
            queryset = queryset.filter(payment_status=status_filter)

        policy_serializer = PolicySerializer(queryset, many=True)
        policies_df = pd.DataFrame(policy_serializer.data)

        # Get summary data
        start_of_month = timezone.now().replace(day=1)
        policies_last_30_days = PolicyModel.objects.filter(created_at__gte=timezone.now() - timedelta(days=30))
        policies_last_start_of_month = PolicyModel.objects.filter(created_at__gte=start_of_month)
        policies_last_7_days = PolicyModel.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))
        policies_today = PolicyModel.objects.filter(created_at=timezone.now().date())
        all_policies = PolicyModel.objects.all()

        total_profit, total_revenue, total_loss = get_total_profit(all_policies)
        profit_30, revenue_30, loss_30 = get_total_profit(policies_last_30_days)
        profit_start, revenue_start, loss_start = get_total_profit(policies_last_start_of_month)
        profit_7, revenue_7, loss_7 = get_total_profit(policies_last_7_days)
        profit_1, revenue_1, loss_1 = get_total_profit(policies_today)

        average_rate_all, average_profit_all = get_average_rates(all_policies)
        average_rate_30, average_profit_30 = get_average_rates(policies_last_30_days)
        average_rate_start, average_profit_start = get_average_rates(policies_last_start_of_month)
        average_rate_7, average_profit_7 = get_average_rates(policies_last_7_days)
        average_rate_1, average_profit_1 = get_average_rates(policies_today)

        summary_data = {
            "Timeframe": ["All Time", "This Month", "Last 30 Days", "Last 7 Days", "Today"],
            "Policy Count": [
                all_policies.count(),
                policies_last_start_of_month.count(),
                policies_last_30_days.count(),
                policies_last_7_days.count(),
                policies_today.count()
            ],
            "Profit": [total_profit, profit_start, profit_30, profit_7, profit_1],
            "Revenue": [total_revenue, revenue_start, revenue_30, revenue_7, revenue_1],
            "Loss": [total_loss, loss_start, loss_30, loss_7, loss_1],
            "Cancelled Policies": [
                all_policies.filter(payment_status='cancelled').count(),
                policies_last_start_of_month.filter(payment_status='cancelled').count(),
                policies_last_30_days.filter(payment_status='cancelled').count(),
                policies_last_7_days.filter(payment_status='cancelled').count(),
                policies_today.filter(payment_status='cancelled').count()
            ],
            "Average Rate": [average_rate_all, average_rate_start, average_rate_30, average_rate_7, average_rate_1],
            "Average Profit": [average_profit_all, average_profit_start, average_profit_30, average_profit_7, average_profit_1],
        }
        summary_df = pd.DataFrame(summary_data)

        # Create an in-memory Excel file
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            policies_df.to_excel(writer, sheet_name='Policies', index=False)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)

        output.seek(0)

        # Create the HttpResponse object with the appropriate content type and headers
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="report.xlsx"'

        return response