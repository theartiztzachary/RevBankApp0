from abc import ABC, abstractmethod
from entities.account_data_object import AccountDataInit

class AccountDataInterface(ABC):

    @abstractmethod
    def create_new_account(self, account: AccountDataInit) -> str:
        pass

    @abstractmethod
    def view_account_balance(self, client_id: str, account_id: str) -> float:
        pass

    @abstractmethod
    def withdraw_from_account(self, client_id: str, account_id: str, withdraw_amount: float) -> float:
        pass

    @abstractmethod
    def deposit_into_account(self, client_id: str, account_id: str, deposit_amount: float) -> float:
        pass

    @abstractmethod
    def delete_account(self, client_id: str, account_id: str) -> bool:
        pass