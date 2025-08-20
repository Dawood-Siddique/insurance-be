from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.policy.serializers.policy_serializer import PolicyModelSerializer

class PolicyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PolicyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        