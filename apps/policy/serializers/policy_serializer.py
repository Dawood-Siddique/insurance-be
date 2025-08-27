from rest_framework import serializers
from apps.policy.models import PolicyModel, ClientModel, InsuranceCompanyModel, AgentModel, TranscationLedger


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
    class Meta:
        model = PolicyModel
        fields = '__all__'

    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['insurance_company'] = instance.insurance_company.name
        rep['agent'] = instance.agent.name
        rep['client'] = instance.client.name
        return rep

class PolicySerializer(serializers.ModelSerializer):

    # insurance_company = serializers.StringRelatedField()
    # agent = serializers.StringRelatedField()
    # client = serializers.StringRelatedField()
    insurance_company = serializers.PrimaryKeyRelatedField(queryset=InsuranceCompanyModel.objects.all())
    agent = serializers.PrimaryKeyRelatedField(queryset=AgentModel.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=ClientModel.objects.all())
    # agent = AgentSerializer()
    # client = ClientSerilializer()

    class Meta:
        model = PolicyModel
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['insurance_company'] = instance.insurance_company.name
        rep['agent'] = instance.agent.name
        rep['client'] = instance.client.name
        return rep