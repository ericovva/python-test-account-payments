from rest_framework.exceptions import APIException

class CurrenciesNotMatched(APIException):
    status_code = 400
    default_detail = "Account currencies don't match."
    default_code = 'currencies_not_matched'


class AccountsNotFound(APIException):
    status_code = 404
    default_detail = "Accounts not found"
    default_code = 'accounts_not_found'


class NotEnoughMoney(APIException):
    status_code = 400
    default_detail = "Not enough money"
    default_code = 'not_enough_money'
