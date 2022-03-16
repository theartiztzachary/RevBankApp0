from entities.account_interface import AccountInterface
from entities.account_data import AccountData
from utilities.connection_manager import connection

from utilities.custom_exceptions import ClientIDNotFound, AccountIDNotFound, NoAccounts, InadequateFunds, FundsStillExist

## A lot of this logic is bloated with extra checks. Once everything is baseline in place and working, will go back and try to reduce
# the bloat if there is time.

class AccountDataImplementation(AccountInterface):
    account_id_value = 1

    def create_new_account(self, client_id: str, starting_amount: float) -> AccountData:
        sql_get_query = "select client_id from clients where client_id = %s"
        cursor_get = connection.cursor()
        cursor_get.execute(sql_get_query, [client_id])
        clients_in_db = cursor_get.fetchone()
        try:
            if len(clients_in_db) > 0:
                new_account_id = f"{client_id}{self.account_id_value}"
                AccountDataImplementation.account_id_value += 1
                sql_post_query = "insert into accounts values(%s, %s, %s)"
                cursor = connection.cursor()
                cursor.execute(sql_post_query, (client_id, new_account_id, starting_amount))
                connection.commit()
                new_account_data = AccountData(client_id, new_account_id, starting_amount)
                return new_account_data
            raise ClientIDNotFound("Client ID does not exist.") #this might be redundant due to the try/except block
        except TypeError:
            raise ClientIDNotFound("Client ID does not exist.")

    def view_account_information(self, client_id: str, account_id: str) -> AccountData:
        sql_get_clients_query = "select client_id from clients where client_id = %s"
        cursor_get_clients = connection.cursor()
        cursor_get_clients.execute(sql_get_clients_query, [client_id])
        clients_in_db = cursor_get_clients.fetchone()
        try:
            if len(clients_in_db) > 0:
                sql_get_accounts_query = "select account_id from accounts where client_id = %s"
                cursor_get_accounts = connection.cursor()
                cursor_get_accounts.execute(sql_get_accounts_query, [client_id])
                accounts_for_client = cursor_get_accounts.fetchall()
                try:
                    if len(accounts_for_client) > 0:
                        for i in range(len(accounts_for_client)):
                            if accounts_for_client[i][0] == account_id:
                                sql_get_information_query = "select * from accounts where account_id = %s"
                                cursor_get_info = connection.cursor()
                                cursor_get_info.execute(sql_get_information_query, [account_id])
                                account_in_db = cursor_get_info.fetchone()
                                returned_account = AccountData(*account_in_db)
                                return returned_account
                        raise AccountIDNotFound("There are no accounts associated with that ID.")
                    raise NoAccounts("There are no accounts associated with that client.") #this might be redundant due to the try/except block
                except TypeError:
                    raise NoAccounts("There are no accounts associated with that client.")
            raise ClientIDNotFound("Client ID does not exist.") #this might be redundant due to the try/except block
        except TypeError:
            raise ClientIDNotFound("Client ID does not exist.")

    def withdraw_from_account(self, client_id: str, account_id: str, withdraw_amount: float) -> AccountData:
        sql_get_clients_query = "select client_id from clients where client_id = %s"
        cursor_get_clients = connection.cursor()
        cursor_get_clients.execute(sql_get_clients_query, [client_id])
        clients_in_db = cursor_get_clients.fetchone()
        try:
            if len(clients_in_db) > 0:
                sql_get_accounts_query = "select account_id from accounts where client_id = %s"
                cursor_get_accounts = connection.cursor()
                cursor_get_accounts.execute(sql_get_accounts_query, [client_id])
                accounts_for_client = cursor_get_accounts.fetchall()
                try:
                    if len(accounts_for_client) > 0:
                        for i in range(len(accounts_for_client)):
                            if accounts_for_client[i][0] == account_id:
                                sql_balance_check_query = "select account_balance from accounts where account_id = %s"
                                cursor_check = connection.cursor()
                                cursor_check.execute(sql_balance_check_query, [account_id])
                                balance_info = cursor_check.fetchone()[0]
                                if float(balance_info) - withdraw_amount >= 0:
                                    sql_post_query = "update accounts set account_balance = %s where account_id = %s returning *"
                                    cursor_post = connection.cursor()
                                    cursor_post.execute(sql_post_query, (float(balance_info) - withdraw_amount, account_id))
                                    returned_info = cursor_post.fetchone()
                                    connection.commit()
                                    account_details = AccountData(*returned_info)
                                    return account_details
                                raise InadequateFunds("You do not have enough funds in the given account to complete the transaction.")
                        raise AccountIDNotFound("There are no accounts associated with that ID.")
                    raise NoAccounts(
                        "There are no accounts associated with that client.")  # this might be redundant due to the try/except block
                except TypeError:
                    raise NoAccounts("There are no accounts associated with that client.")
            raise ClientIDNotFound("Client ID does not exist.")  # this might be redundant due to the try/except block
        except TypeError:
            raise ClientIDNotFound("Client ID does not exist.")

    def deposit_into_account(self, client_id: str, account_id: str, deposit_amount: float) -> AccountData:
        sql_get_clients_query = "select client_id from clients where client_id = %s"
        cursor_get_clients = connection.cursor()
        cursor_get_clients.execute(sql_get_clients_query, [client_id])
        clients_in_db = cursor_get_clients.fetchone()
        try:
            if len(clients_in_db) > 0:
                sql_get_accounts_query = "select account_id from accounts where client_id = %s"
                cursor_get_accounts = connection.cursor()
                cursor_get_accounts.execute(sql_get_accounts_query, [client_id])
                accounts_for_client = cursor_get_accounts.fetchall()
                try:
                    if len(accounts_for_client) > 0:
                        for i in range(len(accounts_for_client)):
                            if accounts_for_client[i][0] == account_id:
                                sql_balance_check_query = "select account_balance from accounts where account_id = %s"
                                cursor_check = connection.cursor()
                                cursor_check.execute(sql_balance_check_query, [account_id])
                                balance_info = cursor_check.fetchone()[0]
                                sql_post_query = "update accounts set account_balance = %s where account_id = %s returning *"
                                cursor_post = connection.cursor()
                                cursor_post.execute(sql_post_query, (float(balance_info) + deposit_amount, account_id))
                                returned_info = cursor_post.fetchone()
                                connection.commit()
                                account_details = AccountData(*returned_info)
                                return account_details
                        raise AccountIDNotFound("There are no accounts associated with that ID.")
                    raise NoAccounts("There are no accounts associated with that client.")  # this might be redundant due to the try/except block
                except TypeError:
                    raise NoAccounts("There are no accounts associated with that client.")
            raise ClientIDNotFound("Client ID does not exist.")  # this might be redundant due to the try/except block
        except TypeError:
            raise ClientIDNotFound("Client ID does not exist.")

    def delete_account(self, client_id: str, account_id: str) -> bool:
        sql_get_clients_query = "select client_id from clients where client_id = %s"
        cursor_get_clients = connection.cursor()
        cursor_get_clients.execute(sql_get_clients_query, [client_id])
        clients_in_db = cursor_get_clients.fetchone()
        try:
            if len(clients_in_db) > 0:
                sql_get_accounts_query = "select * from accounts where client_id = %s"
                cursor_get_accounts = connection.cursor()
                cursor_get_accounts.execute(sql_get_accounts_query, [client_id])
                accounts_for_client = cursor_get_accounts.fetchall()
                try:
                    if len(accounts_for_client) > 0:
                        for i in range(len(accounts_for_client)):
                            if accounts_for_client[i][1] == account_id:
                                if accounts_for_client[i][2] <= 0:
                                    sql_delete_query = "delete from accounts where account_id = %s"
                                    delete_cursor = connection.cursor()
                                    delete_cursor.execute(sql_delete_query, [account_id])
                                    connection.commit()
                                    if delete_cursor.rowcount > 0:
                                        return True
                                raise FundsStillExist(
                                    "There are still funds in that account. Please withdraw or transfer the balance before attempting to close the account.")
                        raise AccountIDNotFound("There are no accounts associated with that ID.")
                    raise NoAccounts(
                        "There are no accounts associated with that client.")  # this might be redundant due to the try/except block
                except TypeError:
                    raise NoAccounts("There are no accounts associated with that client.")
            raise ClientIDNotFound("Client ID does not exist.")  # this might be redundant due to the try/except block
        except TypeError:
            raise ClientIDNotFound("Client ID does not exist.")