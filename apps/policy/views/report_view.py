from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.utils import timezone
from datetime import timedelta
import pandas as pd
from django.http import HttpResponse
import io

from apps.policy.models import PolicyModel, TranscationLedger
from apps.policy.serializers.policy_serializer import PolicySerializer
from apps.policy.utils import get_total_profit, get_average_rates, get_expected_bank_money, get_expected_cash_money


class DownloadReportView(APIView):
    """
    View to download a report of policies.
    """
    permission_classes = [IsAuthenticated]


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
        total_profit, total_revenue, total_loss = get_total_profit(queryset)
        average_rate, average_profit = get_average_rates(queryset)
        expected_money, current_money = get_expected_bank_money(queryset)
        exptected_money_cash, current_money_cash = get_expected_cash_money(queryset)

        summary_data = {
            "Policy Count": [queryset.count()],
            "Profit": [total_profit],
            "Revenue": [total_revenue],
            "Loss": [total_loss],
            "Cancelled Policies": [queryset.filter(payment_status='cancelled').count()],
            "Average Rate": [average_rate],
            "Average Profit": [average_profit],
            "Expected Bank Money": [expected_money],
            "Current Bank Money": [current_money],
            "Expected Cash Money": [exptected_money_cash],
            "Current Cash Money": [current_money_cash],

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