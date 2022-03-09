from abc import ABC, abstractmethod
from entities.client_data import ClientData

class ClientInterface(ABC):

    @abstractmethod
    def create_new_client(self, first_name: str, last_name: str) -> ClientData:
        pass

    @abstractmethod
    def view_all_client_accounts(self, client_id: str) -> ClientData:
        pass

    @abstractmethod
    def transfer_between_accounts(self, client_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> ClientData:
        pass

    @abstractmethod
    def delete_client(self, client_id: str) -> bool:
        pass