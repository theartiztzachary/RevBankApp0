from entities.client_data_interface import ClientDataInterface
from entities.client_data_object import ClientData
from entities.account_data_object import AccountData

from custom_exceptions.client_id_not_found import ClientIDNotFound
from custom_exceptions.no_accounts import NoAccountsForClient
from custom_exceptions.inadequate_funds import InadequateFunds
from custom_exceptions.account_id_not_found import AccountIDNotFound
from custom_exceptions.input_too_long import InputTooLong
from custom_exceptions.accounts_still_exist import AccountsStillExist

class ClientDataImplementation(ClientDataInterface):
    client_database = {}

    def __init__(self):
        ##-Begin hard-coded test data.-##
        self.mekio_client = ClientData("Mekio", "Nefta")
        self.mekio_client_id = self.mekio_client.client_id

        self.salvador_client = ClientData("Salvador", "Veluvaza")
        self.salvador_client_id = self.salvador_client.client_id
        self.salvador_account_one = AccountData(self.salvador_client_id, 50)
        self.salvador_account_one_id = self.salvador_account_one.account_id
        self.salvador_account_two = AccountData(self.salvador_client_id, 100)
        self.salvador_account_two_id = self.salvador_account_two.account_id
        self.salvador_client.client_accounts[self.salvador_account_one_id] = self.salvador_account_one
        self.salvador_client.client_accounts[self.salvador_account_two_id] = self.salvador_account_two

        self.luken_client = ClientData("Luken", "VonTelan")
        self.luken_client_id = self.luken_client.client_id

        self.zandel_client = ClientData("Zandel", "Horris")
        self.zandel_client_id = self.zandel_client.client_id
        self.zandel_account = AccountData(self.zandel_client_id, 50)
        self.zandel_account_id = self.zandel_account.account_id
        self.zandel_client.client_accounts[self.zandel_account_id] = self.zandel_account

        self.isaac_client = ClientData("Isaac", "Daurcour")
        self.isaac_client_id = self.isaac_client.client_id

        self.hamel_client = ClientData("Hamel", "Bergstrom")
        self.hamel_client_id = self.hamel_client.client_id
        self.hamel_account = AccountData(self.hamel_client_id, 0)
        self.hamel_account_id = self.hamel_account.account_id
        self.hamel_client.client_accounts[self.hamel_account_id] = self.hamel_account

        self.client_database[self.mekio_client_id] = self.mekio_client
        self.client_database[self.salvador_client_id] = self.salvador_client
        self.client_database[self.luken_client_id] = self.luken_client
        self.client_database[self.zandel_client_id] = self.zandel_client
        self.client_database[self.hamel_client_id] = self.hamel_client
        self.client_database[self.isaac_client_id] = self.isaac_client
        ##-End hard-coded test data.-##

    def create_new_client(self, client: ClientData) -> str:
        if len(client.first_name) <= 20:
            if len(client.last_name) <= 20:
                ClientDataImplementation.client_database[client.client_id] = client
                return client.client_id
            raise InputTooLong("Inputted last name is too long. Last names must be less than 20 characters.")
        raise InputTooLong("Inputted first name is too long. First names must be less than 20 characters.")

    def get_all_accounts_by_id(self, client_id: str) -> str:
        return_string = ""
        for client in ClientDataImplementation.client_database.keys():
            if client == client_id:
                if len(ClientDataImplementation.client_database[client].client_accounts) > 0:
                    for account in ClientDataImplementation.client_database[client].client_accounts.keys():
                        return_string += f"Account: {account}, Balance: {ClientDataImplementation.client_database[client].client_accounts[account].current_balance} // "
                    return return_string
                raise NoAccountsForClient("There are no accounts associated with that client.")
        raise ClientIDNotFound("Client ID does not exist.")

    def transfer_between_accounts(self, client_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> bool:
        account_one: AccountData
        account_two: AccountData
        have_account_one = False
        have_account_two = False
        for client in ClientDataImplementation.client_database.keys():
            if client == client_id:
                for account in ClientDataImplementation.client_database[client].client_accounts.keys():
                    if account == account_from_id:
                        account_one = ClientDataImplementation.client_database[client].client_accounts[account]
                        have_account_one = True
                    elif account == account_to_id:
                        account_two = ClientDataImplementation.client_database[client].client_accounts[account]
                        have_account_two = True

                    if have_account_one and have_account_two:
                        if account_one.current_balance - transfer_amount >= 0:
                            account_one.current_balance -= transfer_amount
                            account_two.current_balance += transfer_amount
                            return True
                        raise InadequateFunds("You do not have enough funds in the given account to complete the transaction.")
                raise AccountIDNotFound("There are no accounts associated with that ID.")
        raise ClientIDNotFound("Client ID does not exist.")

    def delete_client(self, client_id: str) -> bool:
        for client in ClientDataImplementation.client_database.keys():
            if client == client_id:
                if len(ClientDataImplementation.client_database[client].client_accounts) == 0:
                    del ClientDataImplementation.client_database[client]
                    return True
                raise AccountsStillExist("There are still accounts associated with that client. Please close all accounts before removing the client.")
        raise ClientIDNotFound("Client ID does not exist.")