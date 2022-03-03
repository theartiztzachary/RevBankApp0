from data_access_layer.client_implementation import ClientDataImplementation
from entities.client_service_interface import ClientServiceInterface
from entities.client_data_object import ClientData

from custom_exceptions.invalid_data_type import InvalidDataType

class ClientServiceImplementation(ClientServiceInterface):
    def __init__(self, client_dal: ClientDataImplementation):
        self.client_dal = client_dal

    def create_new_client(self, first_name: str, last_name: str) -> str:
        if type(first_name) == str and type(last_name) == str:
            new_client_data = ClientData(first_name, last_name)
            new_client_id = self.client_dal.create_new_client(new_client_data)
            return new_client_id
        raise InvalidDataType("That is not a valid input type. Please double check your input.")

    def get_all_accounts_by_id(self, client_id: str) -> str:
        if type(client_id) == str:
            viewed_accounts = self.client_dal.get_all_accounts_by_id(client_id)
            return viewed_accounts
        raise InvalidDataType("That is not a valid input type. Please double check your input.")

    def transfer_between_accounts(self, client_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> bool:
        pass

    def delete_client(self, client_id: str) -> bool:
        pass