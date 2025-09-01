from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from apps.policy.models import PolicyModel, TranscationLedger
from apps.policy.serializers.policy_serializer import PolicySerializer
from django.db.models import Sum
import pandas as pd
from django.http import HttpResponse
import io

class DownloadReportView(APIView):
    """
    View to download a report of policies.
    """
    # permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to download the report.
        """
        queryset = PolicyModel.objects.all()

        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        status_filter = self.request.query_params.get('status', None)

        if start_date:
            queryset = queryset.filter(issue_date__gte=start_date)
        
        if end_date:
            queryset = queryset.filter(issue_date__lte=end_date)

        if status_filter:
            queryset = queryset.filter(payment_status=status_filter)

        serializer = PolicySerializer(queryset, many=True)

        total_revenue = queryset.aggregate(total=Sum('client_price'))['total'] or 0
        total_paid = TranscationLedger.objects.filter(policy__in=queryset, type='payment').aggregate(total=Sum('amount'))['total'] or 0
        total_remaining = total_revenue - total_paid
        total_gross_price = queryset.aggregate(total=Sum('gross_price'))['total'] or 0
        total_profit = total_revenue - total_gross_price


        # Create a pandas DataFrame from the serialized data
        df = pd.DataFrame(serializer.data)

        # Create a summary DataFrame
        summary_data = {
            'Description': ['Total Revenue', 'Total Amount Paid', 'Total Amount Remaining', 'Total Gross Price', 'Total Profit'],
            'Amount': [total_revenue, total_paid, total_remaining, total_gross_price, total_profit]
        }
        summary_df = pd.DataFrame(summary_data)

        # Create an in-memory Excel file
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Policies', index=False)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)

        output.seek(0)

        # Create the HttpResponse object with the appropriate content type and headers
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="report.xlsx"'

        return response
