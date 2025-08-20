from rest_framework import serializers
from apps.policy.models import PolicyModel

class PolicyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyModel
        fields = '__all__'
