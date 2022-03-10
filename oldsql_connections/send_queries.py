
# def get_single_client_record(client_id: str) -> ClientData:
#     sql_query_client = "select * from clients where client_id = %s"
#     cursor_client = connection.cursor()
#     cursor_client.execute(sql_query_client, [client_id])
#     client_record = cursor_client.fetchone()
#     client = ClientData(*client_record)
#
#     sql_query_accounts = "select * from accounts where client_id = %s"
#     cursor_account = connection.cursor()
#     cursor_account.execute(sql_query_accounts, [client_id])
#     account_record = cursor_account.fetchall()
#     for record in account_record:
#         client.client_accounts.append(record)
#
#     return client
#
# def get_single_account_record(client_id: str, account_id: str) -> AccountData:
#     pass
#
# def withdraw_from_an_account(client_id: str, account_id: str, withdraw_amount: float) -> bool:
#     pass
#
# def deposit_into_an_account(client_id: str, account_id: str, deposit_amount: float) -> bool:
#     pass
#
# def transfer_between_accounts(client_id: str, account_trans_from: str, account_trans_to: str, transfer_amount: str) -> bool:
#     pass
#
# def delete_account(client_id: str, account_id: str) -> bool:
#     pass
#
# def delete_client(client_id: str) -> bool:
#     pass

