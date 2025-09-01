
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.policy.models import PolicyModel, TranscationLedger, AgentModel, ClientModel
from apps.policy.utils import get_total_profit, get_average_rates, get_expected_bank_money


class StatisticsAPIView(APIView):
    def get(self, request):
        # total_policies = PolicyModel.objects.count()
        # total_agents = AgentModel.objects.count()
        # total_clients = ClientModel.objects.count()
        start_of_month = timezone.now().replace(day=1)


        policies_last_30_days = PolicyModel.objects.filter(
            created_at__gte=timezone.now() - timedelta(days=30))
        
        policies_last_start_of_month = PolicyModel.objects.filter(
            created_at__gte=start_of_month)
        policies_last_7_days = PolicyModel.objects.filter(
            created_at__gte=timezone.now() - timedelta(days=7))
        policies_today = PolicyModel.objects.filter(
            created_at=timezone.now().date())


        policies = PolicyModel.objects.all()

        total_profit, total_revenue, total_loss = get_total_profit(policies)
        profit_30, revenue_30, loss_30 = get_total_profit(
            policies_last_30_days)
        profit_start, revenue_start, loss_start = get_total_profit(
            policies_last_start_of_month)
        profit_7, revenue_7, loss_7 = get_total_profit(policies_last_7_days)
        profit_1, revenue_1, loss_1 = get_total_profit(policies_today)

        average_rate_all, average_profit_all = get_average_rates(policies)
        average_rate_30, average_profit_30 = get_average_rates(policies_last_30_days)
        average_rate_start, average_profit_start = get_average_rates(policies_last_start_of_month)
        average_rate_7, average_profit_7 = get_average_rates(policies_last_7_days)
        average_rate_1, average_profit_1 = get_average_rates(policies_today)
    
        # exptected money in the bank
        all_expected, all_current = get_expected_bank_money(policies)
        start_expected, start_current = get_expected_bank_money(policies_last_start_of_month)
        thirty_expected, thirty_current = get_expected_bank_money(policies_last_30_days)
        seven_expected, seven_current = get_expected_bank_money(policies_last_7_days)
        one_expected, one_current = get_expected_bank_money(policies_today)



        data = {
            "all":{
                "policy_count": policies.count(),
                "profit": total_profit,
                "revenue": total_revenue,
                "loss": total_loss,
                "cancel_policy": policies.filter(payment_status='cancelled').count(),
                "average_rate": average_rate_all,
                "average_profit": average_profit_all,
                "expected_money": all_expected,
                "current_money": all_current,
            },
            "start": {
                "policy_count": policies_last_start_of_month.count(),
                "profit": profit_start,
                "revenue": revenue_start,
                "loss": loss_start,
                "cancel_policy": policies_last_start_of_month.filter(payment_status='cancelled').count(),
                "average_rate": average_rate_start,
                "average_profit": average_profit_start,
                "expected_money": start_expected,
                "current_money": start_current,
            },
            "30": {
                "policy_count": policies_last_30_days.count(),
                "profit": profit_30,
                "revenue": revenue_30,
                "loss": loss_30,
                "cancel_policy": policies_last_30_days.filter(payment_status='cancelled').count(),
                "average_rate": average_rate_30,
                "average_profit": average_profit_30,
                "expected_money": thirty_expected,
                "current_money": thirty_current,
            },
            "7": {
                "policy_count": policies_last_7_days.count(),
                "profit": profit_7,
                "revenue": revenue_7,
                "loss": loss_7,
                "cancel_policy": policies_last_7_days.filter(payment_status='cancelled').count(),
                "average_rate": average_rate_7,
                "average_profit": average_profit_7,
                "expected_money": seven_expected,
                "current_money": seven_current,
            },
            "1": {
                "policy_count": policies_today.count(),
                "profit": profit_1,
                "revenue": revenue_1,
                "loss": loss_1,
                "cancel_policy": policies_today.filter(payment_status='cancelled').count(),
                "average_rate": average_rate_1,
                "average_profit": average_profit_1,
                "expected_money": one_expected,
                "current_money": one_current,
            },
        }
        return Response(data)
