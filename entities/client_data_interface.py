from abc import ABC, abstractmethod
from entities.client_data_object import ClientData


class ClientDataInterface(ABC):

    @abstractmethod
    def create_new_client(self, client: ClientData) -> str:
        pass

    @abstractmethod
    def get_all_accounts_by_id(self, client: str) -> str:
        pass

    @abstractmethod
    def transfer_between_accounts(self, client_from_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> bool:
        pass

    @abstractmethod
    def delete_client(self, client_id: str) -> bool:
        pass