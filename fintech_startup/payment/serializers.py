from rest_framework import serializers
from payment.models import Payment


class PaymentSer(serializers.ModelSerializer):
    def validate(self, data):
        if data.get('amount', 0) < 0:
            raise serializers.ValidationError('Amount less than zero')
        return super(PaymentSer, self).validate(data)

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('direction', 'tr_hash',)

