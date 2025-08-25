from rest_framework import serializers
from apps.policy.models import PolicyModel, ClientModel, InsuranceCompanyModel, AgentModel, TranscationLedger


class PolicySerializer(serializers.ModelSerializer):

    insurance_company = serializers.StringRelatedField()
    agent = serializers.StringRelatedField()
    client = serializers.StringRelatedField()

    class Meta:
        model = PolicyModel
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
    class Meta:
        model = PolicyModel
        fields = '__all__'