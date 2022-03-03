from data_access_layer.client_implementation import ClientDataImplementation
from service_layer.client_service_implementation import ClientServiceImplementation
from data_access_layer.account_implementation import AccountDataImplementation
from service_layer.account_service_implementation import AccountServiceImplementation

from custom_exceptions.invalid_data_type import InvalidDataType

client_dal_imp = ClientDataImplementation()
client_serl_imp = ClientServiceImplementation(client_dal_imp)
account_dal_imp = AccountDataImplementation()
account_serl_imp = AccountServiceImplementation(account_dal_imp)

##The tests here check if the user input is of a valid type to use in queries - the actual check of the (valid) inputted data
#against the database is checked by the data access layer. These tests also prove that basic data passing is working by using
#data that should exist due to it currently being hard-coded into the data access client implementation.

##At some point need to add integer check into service layer. (what happens if you try int("not a number")?)

#Validate creating a new client with good data.
def test_service_create_client():
    new_client = client_serl_imp.create_new_client("Flash", "Wilmer")
    assert new_client == "fw5"

#Validtate creating a new client with bad data.
def test_service_create_client_incorrect_inputs():
    try:
        bad_client = client_serl_imp.create_new_client(70, "Wilmer")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_client = client_serl_imp.create_new_client(70.1, "Wilmer")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_client = client_serl_imp.create_new_client(True, "Wilmer")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_client = client_serl_imp.create_new_client("Flash", 70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_client = client_serl_imp.create_new_client("Flash", 70.1)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_client = client_serl_imp.create_new_client("Flash", False)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

#Validate creating a new account with good data.
def test_service_create_account():
    new_account = account_serl_imp.create_new_account("lv3", 350)
    assert new_account == "lv34"

    account_balance = account_serl_imp.view_account_balance("lv3", new_account)
    assert account_balance == 350

#Validate creating a new account with bad data.
def test_service_create_account_incorrect_inputs():
    try:
        bad_account = account_serl_imp.create_new_account(70, 70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_account = account_serl_imp.create_new_account(70.1, 70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_account = account_serl_imp.create_new_account(True, 70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_account = account_serl_imp.create_new_account("lv3", "this is not a number lol")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_account = account_serl_imp.create_new_account("lv3", False)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

#Validate viewing account with good data.
def test_service_view_account_balance():
    viewed_balance = account_serl_imp.view_account_balance("zh4", "zh43")
    assert viewed_balance == 50

#Validate viewing account with bad data.
def test_service_view_account_balance_incorrect_inputs():
    try:
        bad_account = account_serl_imp.view_account_balance(70, "zh43")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_account = account_serl_imp.view_account_balance(70.1, "zh43")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_account = account_serl_imp.view_account_balance(True, "zh43")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_account = account_serl_imp.view_account_balance("zh4", 70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_account = account_serl_imp.view_account_balance("zh4", 70.1)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_account = account_serl_imp.view_account_balance("zh4", False)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

#Validate getting all accounts from user with good data.
def test_service_get_accounts_from_user():
    viewed_accounts = client_serl_imp.get_all_accounts_by_id("sv2")
    assert viewed_accounts == "Account: sv21, Balance: 50 // Account: sv22, Balance: 100 // "

#Validate getting all accounts from user with bad data.
def test_service_get_accounts_from_user_incorrect_inputs():
    try:
        bad_client = client_serl_imp.get_all_accounts_by_id(70)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_client = client_serl_imp.get_all_accounts_by_id(70.1)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_client = client_serl_imp.get_all_accounts_by_id(True)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

#Validate withdrawing from an account with good data.
def test_service_withdraw_from_account():
    remaining_total = account_serl_imp.withdraw_from_account("zh4", "zh43", 5)
    assert remaining_total == 45

#Validate withdrawing from an account with bad data.
def test_service_withdraw_from_account_incorrect_inputs():
    try:
        bad_total = account_serl_imp.withdraw_from_account(70, "zh43", 5)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_total = account_serl_imp.withdraw_from_account(70.1, "zh43", 5)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_total = account_serl_imp.withdraw_from_account(False, "zh43", 5)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_total = account_serl_imp.withdraw_from_account("zh4", 70, 5)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_total = account_serl_imp.withdraw_from_account("zh4", 70.1, 5)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_total = account_serl_imp.withdraw_from_account("zh4", True, 5)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_total = account_serl_imp.withdraw_from_account("zh4", "zh43", "this isn't a number")
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

    try:
        bad_total = account_serl_imp.withdraw_from_account("zh4", "zh43", False)
        assert False
    except InvalidDataType as exception:
        assert str(exception) == "That is not a valid input type. Please double check your input."

#Validate depositing into an account with good data.
def test_service_deposit_into_account():
    new_total = account_serl_imp.deposit_into_account("sv2", "sv21", 5)
    assert new_total == 55

#Validate depositing into an account with bad data.
def test_service_deposit_into_account_incorrect_inputs():
    pass