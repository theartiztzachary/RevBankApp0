from unittest.mock import MagicMock

from entities.client_data import ClientData
from data_access_layer.client_data_implementation import ClientDataImplementation
from service_layer.client_service_implementation import ClientServiceImplementation
from entities.account_data import AccountData
from data_access_layer.account_data_implementation import AccountDataImplementation
from service_layer.account_service_implementation import AccountServiceImplementation

from utilities.custom_exceptions import InvalidDataType

client_test_data_imp = ClientDataImplementation()
client_test_service_imp = ClientServiceImplementation(client_test_data_imp)
account_test_data_imp = AccountDataImplementation()
account_test_service_imp = AccountServiceImplementation(account_test_data_imp)

## These tests check if the USER input is of a valid type to use in queries.

#Every positive test needs to be mocked so it doesn't actually touch the data access layer.

#Should there be tests for ensuring that the numbers inputted are positive, since our code only works with positive numbers?

#Validate creating a new client with good data. We are checking to make sure valid data passes through correctly, so if we get the
#MagicMock return value, it passed through correctly.
def test_service_create_client():
    client_test_service_imp.data_imp.create_new_client = MagicMock(return_value=ClientData("Flash", "Wilmer", "fw7"))
    new_client = client_test_service_imp.create_new_client("Flash", "Wilmer")
    assert new_client.client_id == "fw7"

#Validate creating a new client with bad data.
def test_service_create_client_bad_first_name():
    try:
        bad_client = client_test_service_imp.create_new_client(70, "Wilmer")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Entered first name is not a valid data type. Please double check your input."

    try:
        bad_client = client_test_service_imp.create_new_client(True, "Wilmer")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Entered first name is not a valid data type. Please double check your input."

def test_service_create_client_bad_last_name():
    try:
        bad_client = client_test_service_imp.create_new_client("Flash", 70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Entered last name is not a valid data type. Please double check your input."

    try:
        bad_client = client_test_service_imp.create_new_client("Flash", False)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Entered last name is not a valid data type. Please double check your input."

#Validate creating a new account with good data.
def test_service_create_account():
    account_test_service_imp.data_imp.create_new_account = MagicMock(return_value=AccountData("lv3", "lv34", 350))
    new_account = account_test_service_imp.create_new_account("lv3", 350)
    assert new_account.account_id == "lv34"

    new_account_2 = account_test_service_imp.create_new_account("lv3", "350")
    assert new_account_2.account_id == "lv34"

#Validate creating a new account with bad data.
def test_service_create_account_bad_client_id():
    try:
        bad_account = account_test_service_imp.create_new_account(70, 70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

    try:
        bad_account = account_test_service_imp.create_new_account(True, 70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

def test_service_create_account_bad_balance():
    try:
        bad_balance = account_test_service_imp.create_new_account("fw7", "non_numeric string")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Inputted account balance is not a valid data type. Please double check your input."

    try:
        bad_balance = account_test_service_imp.create_new_account("fw7", True)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Inputted account balance is not a valid data type. Please double check your input."

#Validate viewing account with good data.
def test_service_view_account_information():
    account_test_service_imp.data_imp.view_account_information = MagicMock(return_value=AccountData("fw7", "fw75", 450))
    viewed_account = account_test_service_imp.view_account_information("fw7", "fw75")
    assert viewed_account.account_balance == 450

#Validate viewing account with bad data.
def test_service_view_account_info_bad_client_id():
    try:
        bad_account = account_test_service_imp.view_account_information(70, "fw75")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

    try:
        bad_account = account_test_service_imp.view_account_information(False, "fw75")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

def test_service_view_account_info_bad_account_id():
    try:
        bad_account = account_test_service_imp.view_account_information("fw7", 70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

    try:
        bad_account = account_test_service_imp.view_account_information("fw7", True)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

#Validate getting all account data for a client with good data.
def test_service_get_accounts_from_user():
    mocked_client = ClientData("Flash", "Wilmer", "fw7")
    mocked_client.client_accounts = {"fw75": 450, "fw76": 250}
    client_test_service_imp.data_imp.view_all_client_accounts = MagicMock(return_value=mocked_client)
    viewed_accounts = client_test_service_imp.view_all_client_accounts("fw7")
    assert viewed_accounts.client_accounts["fw75"] == 450
    assert viewed_accounts.client_accounts["fw76"] == 250

#Validate getting all accounts from user with bad data.
def test_service_get_accounts_from_user_bad_client_id():
    try:
        bad_client = client_test_service_imp.view_all_client_accounts(70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

    try:
        bad_client = client_test_service_imp.view_all_client_accounts(True)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

#Validate withdrawing from an account with good data.
def test_service_withdraw_from_account():
    account_test_service_imp.data_imp.withdraw_from_account = MagicMock(return_value=AccountData("fw7", "fw75", 400))
    returned_account = account_test_service_imp.withdraw_from_account("fw7", "fw75", 50)
    assert returned_account.account_balance == 400

    returned_account_2 = account_test_service_imp.withdraw_from_account("fw7", "fw75", "50")
    assert returned_account_2.account_balance == 400

#Validate withdrawing from an account with bad data.
def test_service_withdraw_from_account_bad_client_id():
    try:
        bad_client = account_test_service_imp.withdraw_from_account(70, "fw75", 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

    try:
        bad_client = account_test_service_imp.withdraw_from_account(True, "fw75", 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

def test_service_withdraw_from_account_bad_account_id():
    try:
        bad_account = account_test_service_imp.withdraw_from_account("fw7", 70, 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

    try:
        bad_account = account_test_service_imp.withdraw_from_account("fw7", False, 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

def test_service_withdraw_from_account_bad_withdraw_amount():
    try:
        bad_withdraw = account_test_service_imp.withdraw_from_account("fw7", "fw75", "non-numeric string")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Withdraw amount is not a valid data type. Please double check your input."

    try:
        bad_withdraw = account_test_service_imp.withdraw_from_account("fw7", "fw75", True)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Withdraw amount is not a valid data type. Please double check your input."

#Validate depositing into an account with good data.
def test_service_deposit_into_account():
    account_test_service_imp.data_imp.deposit_into_account = MagicMock(return_value=AccountData("fw7", "fw75", 500))
    returned_account = account_test_service_imp.deposit_into_account("fw7", "fw75", 50)
    assert returned_account.account_balance == 500

    returned_account_2 = account_test_service_imp.deposit_into_account("fw7", "fw75", "50")
    assert returned_account_2.account_balance == 500

#Validate depositing into an account with bad data.
def test_service_deposit_into_account_bad_client_id():
    try:
        bad_client = account_test_service_imp.deposit_into_account(70, "fw75", 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

    try:
        bad_client = account_test_service_imp.deposit_into_account(True, "fw75", 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

def test_service_deposit_into_account_bad_account_id():
    try:
        bad_account = account_test_service_imp.deposit_into_account("fw7", 70, 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

    try:
        bad_account = account_test_service_imp.deposit_into_account("fw7", False, 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

def test_service_deposit_into_account_bad_deposit_amount():
    try:
        bad_deposit = account_test_service_imp.deposit_into_account("fw7", "fw75", "non-numeric string")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Deposit amount is not a valid data type. Please double check your input."

    try:
        bad_deposit = account_test_service_imp.deposit_into_account("fw7", "fw75", True)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Deposit amount is not a valid data type. Please double check your input."

#Validate transferring between accounts with good data.
def test_service_transfer_between_accounts():
    mocked_client = ClientData("Flash", "Wilmer", "fw7")
    mocked_client.client_accounts = {"fw75": 300, "fw76": 350}
    client_test_service_imp.data_imp.transfer_between_accounts = MagicMock(return_value=mocked_client)
    returned_client = client_test_service_imp.transfer_between_accounts("fw7", "fw75", "fw76", 50)
    assert returned_client.client_accounts["fw75"] == 300
    assert returned_client.client_accounts["fw76"] == 350

    returned_client_2 = client_test_service_imp.transfer_between_accounts("fw7", "fw75", "fw76", "50")
    assert returned_client_2.client_accounts["fw75"] == 300
    assert returned_client_2.client_accounts["fw76"] == 350

#Validate transferring between accounts with bad data.
def test_service_transfer_between_accounts_bad_client_id():
    try:
        bad_client = client_test_service_imp.transfer_between_accounts(70, "fw75", "fw76", 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

    try:
        bad_client = client_test_service_imp.transfer_between_accounts(True, "fw75", "fw76", 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

def test_service_transfer_between_accounts_bad_account_ids():
    try:
        bad_account = client_test_service_imp.transfer_between_accounts("fw7", 70, "fw76", 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

    try:
        bad_account = client_test_service_imp.transfer_between_accounts("fw7", True, "fw76", 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

    try:
        bad_account = client_test_service_imp.transfer_between_accounts("fw7", "fw75", 70, 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

    try:
        bad_account = client_test_service_imp.transfer_between_accounts("fw7", "fw75", False, 50)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

def test_service_transfer_between_accounts_bad_transfer_amount():
    try:
        bad_transfer = client_test_service_imp.transfer_between_accounts("fw7", "fw75", "fw76", "non-numeric string")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Transfer amount is not a valid data type. Please double check your input."

    try:
        bad_transfer = client_test_service_imp.transfer_between_accounts("fw7", "fw75", "fw76", True)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Transfer amount is not a valid data type. Please double check your input."

#Validate deleting account with good data.
def test_service_delete_account():
    account_test_service_imp.data_imp.delete_account = MagicMock(return_value=True)
    delete_result = account_test_service_imp.delete_account("fw7", "fw75")
    assert delete_result == True

#Validate deleting account with bad data.
def test_service_delete_account_bad_client_id():
    try:
        bad_client = account_test_service_imp.delete_account(70, "fw75")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

    try:
        bad_client = account_test_service_imp.delete_account(False, "fw76")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

def test_service_delete_account_bad_account_id():
    try:
        bad_account = account_test_service_imp.delete_account("fw7", 70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

    try:
        bad_account = account_test_service_imp.delete_account("fw7", True)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Account ID is not a valid data type. Please double check your input."

#Validate deleting a client with good data.
def test_service_delete_client():
    client_test_service_imp.data_imp.delete_client = MagicMock(return_value=True)
    delete_result = client_test_service_imp.delete_client("fw7")
    assert delete_result == True

#Validate deleting a client with bad data.
def test_service_delete_client_bad_client_id():
    try:
        bad_client = client_test_service_imp.delete_client(70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."

    try:
        bad_client = client_test_service_imp.delete_client(False)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "Client ID is not a valid data type. Please double check your input."