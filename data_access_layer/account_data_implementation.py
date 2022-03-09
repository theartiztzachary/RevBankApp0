from entities.account_interface import AccountInterface
from entities.account_data import AccountData
from utilities.connection_manager import connection
from utilities.custom_exceptions import ClientIDNotFound, AccountIDNotFound, NoAccounts, InadequateFunds, FundsStillExist, AccountsStillExist

class AccountDataImplementation(AccountInterface):
    account_id_value = 1

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