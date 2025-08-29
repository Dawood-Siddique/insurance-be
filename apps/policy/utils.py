from apps.policy.models import TranscationLedger, PolicyModel

def get_all_balance(policy_id):
    try:
        current_policy = PolicyModel.objects.get(id=policy_id)
        agent = current_policy.agent

        policies = PolicyModel.objects.filter(agent=agent)
        total_balance = 0
        for policy in policies:
            exptected_profit = policy.client_price - policy.co_rate
            transactions = TranscationLedger.objects.filter(policy=policy)
            for transaction in transactions:
                if transaction.type == 'payment':
                    total_balance += transaction.amount
                elif transaction.type == 'payback':
                    total_balance -= transaction.amount
                elif transaction.type == 'credit_adjustment':
                    total_balance -= transaction.amount
            total_balance -= exptected_profit
        return total_balance    
    except Exception as e:
        raise e

def get_total_profit(policies):
    total_profit = 0
    total_loss = 0
    total_revenue = 0
    for policy in policies:
        transactions = TranscationLedger.objects.filter(policy=policy)

        for transaction in transactions:
            if transaction.type == 'payment':
                total_revenue += transaction.amount
            else:
                total_loss += transaction.amount
        total_profit += total_revenue - total_loss
    
    return (total_profit, total_revenue, total_loss)



