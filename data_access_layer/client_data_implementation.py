from entities.client_interface import ClientInterface
from entities.client_data import ClientData
from utilities.connection_manager import connection

from utilities.custom_exceptions import ClientIDNotFound, NoAccounts, InadequateFunds, AccountIDNotFound, AccountsStillExist

## A lot of this logic is bloated with extra checks. Once everything is baseline in place and working, will go back and try to reduce
# the bloat if there is time.

class ClientDataImplementation(ClientInterface):
    client_id_value = 1

    def create_new_client(self, first_name: str, last_name: str) -> ClientData:
        temp_first = first_name.lower()
        temp_last = last_name.lower()
        client_id = f"{temp_first[0]}{temp_last[0]}{self.client_id_value}"
        ClientDataImplementation.client_id_value += 1
        sql_query = "insert into clients values(%s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql_query, (first_name, last_name, client_id))
        connection.commit()
        new_client = ClientData(first_name, last_name, client_id)
        return new_client

    def view_all_client_accounts(self, client_id: str) -> ClientData:
        sql_client_query = "select * from clients where client_id = %s"
        cursor_client = connection.cursor()
        cursor_client.execute(sql_client_query, [client_id])
        client_info = cursor_client.fetchone()
        try:
            if len(client_info) > 0:
                returning_client = ClientData(*client_info)
                sql_accounts_query = "select * from accounts where client_id = %s"
                cursor_accounts = connection.cursor()
                cursor_accounts.execute(sql_accounts_query, [client_id])
                account_info = cursor_accounts.fetchall()
                try:
                    if len(account_info) > 0:
                        for i in range(len(account_info)):
                            returning_client.client_accounts[account_info[i][1]] = account_info[i][2]
                        return returning_client
                    raise NoAccounts("There are no accounts associated with that client.") #this is...not redudant I guess haha
                except TypeError:
                    raise NoAccounts("There are no accounts associated with that client.")
        except TypeError:
            raise ClientIDNotFound("Client ID does not exist.")

    #See if there's a way to checkpoint this transaction so it doesn't do one and then the other, but both simultaneously.
    def transfer_between_accounts(self, client_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> ClientData:
        sql_client_query = "select * from clients where client_id = %s"
        cursor_client = connection.cursor()
        cursor_client.execute(sql_client_query, [client_id])
        client_info = cursor_client.fetchone()
        try:
            if len(client_info) > 0:
                returning_client = ClientData(*client_info)
                sql_accounts_query = "select * from accounts where client_id = %s"
                cursor_accounts = connection.cursor()
                cursor_accounts.execute(sql_accounts_query, [client_id])
                account_info = cursor_accounts.fetchall()
                try:
                    if len(account_info) > 0:
                        from_account_balance: float
                        have_from_account = False
                        to_account_balance: float
                        have_to_account = False
                        for i in range(len(account_info)):
                            if account_info[i][1] == account_from_id:
                                from_account_balance = account_info[i][2]
                                have_from_account = True
                                if float(account_info[i][2]) - transfer_amount < 0:
                                    raise InadequateFunds("You do not have enough funds in the given account to complete the transaction.")
                            elif account_info[i][1] == account_to_id:
                                to_account_balance = account_info[i][2]
                                have_to_account = True
                        if have_from_account and have_to_account:
                            if float(from_account_balance) - transfer_amount > 0:
                                sql_transfer_query_from = "update accounts set account_balance = %s where account_id = %s returning account_balance"
                                cursor_transfer_from = connection.cursor()
                                cursor_transfer_from.execute(sql_transfer_query_from, (float(from_account_balance) - transfer_amount, account_from_id))
                                account_from_balance_end = cursor_transfer_from.fetchone()[0]
                                connection.commit()
                                sql_transfer_query_to = "update accounts set account_balance = %s where account_id = %s returning account_balance"
                                cursor_transfer_to = connection.cursor()
                                cursor_transfer_to.execute(sql_transfer_query_to, (float(to_account_balance) + transfer_amount, account_to_id))
                                account_to_balance_end = cursor_transfer_to.fetchone()[0]
                                connection.commit()
                                returning_client.client_accounts[account_from_id] = account_from_balance_end
                                returning_client.client_accounts[account_to_id] = account_to_balance_end
                                return returning_client #at the moment, this ClientData object only has the accounts that were modified. It's probably fine, but should be noted.
                            raise InadequateFunds("You do not have enough funds in the given account to complete the transaction.")
                        raise AccountIDNotFound("There are no accounts associated with that ID.")
                except TypeError:
                    raise NoAccounts("There are no accounts associated with that client.")
        except TypeError:
            raise ClientIDNotFound("Client ID does not exist.")

    def delete_client(self, client_id: str) -> bool:
        sql_client_query = "select client_id from clients where client_id = %s"
        cursor_client = connection.cursor()
        cursor_client.execute(sql_client_query, [client_id])
        client_info = cursor_client.fetchone()
        try:
            if len(client_info) > 0:
                sql_accounts_query = "select account_id from accounts where client_id = %s"
                cursor_accounts = connection.cursor()
                cursor_accounts.execute(sql_accounts_query, [client_id])
                account_info = cursor_accounts.fetchone()
                try:
                    account_count = len(account_info)
                    raise AccountsStillExist("There are still accounts associated with that client. Please close all accounts before removing the client.")
                except TypeError:
                    sql_delete_query = "delete from clients where client_id = %s"
                    cursor_delete = connection.cursor()
                    cursor_delete.execute(sql_delete_query, [client_id])
                    connection.commit()
                    if cursor_delete.rowcount > 0:
                        return True
            raise ClientIDNotFound("Client ID does not exist.")
        except TypeError:
            raise ClientIDNotFound("Client ID does not exist.")