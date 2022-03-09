from entities.client_interface import ClientInterface
from entities.client_data import ClientData

class ClientDataImplementation(ClientInterface):
    client_id_value = 1

    def create_new_client(self, first_name: str, last_name: str) -> ClientData:
        pass

    def view_all_client_accounts(self, client_id: str) -> ClientData:
        pass

    def transfer_between_accounts(self, client_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> ClientData:
        pass

    def delete_client(self, client_id: str) -> bool:
        pass