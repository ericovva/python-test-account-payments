from django.conf.urls import url, include
from account.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', Account)

urlpatterns = [
    url(r'^', include(router.urls)),
]
