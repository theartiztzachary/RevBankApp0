from abc import ABC, abstractmethod

class ClientServiceInterface(ABC):

    @abstractmethod
    def create_new_client(self, first_name: str, last_name: str) -> str:
        pass

    @abstractmethod
    def get_all_accounts_by_id(self, client_id: str) -> str:
        pass

    @abstractmethod
    def transfer_between_accounts(self, client_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> bool:
        pass

    @abstractmethod
    def delete_client(self, client_id: str) -> bool:
        pass