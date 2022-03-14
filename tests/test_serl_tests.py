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

#Validate creating a new client with good data. We are checking to make sure valid data passes through correctly, so if we get the
#MagicMock return value, it passed through correctly.
def test_service_create_client():
    client_test_service_imp.data_imp.create_new_client = MagicMock(return_value=[ClientData("Flash", "Wilmer", "fw7")])
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
    account_test_service_imp.data_imp.create_new_account = MagicMock(return_value=[AccountData("lv3", "lv34", 350)])
    new_account = account_test_service_imp.create_new_account("lv3", 350)
    assert new_account.account_id == "lv34"

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

#Validate viewing account with good data.
def test_service_view_account_information():
    pass

#Validate viewing account with bad data.
def test_service_view_account_balance_incorrect_inputs():
    pass

#Validate getting all account data for a client with good data.
def test_service_get_accounts_from_user():
    pass

#Validate getting all accounts from user with bad data.
def test_service_get_accounts_from_user_incorrect_inputs():
    pass

#Validate withdrawing from an account with good data.
def test_service_withdraw_from_account():
    pass

#Validate withdrawing from an account with bad data.
def test_service_withdraw_from_account_incorrect_inputs():
    pass

#Validate depositing into an account with good data.
def test_service_deposit_into_account():
    pass

#Validate depositing into an account with bad data.
def test_service_deposit_into_account_incorrect_inputs():
    pass

#Validate transferring between accounts with good data.
def test_service_transfer_between_accounts():
    pass

#Validate transferring between accounts with bad data.
def test_service_transfer_between_accoutns_incorrect_inputs():
    pass

#Validate deleting account with good data.
def test_service_delete_account():
    pass

#Validate deleting account with bad data.
def test_service_delete_account_incorrect_inputs():
    pass

#Validate deleting a client with good data.
def test_service_delete_client():
    pass

#Validate deleting a client with bad data.
def test_service_delete_client_incorrect_inputs():
    pass