from service_layer.client_service_implementation import ClientServiceImplementation
from service_layer.account_service_implementation import AccountServiceImplementation

from custom_exceptions.invalid_data_type import InvalidDataType

client_serl_imp = ClientServiceImplementation()
account_serl_imp = AccountServiceImplementation()

test_client = client_serl_imp.create_new_client("Aesteri", "Telyn")

def test_service_create_client():
    new_client = client_serl_imp.create_new_client("Flash", "Wilmer")

    assert new_client == "fw6"

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

def test_service_create_account():
    new_account = account_serl_imp.create_new_account()