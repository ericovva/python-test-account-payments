from rest_framework import serializers
from account.models import Account

# дока и сокращение
class AccountSer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
