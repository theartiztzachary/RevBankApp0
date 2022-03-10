from entities.account_interface import AccountInterface
from entities.account_data import AccountData
from utilities.connection_manager import connection

from utilities.custom_exceptions import ClientIDNotFound

class AccountDataImplementation(AccountInterface):
    account_id_value = 1

    def create_new_account(self, client_id: str, starting_amount: float) -> AccountData:
        sql_get_query = "select client_id from clients"
        cursor_get = connection.cursor()
        cursor_get.execute(sql_get_query)
        clients_in_db = cursor_get.fetchall()
        for client in clients_in_db:
            if client == client_id:
                new_account_id = f"{client_id}{self.account_id_value}"
                AccountDataImplementation.account_id_value += 1
                sql_post_query = "insert into accounts values(%s, %s, %s)"
                cursor = connection.cursor()
                cursor.execute(sql_post_query, (client_id, new_account_id, starting_amount))
                new_account_data = AccountData(client_id, new_account_id, starting_amount)
                return new_account_data
        raise ClientIDNotFound("Client ID does not exist.")

    def view_account_information(self, client_id: str, account_id: str) -> AccountData:
        pass

    def withdraw_from_account(self, client_id: str, account_id: str, withdraw_amount: float) -> AccountData:
        pass

    def deposit_into_account(self, client_id: str, account_id: str, deposit_amount: float) -> AccountData:
        pass

    def delete_account(self, client_id: str, account_id: str) -> bool:
        pass