from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from apps.policy.serializers.policy_serializer import (
    PolicySerializer,
    ClientSerilializer,
    InsuranceCompanySerializer,
    AgentSerializer,
    TransactionLedgerSerializer,
)
from apps.policy.models import PolicyModel, ClientModel, InsuranceCompanyModel, AgentModel, TranscationLedger

class TransactionLedgerView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = TransactionLedgerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        policy_id = request.query_params.get('policy_id')
        if not policy_id:
            return Response({'error': 'Policy ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = TranscationLedger.objects.filter(policy_id=policy_id)
        serializer = TransactionLedgerSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        transaction_id = request.data.get('transaction_id')
        if not transaction_id:
            return Response({'error': 'Transaction ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            transaction = TranscationLedger.objects.get(id=transaction_id)
            transaction.delete()
            return Response({'message': 'Transaction deleted successfully.'}, status=status.HTTP_200_OK)
        except TranscationLedger.DoesNotExist:
            return Response({'error': 'Transaction not found.'}, status=status.HTTP_404_NOT_FOUND)  

class PolicyView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        data = PolicyModel.objects.all()
        serializer = PolicySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = PolicySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        policy_id = request.data.get('policy_id')
        if not policy_id:
            return Response({'error': 'Policy ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            policy = PolicyModel.objects.get(id=policy_id)
            policy.delete()
            return Response({'message': 'Policy deleted successfully.'}, status=status.HTTP_200_OK)
        except PolicyModel.DoesNotExist:
            return Response({'error': 'Policy not found.'}, status=status.HTTP_404_NOT_FOUND)


class ClientView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ClientSerilializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = ClientModel.objects.all()
        serializer = ClientSerilializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InsuranceCompanyView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = InsuranceCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        data = InsuranceCompanyModel.objects.all()
        serializer = InsuranceCompanySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AgentView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        data = AgentModel.objects.all()
        serializer = AgentSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)