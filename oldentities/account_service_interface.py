from abc import ABC, abstractmethod

class AccountServiceInterface(ABC):

    @abstractmethod
    def create_new_account(self, client_id: str, starting_amount: float) -> str:
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