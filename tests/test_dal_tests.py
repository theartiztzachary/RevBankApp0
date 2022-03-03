from data_access_layer.client_implementation import ClientDataImplementation
from entities.client_data_object import ClientData
from data_access_layer.account_implementation import AccountDataImplementation
from entities.account_data_object import AccountData

from custom_exceptions.client_id_not_found import ClientIDNotFound
from custom_exceptions.account_id_not_found import AccountIDNotFound
from custom_exceptions.inadequate_funds import InadequateFunds
from custom_exceptions.no_accounts import NoAccountsForClient

client_test_data_imp = ClientDataImplementation()
account_test_data_imp = AccountDataImplementation()

##THESE TESTS ASSUME THAT THE DATA HAS SUCCESSFULLY PASSED THROUGH THE SERVICE LAYER##

#Create a new client.
def test_create_a_new_client():
    estaire_client = ClientData("Estaire", "VonTelan")
    added_client = client_test_data_imp.create_new_client(estaire_client)

    assert added_client == "ev5"
    assert ClientDataImplementation.client_database[added_client] == estaire_client

#Create a new account with a client.
def test_create_a_new_account():
    mekio_account = AccountData(client_test_data_imp.mekio_client_id, 200)
    test_id = account_test_data_imp.create_new_account(mekio_account)

    assert test_id == "mn14"
    assert client_test_data_imp.client_database["mn1"].client_accounts["mn14"] == mekio_account

#Attempt to create a new account with a client that does not exist.
def test_create_new_account_with_nonexistant_client():
    try:
        bad_account = AccountData("nonexistant", 10)
        test_id = account_test_data_imp.create_new_account(bad_account)
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#View balance of a specific account.
def test_view_balance():
    test_balance = account_test_data_imp.view_account_balance(client_test_data_imp.salvador_client_id, client_test_data_imp.salvador_account_one_id)

    assert test_balance == 50

#Attempt to view the balance of an account that does not exist.
def test_view_balance_with_nonexistant_account():
    try:
        bad_balance = account_test_data_imp.view_account_balance(client_test_data_imp.salvador_client_id, "sv1313")
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to view the balance of a theoretical account from a client that does not exist.
def test_view_balance_with_nonexistant_client():
    try:
        not_client = account_test_data_imp.view_account_balance("nope", client_test_data_imp.salvador_account_two_id)
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#View balance of all accounts.
def test_view_balance_of_all_accounts():
    balance_return = client_test_data_imp.get_all_accounts_by_id(client_test_data_imp.salvador_client_id)

    assert balance_return == "Account: sv21, Balance: 50 // Account: sv22, Balance: 100 // "

#Attempt to view balance of all accounts from a client that does not exist.
def test_view_balance_of_all_accounts_with_nonexistant_client():
    try:
        bad_return = client_test_data_imp.get_all_accounts_by_id("zw1234")
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#Attempt to view balance of all accounts with an existing client that does not have any accounts.
def test_view_balance_of_all_accounts_existing_client_nonexistant_accounts():
    try:
        no_accounts = client_test_data_imp.get_all_accounts_by_id("lv3")
        assert False
    except NoAccountsForClient as exception:
        assert str(exception) == "There are no accounts associated with that client."

#Withdraw from a specific account.
def test_withdraw_from_account():
    current_balance = account_test_data_imp.withdraw_from_account(client_test_data_imp.salvador_client_id, client_test_data_imp.salvador_account_one_id, 5)

    assert current_balance == 45

#Attempt to withdraw from an account that does not exist.
def test_withdraw_from_nonexistant_account():
    try:
        bad_balance = account_test_data_imp.withdraw_from_account(client_test_data_imp.salvador_client_id, "zw12346", 10)
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to withdraw from a theoretical account from a nonexistant client.
def test_withdraw_from_nonexistant_client():
    try:
        no_client = account_test_data_imp.withdraw_from_account("tehe", client_test_data_imp.salvador_account_two_id, 10)
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#Attempt to withdraw from an account that does not have enough funds.
def test_withdraw_not_enough_funds():
    try:
        poor_lad = account_test_data_imp.withdraw_from_account(client_test_data_imp.zandel_client_id, client_test_data_imp.zandel_account_id, 100)
        assert False
    except InadequateFunds as exception:
        assert str(exception) == "You do not have enough funds in the given account to complete the transaction."

#Deposit to a specific account.
def test_deposit_into_account():
    current_balance = account_test_data_imp.deposit_into_account(client_test_data_imp.zandel_client_id, client_test_data_imp.zandel_account_id, 20)

    assert current_balance == 70

#Attempt to deposit into an account that does not exist.
def test_deposit_into_nonexistant_account():
    try:
        no_balance = account_test_data_imp.deposit_into_account(client_test_data_imp.salvador_client_id, "zw12346", 10)
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to deposit into a theoretical account with a nonexistant client.
def test_deposit_into_nonexistant_client():
    try:
        no_client = account_test_data_imp.deposit_into_account("no client for u", client_test_data_imp.salvador_account_two_id, 70)
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#Transfer money between two accounts.
def test_transfer_money_between_accounts():
    transfer_complete = client_test_data_imp.transfer_between_accounts(client_test_data_imp.salvador_client_id, client_test_data_imp.salvador_account_one_id, client_test_data_imp.salvador_account_two_id, 5)

    assert transfer_complete == True
    assert ClientDataImplementation.client_database[client_test_data_imp.salvador_client_id].client_accounts[client_test_data_imp.salvador_account_two_id].current_balance == 105

#Attempt to transfer from an account that does not exist.
def test_transfer_from_nonexistant_account():
    try:
        no_account = client_test_data_imp.transfer_between_accounts(client_test_data_imp.salvador_client_id, "this account dosen't exist", client_test_data_imp.salvador_account_two_id, 5)
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to transfer from a theoretical account from a nonexistant client.
def test_transfer_from_nonexistant_client():
    try:
        no_client = client_test_data_imp.transfer_between_accounts("tehe", client_test_data_imp.salvador_account_one_id, client_test_data_imp.salvador_account_two_id, 5)
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#Attempt to transfer from an account that does not have enough funds.
def test_transfer_from_no_funds_account():
    try:
        no_money = client_test_data_imp.transfer_between_accounts(client_test_data_imp.salvador_client_id, client_test_data_imp.salvador_account_one_id, client_test_data_imp.salvador_account_two_id, 100000)
        assert False
    except InadequateFunds as exception:
        assert str(exception) == "You do not have enough funds in the given account to complete the transaction."

#Attempt to transfer to an account that does not exist.
def test_transfer_to_nonexistant_account():
    try:
        no_account = client_test_data_imp.transfer_between_accounts(client_test_data_imp.salvador_client_id, client_test_data_imp.salvador_account_one_id, "this account does not exist", 1)
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#What happens if a valid client attempts to transfer between accounts that are not theirs?
#Curently returns an AccountIDNotFound error.

#Close bank account.
def test_close_individual_account():
    account_closed = account_test_data_imp.delete_account(client_test_data_imp.zandel_client_id, client_test_data_imp.zandel_account_id)
    assert account_closed == True
    try:
        no_account = account_test_data_imp.view_account_balance(client_test_data_imp.zandel_client_id, client_test_data_imp.zandel_account_id)
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to close a bank account that does not exist.
def test_close_nonexistant_account():
    try:
        no_account = account_test_data_imp.delete_account(client_test_data_imp.salvador_client_id, "this account doesn't exist")
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to close a theoretical bank account from a nonexistant client.
def test_close_nonexistant_client():
    try:
        no_client = account_test_data_imp.delete_account("nope", client_test_data_imp.salvador_account_two_id)
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#What happens if someone tries to close an account with funds still in it?

#End client relationship.
def test_remove_client():
    goodbye_client = client_test_data_imp.delete_client(client_test_data_imp.zandel_client_id)

    assert goodbye_client == True

#Attempt to end a client relationship that does not exist.
def test_remove_nonexistant_client():
    try:
        never_existed = client_test_data_imp.delete_client("i was never pat of this to begin with")
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#What happens if someone tries to end a client relationship with accounts still open?