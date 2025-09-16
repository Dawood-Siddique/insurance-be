from django.db import models

# Create your models here.

class InsuranceCompanyModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class ClientModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    # balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name}"

class VendorModel(models.Model):
    name = models.CharField(max_length=225, unique=True)
    
    def __str__(self):
        return f"{self.name}"

class AgentModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class PolicyModel(models.Model):
    issue_date = models.DateField()
    insurance_company = models.ForeignKey(InsuranceCompanyModel, on_delete=models.CASCADE, blank=True, null=True)
    policy_number = models.CharField(max_length=255, unique=True)
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE, blank=True, null=True)
    car_model = models.CharField(max_length=255, blank=True, null=True)
    engine_type = models.CharField(max_length=255, blank=True, null=True)
    agent = models.ForeignKey(AgentModel, on_delete=models.CASCADE, blank=True, null=True)

    gross_price = models.DecimalField(max_digits=10, decimal_places=2)
    co_rate = models.DecimalField(max_digits=10, decimal_places=2)
    client_price = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(max_length=100, choices=[('cash', 'cash'), ('bank', 'bank')])
    payment_status = models.CharField(max_length=100, choices=[('active', 'active'), ('complete', 'complete'), ('cancelled', 'cancelled')])
    remarks = models.TextField(blank=True, null=True)
    reference_number = models.IntegerField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)

    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE, blank=True, null=True)



class TranscationLedger(models.Model):
    policy = models.ForeignKey(PolicyModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=100, choices=[('cancelled', 'cancelled'), ('payment', 'payment'), ('credit_adjustment', 'credit_adjustment'), ('payback', 'payback')])
    description = models.TextField(blank=True, null=True)