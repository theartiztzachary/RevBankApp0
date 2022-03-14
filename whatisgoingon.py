## Unit testing the unit tests :)
from utilities.connection_manager import connection

from data_access_layer.client_data_implementation import ClientDataImplementation
from entities.client_data import ClientData
from entities.account_data import AccountData

from utilities.custom_exceptions import FundsStillExist, AccountIDNotFound, NoAccounts, ClientIDNotFound

def whats_goin_on():
    client_id = "hb6"
    account_id = "hb64"

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
                        print(accounts_for_client[i][1])
                        if accounts_for_client[i][1] == account_id:
                            print(accounts_for_client[i][2])
                            if accounts_for_client[i][2] <= 0:
                                sql_delete_query = "delete from accounts where account_id = %s"
                                delete_cursor = connection.cursor()
                                delete_cursor.execute(sql_delete_query, [account_id])
                                connection.commit()
                                if delete_cursor.rowcount > 0:
                                    return True
                            raise FundsStillExist("There are still funds in that account. Please withdraw or transfer the balance before attempting to close the account.")
                    raise AccountIDNotFound("There are no accounts associated with that ID.")
                raise NoAccounts("There are no accounts associated with that client.")  # this might be redundant due to the try/except block
            except TypeError:
                raise NoAccounts("There are no accounts associated with that client.")
        raise ClientIDNotFound("Client ID does not exist.")  # this might be redundant due to the try/except block
    except TypeError:
        raise ClientIDNotFound("Client ID does not exist.")

print(whats_goin_on())