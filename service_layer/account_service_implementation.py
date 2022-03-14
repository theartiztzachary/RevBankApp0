from entities.account_data import AccountData
from entities.account_interface import AccountInterface
from data_access_layer.account_data_implementation import AccountDataImplementation

class AccountServiceImplementation(AccountInterface):
    def __init__(self, data_imp: AccountDataImplementation):
        self.data_imp = data_imp

    def create_new_account(self, client_id: str, starting_amount: float) -> AccountData:
        pass

    def view_account_information(self, client_id: str, account_id: str) -> AccountData:
        pass

    def withdraw_from_account(self, client_id: str, account_id: str, withdraw_amount: float) -> AccountData:
        pass

    def deposit_into_account(self, client_id: str, account_id: str, deposit_amount: float) -> AccountData:
        pass

    def delete_account(self, client_id: str, account_id: str) -> bool:
        pass