from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('work',WorkViewset)
router.register('worker',WorkerViewset),
router.register('another',AnotherViewset)
urlpatterns = [
    path('',include(router.urls))
]