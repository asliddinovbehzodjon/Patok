from import_export import resources
from .models import Worker,Work
class WorkerResources(resources.ModelResource):
    class Meta:
        model = Worker
class WorkResources(resources.ModelResource):
    class Meta:
        model = Work