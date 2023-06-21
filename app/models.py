from django.db import models

# Create your models here.
class Bank(models.Model):
    BankName=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.BankName
    
class BankBranch(models.Model):
    BankName=models.ForeignKey(Bank,on_delete=models.CASCADE)
    IFSC=models.CharField(max_length=100,primary_key=True)
    Branch=models.CharField(max_length=100)
    Address=models.TextField()
    Contact=models.IntegerField()
    City=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    State=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Branch