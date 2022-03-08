from entities.account_data_interface import AccountDataInterface
from entities.account_data_object import AccountDataInit
from data_access_layer.client_implementation import ClientDataImplementation

from custom_exceptions.client_id_not_found import ClientIDNotFound
from custom_exceptions.account_id_not_found import AccountIDNotFound
from custom_exceptions.inadequate_funds import InadequateFunds
from custom_exceptions.funds_still_exist import FundsStillExist

class AccountDataImplementation(AccountDataInterface):

    def create_new_account(self, account: AccountDataInit) -> str:
        for client_id in ClientDataImplementation.client_database.keys():
            if client_id == account.holding_client:
                ClientDataImplementation.client_database[client_id].client_accounts[account.account_id] = account
                return account.account_id
        raise ClientIDNotFound("Client ID does not exist.")

    def view_account_balance(self, client_id: str, account_id: str) -> float:
        for client in ClientDataImplementation.client_database.keys():
            if client == client_id:
                for account in ClientDataImplementation.client_database[client].client_accounts.keys():
                    if account == account_id:
                        balance = ClientDataImplementation.client_database[client].client_accounts[account_id].current_balance
                        return balance
                raise AccountIDNotFound("There are no accounts associated with that ID.")
        raise ClientIDNotFound("Client ID does not exist.")

    def withdraw_from_account(self, client_id: str, account_id: str, withdraw_amount: float) -> float:
        for client in ClientDataImplementation.client_database.keys():
            if client == client_id:
                for account in ClientDataImplementation.client_database[client].client_accounts.keys():
                    if account == account_id:
                        if ClientDataImplementation.client_database[client].client_accounts[account].current_balance - withdraw_amount >= 0:
                            ClientDataImplementation.client_database[client].client_accounts[account].current_balance -= withdraw_amount
                            return ClientDataImplementation.client_database[client].client_accounts[account].current_balance
                        raise InadequateFunds("You do not have enough funds in the given account to complete the transaction.")
                raise AccountIDNotFound("There are no accounts associated with that ID.")
        raise ClientIDNotFound("Client ID does not exist.")

    def deposit_into_account(self, client_id: str, account_id: str, deposit_amount: float) -> float:
        for client in ClientDataImplementation.client_database.keys():
            if client == client_id:
                for account in ClientDataImplementation.client_database[client].client_accounts.keys():
                    if account == account_id:
                        ClientDataImplementation.client_database[client].client_accounts[account].current_balance += deposit_amount
                        return ClientDataImplementation.client_database[client].client_accounts[account].current_balance
                raise AccountIDNotFound("There are no accounts associated with that ID.")
        raise ClientIDNotFound("Client ID does not exist.")

    def delete_account(self, client_id: str, account_id: str) -> bool:
        for client in ClientDataImplementation.client_database.keys():
            if client == client_id:
                for account in ClientDataImplementation.client_database[client].client_accounts.keys():
                    if account == account_id:
                        if ClientDataImplementation.client_database[client].client_accounts[account].current_balance == 0:
                            del ClientDataImplementation.client_database[client].client_accounts[account]
                            return True
                        raise FundsStillExist("There are still funds in that account. Please withdraw or transfer the balance before attempting to close the account.")
                raise AccountIDNotFound("There are no accounts associated with that ID.")
        raise ClientIDNotFound("Client ID does not exist.")