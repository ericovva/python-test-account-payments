from rest_framework import serializers
from payment.models import Payment


# дока к сериализатору
# сокращать мб не стоит?
class PaymentSer(serializers.ModelSerializer):
    def validate(self, data):
        if data.get('amount', 0) < 0:
            raise serializers.ValidationError('Amount less than zero')
            # super(PaymentSer, self) - наследие второго питона. пиши просто super()
        return super(PaymentSer, self).validate(data)

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('direction', 'tr_hash',)

