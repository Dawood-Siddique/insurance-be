from rest_framework import serializers
from apps.policy.models import PolicyModel, ClientModel, InsuranceCompanyModel, AgentModel, TranscationLedger, VendorModel

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=VendorModel
        fields = '__all__'


class ClientSerilializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'


class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCompanyModel
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentModel
        fields = '__all__'


class TransactionLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranscationLedger
        fields = '__all__'


class PolicyDetailSerializer(serializers.ModelSerializer):
    transactions = TransactionLedgerSerializer(source='transcationledger_set', many=True, read_only=True)
    profit_loss = serializers.SerializerMethodField()
    expected_profit = serializers.SerializerMethodField()

    
    class Meta:
        model = PolicyModel
        fields = '__all__'
    
    def get_profit_loss(self, obj):
        total_profit = 0
        transactions = TranscationLedger.objects.filter(policy=obj)
        for transaction in transactions:
            if transaction.type == 'payment':
                total_profit += transaction.amount
            else:
                total_profit -= transaction.amount
        total_profit -= obj.co_rate
        return total_profit
    
    def get_expected_profit(self, obj):
        return obj.client_price - obj.co_rate
    


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['insurance_company'] = instance.insurance_company.name if instance.insurance_company else None
        rep['agent'] = instance.agent.name if instance.agent else None
        rep['client'] = instance.client.name if instance.client else None
        rep['vendor'] = instance.vendor.name if instance.vendor else None
        return rep

class PolicySerializer(serializers.ModelSerializer):

    # insurance_company = serializers.StringRelatedField()
    # agent = serializers.StringRelatedField()
    # client = serializers.StringRelatedField()
    insurance_company = serializers.PrimaryKeyRelatedField(queryset=InsuranceCompanyModel.objects.all())
    agent = serializers.PrimaryKeyRelatedField(queryset=AgentModel.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=ClientModel.objects.all())
    vendor = serializers.PrimaryKeyRelatedField(queryset=VendorModel.objects.all())
    profit_loss = serializers.SerializerMethodField()
    # agent = AgentSerializer()
    # client = ClientSerilializer()

    class Meta:
        model = PolicyModel
        fields = '__all__'
    
    def get_profit_loss(self, obj):
        total_profit = 0
        transactions = TranscationLedger.objects.filter(policy=obj)
        for transaction in transactions:
            if transaction.type == 'payment':
                total_profit += transaction.amount
            else:
                total_profit -= transaction.amount
        total_profit -= obj.co_rate
        return total_profit

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['insurance_company'] = instance.insurance_company.name
        rep['agent'] = instance.agent.name
        rep['client'] = instance.client.name
        return rep