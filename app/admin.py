from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from .resources import *
@admin.register(Worker)
class WorkerAdmin(ImportExportModelAdmin):
    resource_class = WorkerResources
    list_filter = ['salary','address','age']
    list_display = ['name','salary','address','job']
    search_fields = ['name','salary','addess','job','age']
    list_per_page = 10
@admin.register(Work)
class WorkAdmin(ImportExportModelAdmin):
    resource_class = WorkResources
    list_display = ['company','job','phone']
    list_filter = ['salary','job']
    list_per_page = 10
    search_fields = ['company','salary','addess','job']
# Register your models here.
admin.site.register(Another)
