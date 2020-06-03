from django import forms
from PaymentsDemo.models import PaymentTransaction

class PaymentTransactionForm(forms.ModelForm):
  #  customerId = forms.CharField(label="Enter Customer Id",max_length=50)  
  #  amountRange = forms.IntegerField(label="Enter amount range value")
  #  time = forms.IntegerField(label="Enter time value")
  #  mode = forms.IntegerField(label="Enter time value")
  #  receiver = forms.IntegerField(label="Enter time value")
  #  location = forms.IntegerField(label="Enter time value")
  #  balancePercent = forms.IntegerField(label="Enter time value")
    class Meta:  
       model = PaymentTransaction  
       fields = "__all__"  
    
class TrainingModelForm(forms.Form):
    customerId = forms.CharField(help_text = "Enter customer id for whome model needs to be trained")
    