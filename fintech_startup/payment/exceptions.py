from rest_framework.exceptions import APIException

# доки к ошибкам
class CurrenciesNotMatched(APIException):
    status_code = 400
    default_detail = "Account currencies don't match."
    default_code = 'currencies_not_matched'


class InvalidAccounts(APIException):
    status_code = 400
    default_detail = "Invalid accounts"
    default_code = 'invalid_accounts'


class NotEnoughMoney(APIException):
    status_code = 400
    default_detail = "Not enough money"
    default_code = 'not_enough_money'
