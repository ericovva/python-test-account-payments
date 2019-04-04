from django.contrib import admin
from payment.models import Payment

# я предпочитаю использовать декоратор
# @admin.register(Payment)
# дока
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'account',
        'amount',
        'to_account',
        'direction',
        'tr_hash',
    )
    search_fields = ('id', 'account__id', 'to_account__id', 'tr_hash',)

admin.site.register(Payment, PaymentAdmin)
