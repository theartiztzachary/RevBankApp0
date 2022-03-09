from abc import ABC, abstractmethod
from entities.account_data import AccountData

class AccountInterface(ABC):

    @abstractmethod
    def create_new_account(self, client_id: str, starting_amount: float) -> AccountData:
        pass

    @abstractmethod
    def view_account_information(self, client_id: str, account_id: str) -> AccountData:
        pass

    @abstractmethod
    def withdraw_from_account(self, client_id: str, account_id: str, withdraw_amount: float) -> AccountData:
        pass

    @abstractmethod
    def deposit_into_account(self, client_id: str, account_id: str, deposit_amount: float) -> AccountData:
        pass

    @abstractmethod
    def delete_account(self, client_id: str, account_id: str) -> bool:
        pass
