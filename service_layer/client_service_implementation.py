from data_access_layer.client_implementation import ClientDataImplementation
from entities.client_service_interface import ClientServiceInterface
from entities.client_data_object import ClientDataInit

from custom_exceptions.invalid_data_type import InvalidDataType

class ClientServiceImplementation(ClientServiceInterface):
    def __init__(self, client_dal: ClientDataImplementation):
        self.client_dal = client_dal

    def create_new_client(self, first_name: str, last_name: str) -> str:
        if type(first_name) == str and type(last_name) == str:
            new_client_data = ClientDataInit(first_name, last_name)
            new_client_id = self.client_dal.create_new_client(new_client_data)
            return new_client_id
        raise InvalidDataType("That is not a valid input type. Please double check your input.")

    def get_all_accounts_by_id(self, client_id: str) -> str:
        if type(client_id) == str:
            viewed_accounts = self.client_dal.get_all_accounts_by_id(client_id)
            return viewed_accounts
        raise InvalidDataType("That is not a valid input type. Please double check your input.")

    def transfer_between_accounts(self, client_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> bool:
        if type(transfer_amount) != bool:
            try:
                transfer_float = float(transfer_amount)
                if type(client_id) == str and type(account_from_id) == str and type(account_to_id) == str:
                    transfer_result = self.client_dal.transfer_between_accounts(client_id, account_from_id, account_to_id, transfer_float)
                    return transfer_result
                raise InvalidDataType("That is not a valid input type. Please double check your input.")
            except ValueError:
                raise InvalidDataType("That is not a valid input type. Please double check your input.")
        raise InvalidDataType("That is not a valid input type. Please double check your input.")

    def delete_client(self, client_id: str) -> bool:
        if type(client_id) == str:
            delete_result = self.client_dal.delete_client(client_id)
            return delete_result
        raise InvalidDataType("That is not a valid input type. Please double check your input.")