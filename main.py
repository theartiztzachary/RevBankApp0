from flask import Flask, request, jsonify

from data_access_layer.client_implementation import ClientDataImplementation
from service_layer.client_service_implementation import ClientServiceImplementation
from data_access_layer.account_implementation import AccountDataImplementation
from service_layer.account_service_implementation import AccountServiceImplementation

from custom_exceptions.invalid_data_type import InvalidDataType
from custom_exceptions.client_id_not_found import ClientIDNotFound
from custom_exceptions.account_id_not_found import AccountIDNotFound
from custom_exceptions.no_accounts import NoAccountsForClient
from custom_exceptions.inadequate_funds import InadequateFunds
from custom_exceptions.input_too_long import InputTooLong

from api_package_layer.convert_to_dictionary import client_id_only
from api_package_layer.convert_to_dictionary import account_id_only
from api_package_layer.convert_to_dictionary import account_with_amount

app: Flask = Flask(__name__)

app_client_data_imp = ClientDataImplementation()
app_client_service_imp = ClientServiceImplementation(app_client_data_imp)
app_account_data_imp = AccountDataImplementation()
app_account_service_imp = AccountServiceImplementation(app_account_data_imp)

# Hello world test to ensure the app is running and the base HTTPS path has been configured correctly.
@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello world!"

# Create a new client.
@app.route("/newclient", methods=["POST"])
def api_create_new_client():
    try:
        received_json: dict = request.get_json()
        first_name = received_json["firstName"]
        last_name = received_json["lastName"]
        result = app_client_service_imp.create_new_client(first_name, last_name)
        result_dictionary = client_id_only(result)
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except InputTooLong as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except:
        message = {
            "message": "Something went completely wrong. Please contact administration."
        }
        return jsonify(message), 400

# Create a new account.
@app.route("/newaccount", methods=["POST"]) #clientID might want to be placed in the URL
def api_create_new_account():
    try:
        received_json: dict = request.get_json()
        client_id = received_json["clientID"]
        starting_amount = received_json["startingAmount"]
        result = app_account_service_imp.create_new_account(client_id, starting_amount)
        result_dictionary = account_id_only(result)
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message)
    except ClientIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message)
    except:
        message = {
            "message": "Something went completely wrong. Please contact administration."
        }
        return jsonify(message), 400

# View account balance.
@app.route("/viewaccount/<clientID>/<accountID>", methods=["GET"]) #something's going wrong without throwing an actual error message, it's just returning null
def api_view_account_balance(clientID: str, accountID: str):
    try:
        result = app_account_service_imp.view_account_balance(clientID, accountID)
        result_dictionary = account_with_amount(accountID, result)
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {
            "message": str(exception)
        }
        return message, 400
    except ClientIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return message, 400
    except AccountIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return message, 400
    except:
        message = {
            "message": "Something went completely wrong. Please contact administration."
        }
        return jsonify(message), 400

# View all of a client's accounts.
@app.route("/viewallaccounts/<clientID>", methods=["GET"])
def api_view_all_client_accounts(clientID: str):
    try:
        result = app_client_service_imp.get_all_accounts_by_id(clientID) #reconfigure this data line to return a dictionary?
        result_dictionary = {
            "All Account Balances": result
        }
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except NoAccountsForClient as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except:
        message = {
            "message": "Something went completely wrong. Please contact administration."
        }
        return jsonify(message), 400

# Withdraw from an account.
@app.route("/withdraw/<clientID>/<accountID>", methods=["POST"])
def api_withdraw_from_account(clientID: str, accountID: str):
    try:
        received_json: dict = request.get_json()
        withdraw_amount = received_json["withdrawAmount"]
        result = app_account_service_imp.withdraw_from_account(clientID, accountID, withdraw_amount)
        result_dictionary = account_with_amount(accountID, result)
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except InadequateFunds as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except:
        message = {
            "message": "Something went completely wrong. Please contact administration."
        }
        return jsonify(message), 400

# Deposit into an account.
@app.route("/deposit/<clientID>/<accountID>", methods=["POST"])
def api_deposit_into_account(clientID: str, accountID: str):
    try:
        received_json: dict = request.get_json()
        deposit_amount = received_json["depositAmount"]
        result = app_account_service_imp.deposit_into_account(clientID, accountID, deposit_amount)
        result_dictionary = account_with_amount(accountID, result)
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except:
        message = {
            "message": "Something went completely wrong. Please contact administration."
        }
        return jsonify(message), 400

# Transfer money between two accounts.
@app.route("/transfer/<clientID>", methods=["POST"])
def api_transfer_between_accounts(clientID: str):
    try:
        received_json = request.get_json()
        account_from = received_json["accountFrom"]
        account_to = received_json["accountTo"]
        transfer_amount = received_json["transferAmount"]
        result = app_client_service_imp.transfer_between_accounts(clientID, account_from, account_to, transfer_amount) #reconfigure to return a dictionary? (boolean + accounts and current balances)
        result_dictionary = {
            "Transfer Result": result
        }
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except InadequateFunds as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except:
        message = {
            "message": "Something went completely wrong. Please contact administration."
        }
        return jsonify(message), 400

# Delete an account.
@app.route("/deleteaccount/<clientID>/<accountID>", methods=["POST"])
def api_delete_account(clientID: str, accountID: str):
    try:
        result = app_account_service_imp.delete_account(clientID, accountID) #hm
        result_dictionary = {
            "Message": "Account deleted successfully."
        }
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except:
        message = {
            "message": "Something went completely wrong. Please contact administration."
        }
        return jsonify(message), 400

# Remove a client.
@app.route("/deleteclient/<clientID>", methods=["POST"])
def api_delete_client(clientID: str):
    try:
        result = app_client_service_imp.delete_client(clientID) #hm but again
        result_dictionary = {
            "Message": "Client removed successfully. We are sorry to see you go."
        }
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {
            "message": str(exception)
        }
        return jsonify(message), 400
    except:
        message = {
            "message": "Something went completely wrong. Please contact administration."
        }
        return jsonify(message), 400

app.run()
