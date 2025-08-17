from django.db import models

# Create your models here.

class InsuranceCompanyModel(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class ClientModel(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    # balance = models.DecimalField(max_digits=10, decimal_places=2)

class AgentModel(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)


class PolicyModel(models.Model):
    policy_number = models.CharField(max_length=255)
    issue_date = models.DateField()
    car_model = models.CharField(max_length=255)
    engine_type = models.CharField(max_length=255)

    payment_status = models.CharField(max_length=100, choices=[('active', 'active'), ('complete', 'complete'), ('cancel', 'cancel')])
    payment_method = models.CharField(max_length=100, choices=[('cash', 'cash'), ('bank', 'bank')])

    remarks = models.TextField()
    reference_number = models.IntegerField()


    gross_price = models.DecimalField(max_digits=10, decimal_places=2)
    co_rate = models.DecimalField(max_digits=10, decimal_places=2)
    client_price = models.DecimalField(max_digits=10, decimal_places=2)



    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentModel, on_delete=models.CASCADE)
    insurance_company = models.ForeignKey(InsuranceCompanyModel, on_delete=models.CASCADE)


    

class TranscationLedger(models.Model):
    policy = models.ForeignKey(PolicyModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=100, choices=[('cancelled', 'cancelled'), ('payment', 'payment'), ('credit_adjustment', 'credit_adjustment'), ('payback', 'payback')])
    description = models.TextField(blank=True, null=True)