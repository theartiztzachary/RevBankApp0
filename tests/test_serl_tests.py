from unittest.mock import MagicMock

from data_access_layer.client_data_implementation import ClientDataImplementation
from service_layer.client_service_implementation import ClientServiceImplementation
from data_access_layer.account_data_implementation import AccountDataImplementation
from service_layer.account_service_implementation import AccountServiceImplementation

client_test_data_imp = ClientDataImplementation()
client_test_service_imp = ClientServiceImplementation(client_test_data_imp)
account_test_data_imp = AccountDataImplementation()
account_test_service_imp = AccountServiceImplementation(account_test_data_imp)

## These tests check if the USER input is of a valid type to use in queries. Theoretically, 95% of these should be caught by the API
# layer, as it would be crafting 