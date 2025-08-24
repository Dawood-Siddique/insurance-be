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
            elif transaction.type == 'cancelled':
                total_balance -= transaction.amount
            elif transaction.type == 'payback':
                total_balance -= transaction.amount
            elif transaction.type == 'credit_adjustment':
                total_balance -= transaction.amount
        return total_balance


    except:
        return None


