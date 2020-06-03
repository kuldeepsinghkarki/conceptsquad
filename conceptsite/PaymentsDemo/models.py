from django.db import models

# Create your models here.

class TrainedModel(models.Model):
  customerId = models.CharField(max_length=200)
  modelId = models.CharField(max_length=150)
  def __str__(self):
        return self.customerId + " : " + self.modelId

class LearnedModel(models.Model):
  customerId = models.CharField(max_length=200)
  model = models.BinaryField()
  modelRefData = models.BinaryField()
  scalar = models.BinaryField()
  pca = models.BinaryField()

  def __str__(self):
        return self.customerId + "-"+ str(self.id)
    
class PaymentTransaction(models.Model):
  customerId = models.CharField(max_length=200)
  amountRange = models.IntegerField(default=1)
  time = models.IntegerField(default=1)
  mode = models.IntegerField(default=1)
  receiver = models.IntegerField(default=1)
  location = models.IntegerField(default=1)
  balancePercent = models.IntegerField(default=1)
      
  def __str__(self):
        return self.customerId + "-" + str(self.amountRange) + str(self.time)+ str(self.mode)+ str(self.receiver)+ str(self.location)+ str(self.balancePercent)
