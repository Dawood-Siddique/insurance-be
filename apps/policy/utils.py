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
        balance = 0
        transactions = TranscationLedger.objects.filter(policy=policy)

        for transaction in transactions:
            if transaction.type == 'payment':
                total_revenue += transaction.amount
                balance += transaction.amount
            else:
                balance -= transaction.amount
        profit = balance - policy.client_price
        if profit >= 0:
            total_profit += profit
        else:
            total_loss += profit
    
    return (total_profit, total_revenue, total_loss)


def get_average_rates(policies):
    total_policies = policies.count()
    if total_policies == 0:
        return (0, 0)

    total_client_price = 0
    total_profit = 0

    for policy in policies:
        total_client_price += policy.client_price
        total_profit += policy.client_price - policy.co_rate

    average_rate = total_client_price / total_policies
    average_profit = total_profit / total_policies

    return (average_rate, average_profit)


def get_expected_bank_money(policies):
    current = 0
    expected_money = 0
    for policy in policies:
        if policy.payment_method == 'bank':
            expected_money += policy.client_price
            try:
                transactions = TranscationLedger.objects.get(policy=policy)
                for transaction in transactions:
                    if transaction.type == 'payment':
                        current += transaction.amount
            except:
                return (0, 0)
    return (expected_money, current)


def get_expected_cash_money(policies):
    current = 0
    expected_money = 0
    for policy in policies:
        if policy.payment_method == 'cash':
            expected_money += policy.client_price
            try:
                transactions = TranscationLedger.objects.filter(policy=policy)
                for transaction in transactions:
                    if transaction.type == 'payment':
                        current += transaction.amount
            except TranscationLedger.DoesNotExist:
                pass # No transactions yet, current remains 0
    return (expected_money, current)
    