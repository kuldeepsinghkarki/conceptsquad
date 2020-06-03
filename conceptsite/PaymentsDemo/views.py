from django.shortcuts import render
from PaymentsDemo import ModelSaver as ms
from PaymentsDemo import modelplotter as mp
from PaymentsDemo.forms import PaymentTransactionForm
from django.http import HttpResponse
import numpy as np

from PaymentsDemo.models import PaymentTransaction
from PaymentsDemo.models import TrainedModel

# Create your views here.

def dashboard(request):
    ms.checkprint('its me')
    td = ([[1,2,3,4,5,6],[2,2,3,3,4,5]])
    model = ms.trainData(td)
    ms.saveTrainedModelJson(model,'kuldeep')
    return render(request, 'dashboard.html', {})


# Create your views here.
def dashboard(request):
    ms.checkprint('its me')
    td = ([[1,2,3,4,5,6],[2,2,3,3,4,5]])
    model = ms.trainData(td)
    ms.saveTrainedModelJson(model,'kuldeep')
    return render(request, 'dashboard.html', {})

def tmp(request):
    from sklearn import svm
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    import pickle
    
    if request.method == 'POST':  
        paymentTransaction = PaymentTransactionForm(request.POST)  
        arr = [[paymentTransaction.data['amountRange'],
                paymentTransaction.data['time'],
                paymentTransaction.data['mode'],
                paymentTransaction.data['receiver'],
                paymentTransaction.data['location'],
                paymentTransaction.data['balancePercent']]]
        val = ms.checkTransaction(paymentTransaction.data['customerId'],arr)
        if(val == -999):
            context = {"testMessage":"Trained Model not found for "+paymentTransaction.data['customerId']}
            return render(request,'PredictedTransaction.html',context)
        
        
        jsonModel = ms.loadTrainedModelDetails(paymentTransaction.data['customerId'])
        modelImage = mp.getModelPlot(jsonModel['model'],jsonModel['modelRefData'],
                                         jsonModel['scalar'],jsonModel['pca'],arr)
        scalar = pickle.loads(jsonModel['scalar'])
        pcaAnalyzer = pickle.loads(jsonModel['pca'])
        plottedAt = scalar.transform(arr)
        plottedAt  = "Transaction plotted at "+ str(pcaAnalyzer.transform(plottedAt))
        
        if(val == 1):        
            paymentTransaction.save()            
            context = {"modelImage": modelImage,"testMessage":"Transaction looks OK ","plottedAt":plottedAt}
        else:
            context = {"modelImage": modelImage,"testMessage":"Transaction looks Suspicious !!!","plottedAt":plottedAt }
          
        return render(request,'PredictedTransaction.html',context)
    else:  
        paymentTransaction = PaymentTransactionForm()  
        return render(request,"PaymentTransaction_form.html",{'form':paymentTransaction})
    

# Save test transaction if it safe else just display a warning message
def testPaymentTransaction(request):
    from sklearn import svm
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from PaymentsDemo.models import LearnedModel
    import pickle
    
    if request.method == 'POST':  
        paymentTransaction = PaymentTransactionForm(request.POST)  
        arr = [[paymentTransaction.data['amountRange'],
                paymentTransaction.data['time'],
                paymentTransaction.data['mode'],
                paymentTransaction.data['receiver'],
                paymentTransaction.data['location'],
                paymentTransaction.data['balancePercent']]]      
        try:
            custId = paymentTransaction.data['customerId']
            learnedModel = LearnedModel.objects.get(customerId=custId) 
            scalar = pickle.loads(learnedModel.scalar)
            pcaAnalyzer = pickle.loads(learnedModel.pca)
            model = pickle.loads(learnedModel.model)
            record = scalar.transform(arr)
            record = pcaAnalyzer.transform(record)
            val = model.predict(record)
            
            modelImage = mp.getModelPlot(learnedModel.model,learnedModel.modelRefData,
                                         learnedModel.scalar,learnedModel.pca,arr)
            
            plottedAt = scalar.transform(arr)
            plottedAt  = "Transaction plotted at "+ str(pcaAnalyzer.transform(plottedAt))
            if(val == 1):        
                paymentTransaction.save()            
                context = {"modelImage": modelImage,"testMessage":"Transaction looks OK ","plottedAt":plottedAt}
            else:
                context = {"modelImage": modelImage,"testMessage":"Transaction looks Suspicious !!!","plottedAt":plottedAt }
            return render(request,'PredictedTransaction.html',context)
        except LearnedModel.DoesNotExist:
            context = {"testMessage":"Trained Model not found for "+paymentTransaction.data['customerId']}
            return render(request,'PredictedTransaction.html',context)
        
    else:  
        paymentTransaction = PaymentTransactionForm()  
        return render(request,"PaymentTransaction_form.html",{'form':paymentTransaction})
    
    

        
# train the model for customer path parameter
def trainData(request, custId):
    import pickle
    from PaymentsDemo.models import LearnedModel
    qs = PaymentTransaction.objects.filter(customerId=custId)
    if not qs.exists():
        msg = "Training Data not found for "+custId
        return render(request,'TrainTransactionResult.html',{'msg':msg})
    else:
        vlqs = qs.values_list('amountRange','time','mode','receiver','location','balancePercent')
        listob = list(vlqs)
        model = ms.trainData(listob)
        try:
            trainedModel = LearnedModel.objects.get(customerId=custId)
            trainedModel.model = pickle.dumps(model['model'])
            trainedModel.modelRefData = pickle.dumps(model['modelRefData'])
            trainedModel.scalar = pickle.dumps(model['scalar'])
            trainedModel.pca = pickle.dumps(model['pca'])
            trainedModel.save()        
            msg = "Updated Trained Data for "+custId + " with id " +str(trainedModel.id)
            return render(request,'TrainTransactionResult.html',{'msg':msg})
        except LearnedModel.DoesNotExist:      
            trainedModel = LearnedModel()
            trainedModel.customerId = custId
            trainedModel.model = pickle.dumps(model['model'])
            trainedModel.modelRefData = pickle.dumps(model['modelRefData'])
            trainedModel.scalar = pickle.dumps(model['scalar'])
            trainedModel.pca = pickle.dumps(model['pca'])
            trainedModel.save()
            msg = "Data Trained successfuly for "+custId + " with id " +str(trainedModel.id)
            return render(request,'TrainTransactionResult.html',{'msg':msg})
        
def generateTrainingModel(request):
    from PaymentsDemo.forms import TrainingModelForm
    
    if request.method == 'POST':
        form = TrainingModelForm(request.POST)
        if form.is_valid():
            customerId = form.cleaned_data['customerId']
            return trainData(request,customerId)
        
    else:
        form = TrainingModelForm(request.GET)
        msg = ""
        return render(request,'TrainTransaction.html',{'msg':msg,'form':form})
    

