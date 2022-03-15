from entities.client_data import ClientData
from entities.client_interface import ClientInterface
from data_access_layer.client_data_implementation import ClientDataImplementation

from utilities.custom_exceptions import InvalidDataType

class ClientServiceImplementation(ClientInterface):
    def __init__(self, data_imp: ClientDataImplementation):
        self.data_imp = data_imp

    def create_new_client(self, first_name: str, last_name: str) -> ClientData:
        if type(first_name) != str:
            raise InvalidDataType("Entered first name is not a valid data type. Please double check your input.")
        if type(last_name) != str:
            raise InvalidDataType("Entered last name is not a valid data type. Please double check your input.")
        returned_client = self.data_imp.create_new_client(first_name, last_name)
        return returned_client

    def view_all_client_accounts(self, client_id: str) -> ClientData:
        if type(client_id) != str:
            raise InvalidDataType("Client ID is not a valid data type. Please double check your input.")
        returned_client = self.data_imp.view_all_client_accounts(client_id)
        return returned_client

    def transfer_between_accounts(self, client_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> ClientData:
        transfer_balance: float
        if type(client_id) != str:
            raise InvalidDataType("Client ID is not a valid data type. Please double check your input.")
        if type(account_from_id) != str:
            raise InvalidDataType("Account ID is not a valid data type. Please double check your input.")
        if type(account_to_id) != str:
            raise InvalidDataType("Account ID is not a valid data type. Please double check your input.")
        if type(transfer_amount) == bool:
            raise InvalidDataType("Transfer amount is not a valid data type. Please double check your input.")
        try:
            transfer_balance = float(transfer_amount)
        except ValueError:
            raise InvalidDataType("Transfer amount is not a valid data type. Please double check your input.")
        returned_client = self.data_imp.transfer_between_accounts(client_id, account_from_id, account_to_id, transfer_balance)
        return returned_client

    def delete_client(self, client_id: str) -> bool:
        if type(client_id) != str:
            raise InvalidDataType("Client ID is not a valid data type. Please double check your input.")
        delete_result = self.data_imp.delete_client(client_id)
        return delete_result