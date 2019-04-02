from django.contrib import admin
from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'balance',
        'currency',
    )
    search_fields = ('id', 'currency',)


admin.site.register(Account, AccountAdmin)
