from data_access_layer.client_data_implementation import ClientDataImplementation
from data_access_layer.account_data_implementation import AccountDataImplementation

from utilities.custom_exceptions import ClientIDNotFound, AccountIDNotFound, NoAccounts, InadequateFunds, FundsStillExist, AccountsStillExist

client_test_data_imp = ClientDataImplementation()
account_test_data_imp = AccountDataImplementation()

## These tests assume that the data has successfully passed through the service (validation) layer. ##
## Run dalTestScript in DBeaver before running these tests. ##

client_test_data_imp.client_id_value = 7 #This brings the client_id_value up to where it would be with the hard-added data.
account_test_data_imp.account_id_value = 5 #This brings the account_id_value up to where it would be with the hard-added data.

#Create a new client and add to database.
def test_create_new_client():
    added_client = client_test_data_imp.create_new_client("Estaire", "VonTelan")
    assert added_client.client_id == "ev7"

#Create a new account and add to database.
def test_create_new_account():
    added_account = account_test_data_imp.create_new_account("mn1", 200)
    assert added_account.account_id == "mn15"

#Attempt to create a new account with a client that does not exist.
def test_create_new_account_with_nonexistant_client():
    try:
        bad_account = account_test_data_imp.create_new_account("nonexistant", 10)
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#Retrive specific account information.
def test_view_account_information():
    viewing_account = account_test_data_imp.view_account_information("zh4", "zh3")
    assert viewing_account.account_balance == 50

#Attempt to view specific account information of an account that does not exist.
def test_view_account_with_nonexistant_account():
    try:
        bad_account = account_test_data_imp.view_account_information("sv2", "sv1313")
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to view the information of a theoretical account from a client that does not exist.
def test_view_account_with_nonexistant_client():
    try:
        no_client = account_test_data_imp.view_account_information("nope", "sv21")
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#View all account information.
def test_view_all_accounts():
    returned_client = client_test_data_imp.view_all_client_accounts("sv2")
    assert returned_client.client_accounts["sv21"] == 50
    assert returned_client.client_accounts["sv22"] == 100

#Attempt to view all account information from a client that does not exist.
def test_view_accounts_with_nonexistant_client():
    try:
        bad_return = client_test_data_imp.view_all_client_accounts("zw3587")
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#Attempt to view account information from an existing client that does not have any accounts.
def test_view_accounts_with_existing_client_no_accounts():
    try:
        no_accounts = client_test_data_imp.view_all_client_accounts("lv3")
        assert False
    except NoAccounts as exception:
        assert str(exception) == "There are no accounts associated with that client."

#Withdraw from a specific account.
def test_withdraw_from_account():
    returned_account = account_test_data_imp.withdraw_from_account("sv2", "sv21", 5)
    assert returned_account.account_balance == 45

#Attempt to withdraw from an account that does not exist.
def test_withdraw_from_nonexistant_account():
    try:
        bad_account = account_test_data_imp.withdraw_from_account("sv2", "zw12346", 10)
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to withdraw from a theoretical account from a nonexistant client.
def test_withdraw_from_nonexistant_client():
    try:
        no_client = account_test_data_imp.withdraw_from_account("tehe", "sv22", 10)
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#Attempt to withdraw from an account that does not have enough funds.
def test_withdraw_not_enough_funds():
    try:
        poor_lad = account_test_data_imp.withdraw_from_account("zh4", "zh43", 100)
        assert False
    except InadequateFunds as exception:
        assert str(exception) == "You do not have enough funds in the given account to complete the transaction."

#Deposit into a specific account.
def test_deposit_into_account():
    returned_account = account_test_data_imp.deposit_into_account("zh4", "zh43", 20)
    assert returned_account.account_balance == 70

#Attempt to deposit into an account that does not exist.
def test_deposit_into_nonexistant_account():
    try:
        no_account = account_test_data_imp.deposit_into_account("sv2", "zq12346", 10)
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to deposit into a theoretical account with a nonexistant client.
def test_deposit_into_nonexistant_client():
    try:
        no_client = account_test_data_imp.deposit_into_account("no client for u", "sv22", 70)
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#Transfer money between two accounts.
def test_transfer_money_between_accounts():
    transfer_complete = client_test_data_imp.transfer_between_accounts("sv2", "sv21", "sv22", 5)
    assert transfer_complete.client_accounts["sv22"] == 105

#Attempt to transfer from an account that does not exist.
def test_transfer_from_nonexistant_account():
    try:
        no_account = client_test_data_imp.transfer_between_accounts("sv2", "this account doesn't exist", "sv22", 5)
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to transfer from a theoretical account from a nonexistant client.
def test_transfer_from_nonexistant_client():
    try:
        no_client = client_test_data_imp.transfer_between_accounts("tehe", "sv21", "sv22", 5)
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist."

#Attempt to transfer from an account that does not have enough funds.
def test_transfer_from_no_funds_account():
    try:
        no_money = client_test_data_imp.transfer_between_accounts("sv2", "sv21", "sv22", 1000000)
        assert False
    except InadequateFunds as exception:
        assert str(exception) == "You do not have enough funds in the given account to complete the transaction."

#Attempt to transfer to an account that does not exist.
def test_transfer_to_nonexistant_account():
    try:
        no_account = client_test_data_imp.transfer_between_accounts("sv2", "sv21", "this account does not exist", 1)
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Close an account.
def test_close_individual_account():
    account_closed = account_test_data_imp.delete_account("hb6", "hb64")
    assert account_closed == True

#Attempt to close an account that has funds in it.
def test_close_nonexistant_account():
    try:
        account_closed = account_test_data_imp.delete_account("at7", "at75")
        assert False
    except AccountIDNotFound as exception:
        assert str(exception) == "There are no accounts associated with that ID."

#Attempt to close a theoretical bank account from a nonexistant client.
def test_close_individual_account_with_funds():
    try:
        cannot_close = account_test_data_imp.delete_account("zh4", "zh43")
        assert False
    except FundsStillExist as exception:
        assert str(exception) == "There are still funds in that account. Please withdraw or transfer the balance before attempting to close the account."

#End client relationship.
def test_remove_client():
    goodbye_client = client_test_data_imp.delete_client("id5")
    assert goodbye_client == True

#Attempt to end client relationship while client still has accounts.
def test_remove_client_with_accounts():
    try:
        still_accounted = client_test_data_imp.delete_client("zh4")
        assert False
    except AccountsStillExist as exception:
        assert str(exception) == "There are still accounts associated with that client. Please close all accounts before removing the client."

#Attempt to end a client relationship that does not exist.
def test_remove_nonexistant_client():
    try:
        never_existed = client_test_data_imp.delete_client("i was never part of this to begin with")
        assert False
    except ClientIDNotFound as exception:
        assert str(exception) == "Client ID does not exist"