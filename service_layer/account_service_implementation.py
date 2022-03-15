from entities.account_data import AccountData
from entities.account_interface import AccountInterface
from data_access_layer.account_data_implementation import AccountDataImplementation

from utilities.custom_exceptions import InvalidDataType

class AccountServiceImplementation(AccountInterface):
    def __init__(self, data_imp: AccountDataImplementation):
        self.data_imp = data_imp

    def create_new_account(self, client_id: str, starting_amount: float) -> AccountData:
        starting_balance: float
        if type(client_id) != str:
            raise InvalidDataType("Client ID is not a valid data type. Please double check your input.")
        if type(starting_amount) == bool:
            raise InvalidDataType("Inputted account balance is not a valid data type. Please double check your input.")
        try:
            starting_balance = float(starting_amount)
        except ValueError:
            raise InvalidDataType("Inputted account balance is not a valid data type. Please double check your input.")
        returned_account = self.data_imp.create_new_account(client_id, starting_balance)
        return returned_account

    def view_account_information(self, client_id: str, account_id: str) -> AccountData:
        if type(client_id) != str:
            raise InvalidDataType("Client ID is not a valid data type. Please double check your input.")
        if type(account_id) != str:
            raise InvalidDataType("Account ID is not a valid data type. Please double check your input.")
        returned_account = self.data_imp.view_account_information(client_id, account_id)
        return returned_account

    def withdraw_from_account(self, client_id: str, account_id: str, withdraw_amount: float) -> AccountData:
        withdraw_balance: float
        if type(client_id) != str:
            raise InvalidDataType("Client ID is not a valid data type. Please double check your input.")
        if type(account_id) != str:
            raise InvalidDataType("Account ID is not a valid data type. Please double check your input.")
        if type(withdraw_amount) == bool:
            raise InvalidDataType("Withdraw amount is not a valid data type. Please double check your input.")
        try:
            withdraw_balance = float(withdraw_amount)
        except ValueError:
            raise InvalidDataType("Withdraw amount is not a valid data type. Please double check your input.")
        returned_account = self.data_imp.withdraw_from_account(client_id, account_id, withdraw_balance)
        return returned_account

    def deposit_into_account(self, client_id: str, account_id: str, deposit_amount: float) -> AccountData:
        deposit_balance: float
        if type(client_id) != str:
            raise InvalidDataType("Client ID is not a valid data type. Please double check your input.")
        if type(account_id) != str:
            raise InvalidDataType("Account ID is not a valid data type. Please double check your input.")
        if type(deposit_amount) == bool:
            raise InvalidDataType("Deposit amount is not a valid data type. Please double check your input.")
        try:
            deposit_balance = float(deposit_amount)
        except ValueError:
            raise InvalidDataType("Deposit amount is not a valid data type. Please double check your input.")
        returned_account = self.data_imp.deposit_into_account(client_id, account_id, deposit_balance)
        return returned_account

    def delete_account(self, client_id: str, account_id: str) -> bool:
        if type(client_id) != str:
            raise InvalidDataType("Client ID is not a valid data type. Please double check your input.")
        if type(account_id) != str:
            raise InvalidDataType("Account ID is not a valid data type. Please double check your input.")
        delete_result = self.data_imp.delete_account(client_id, account_id)
        return delete_result