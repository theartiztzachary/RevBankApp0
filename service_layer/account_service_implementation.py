from data_access_layer.account_implementation import AccountDataImplementation
from entities.account_service_interface import AccountServiceInterface
from entities.account_data_object import AccountData

from custom_exceptions.invalid_data_type import InvalidDataType

account_data_layer = AccountDataImplementation()

class AccountServiceImplementation(AccountServiceInterface):
    def create_new_account(self, client_id: str, starting_amount: float) -> str:
        if type(client_id) == str and (type(starting_amount) == float or type(starting_amount) == int):
            new_account_data = AccountData(client_id, starting_amount)
            new_account_id = account_data_layer.create_new_account(new_account_data)
            return new_account_id
        raise InvalidDataType("That is not a valid input type. Please double check your input.")

    def view_account_balance(self, client_id: str, account_id: str) -> float:
        if type(client_id) == str and type(account_id) == str:
            viewed_accounts = account_data_layer.view_account_balance(client_id, account_id)
            return viewed_accounts
        raise InvalidDataType("That is not a valid input type. Please double check your input.")

    def withdraw_from_account(self, client_id: str, account_id: str, withdraw_amount: float) -> float:
        if type(client_id) == str and type(account_id) == str and (type(withdraw_amount) == float or type(withdraw_amount) == int):
            remaining_total = account_data_layer.withdraw_from_account(client_id, account_id, withdraw_amount)
            return remaining_total
        raise InvalidDataType("That is not a valid input type. Please double check your input.")

    def deposit_into_account(self, client_id: str, account_id: str, deposit_amount: float) -> float:
        pass

    def delete_account(self, client_id: str, account_id: str) -> bool:
        pass