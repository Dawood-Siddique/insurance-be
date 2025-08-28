from apps.policy.models import TranscationLedger, PolicyModel

def get_all_balance(policy_id):
    try:

        policy = PolicyModel.objects.get(id=policy_id)
        agent = policy.agent
        transactions = TranscationLedger.objects.filter(policy__agent=agent)
        total_balance = 0
        for transaction in transactions:
            if transaction.type == 'payment':
                total_balance += transaction.amount
            elif transaction.type == 'payback':
                total_balance -= transaction.amount
            elif transaction.type == 'credit_adjustment':
                total_balance -= transaction.amount
        return total_balance


    except:
        return None

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



