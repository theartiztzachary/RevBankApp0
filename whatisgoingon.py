## Unit testing the unit tests :)
from utilities.connection_manager import connection

from data_access_layer.client_data_implementation import ClientDataImplementation
from entities.client_data import ClientData
from entities.account_data import AccountData

withdraw_amount: float = 45

sql_balance_check_query = "select account_balance from accounts where account_id = 'sv21'"
cursor_check = connection.cursor()
cursor_check.execute(sql_balance_check_query)
balance_info = cursor_check.fetchone()[0]
if balance_info - withdraw_amount >= 0:
    sql_post_query = "update accounts set account_balance = %s where account_id = 'sv21' returning *"
    cursor_post = connection.cursor()
    cursor_post.execute(sql_post_query, [balance_info - withdraw_amount])
    returned_info = cursor_post.fetchone()
    connection.commit()
    account_details = AccountData(*returned_info)
    print(account_details)
else:
    print("nay")