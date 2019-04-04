from django.conf.urls import url, include
from payment.views import *
# Говорят никогда не стоит сипользовать *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', Payment)

urlpatterns = [
    url(r'^', include(router.urls)),
]
