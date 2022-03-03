from data_access_layer.client_implementation import ClientDataImplementation
from entities.client_service_interface import ClientServiceInterface
from entities.client_data_object import ClientData

from custom_exceptions.invalid_data_type import InvalidDataType

client_data_layer = ClientDataImplementation()

class ClientServiceImplementation(ClientServiceInterface):
    def create_new_client(self, first_name: str, last_name: str) -> str:
        if type(first_name) == str and type(last_name) == str:
            new_client_data = ClientData(first_name, last_name)
            new_client_id = client_data_layer.create_new_client(new_client_data)
            return new_client_id
        raise InvalidDataType("That is not a valid input type. Please double check your input.")

    def get_all_accounts_by_id(self, client: str) -> str:
        pass

    def transfer_between_accounts(self, client_from_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> bool:
        pass

    def delete_client(self, client_id: str) -> bool:
        pass