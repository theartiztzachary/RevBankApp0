from flask import Flask

from entities.client_data_object import ClientData
from data_access_layer.client_implementation import ClientDataImplementation
from service_layer.client_service_implementation import ClientServiceImplementation
from entities.account_data_object import AccountData
from data_access_layer.account_implementation import AccountDataImplementation
from service_layer.account_service_implementation import AccountServiceImplementation

app: Flask = Flask(__name__)

app_client_data_imp = ClientDataImplementation()
app_client_service_imp = ClientServiceImplementation(app_client_data_imp)
app_account_data_imp = AccountDataImplementation()
app_account_service_imp = AccountServiceImplementation(app_account_data_imp)

#Hello world test to ensure the app is running and the base HTTPS path has been configured correctly.
@app.route("/greeting", methods=["GET"])
def hello_world():
   return "Hello world!"

#Create a new client.

#Create a new account.

#View account balance.

#View all of a client's accounts.

#Withdraw from an account.

#Deposit into an account.

#Transfer money between two accounts.

#Delete an account.

#Remove a client.

app.run()