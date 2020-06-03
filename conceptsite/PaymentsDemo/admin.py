from django.contrib import admin

# Register your models here.
from .models import TrainedModel
from .models import PaymentTransaction
from .models import LearnedModel
from import_export.admin import ImportExportModelAdmin

admin.site.register(TrainedModel)
admin.site.register(LearnedModel)

admin.site.site_url = "/payments/generateTrainingModel"

@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(ImportExportModelAdmin):
    pass
