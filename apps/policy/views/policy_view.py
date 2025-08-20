from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class PolicyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # issue_date = models.DateField()
        # insurance_company = models.ForeignKey(InsuranceCompanyModel, on_delete=models.CASCADE)
        # policy_number = models.CharField(max_length=255)
        # client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
        # car_model = models.CharField(max_length=255)
        # engine_type = models.CharField(max_length=255)
        # agent = models.ForeignKey(AgentModel, on_delete=models.CASCADE)

        # gross_price = models.DecimalField(max_digits=10, decimal_places=2)
        # co_rate = models.DecimalField(max_digits=10, decimal_places=2)
        # client_price = models.DecimalField(max_digits=10, decimal_places=2)

        # payment_method = models.CharField(max_length=100, choices=[('cash', 'cash'), ('bank', 'bank')])
        # payment_status = models.CharField(max_length=100, choices=[('active', 'active'), ('complete', 'complete'), ('cancel', 'cancel')])
        # remarks = models.TextField()
        # reference_number = models.IntegerField()

        