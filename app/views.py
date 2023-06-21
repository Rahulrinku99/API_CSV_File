from django.shortcuts import render
from app.models import *
import csv
from django.http import HttpResponse
# Create your views here.

def bank_upload(request):
    a = 'C:\\Users\\Hp\\OneDrive\\Desktop\\API\\rahul\\Scripts\\bank\\bank.csv'
    
    with open(a, 'r') as file:
        csv_data = csv.reader(file)
          # Skip the header row if it exists
        next(csv_data)
        for row in csv_data:
            bn=row[0].strip()
            instance = Bank(BankName=bn,)  
            instance.save()
        return HttpResponse('successful')
    
def branch_upload(file_path):
    b = 'C:\\Users\\Hp\\OneDrive\\Desktop\\API\\rahul\\Scripts\\bank\\branch1.csv'
    
    with open(b, 'r') as file:
        csv_data = csv.reader(file)
          # Skip the header row if it exists
        next(csv_data)
        for row in csv_data:
              BankName = row[0]
              print(row[0])
              bo = Bank.objects.filter(BankName=BankName)[0]
              instance = BankBranch(
                      BankName=bo,            
                      
                      IFSC = row[1],
                      Branch = row[2],
                      Address =row[3],
                      Contact=row[4],
                      City = row[5],
                      District = row[6],
                      State = row[7],)
                                  
              instance.save()
        return HttpResponse('successful')