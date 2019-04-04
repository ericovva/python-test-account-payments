from rest_framework.viewsets import ModelViewSet
from account import serializers as account_serializers
from account import models as account_models

import logging
logger = logging.getLogger('django')
# логгер не используется

class Account(ModelViewSet):
    queryset = account_models.Account.objects.all()
    serializer_class = account_serializers.AccountSer
    http_method_names = ['get']
