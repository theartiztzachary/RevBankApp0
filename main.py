from flask import Flask, request, jsonify

from data_access_layer.client_data_implementation import ClientDataImplementation
from service_layer.client_service_implementation import ClientServiceImplementation
from data_access_layer.account_data_implementation import AccountDataImplementation
from service_layer.account_service_implementation import AccountServiceImplementation

from utilities.custom_exceptions import InvalidDataType, DatabaseConnection, ClientIDNotFound, AccountIDNotFound, NoAccounts, InadequateFunds, FundsStillExist, AccountsStillExist

app: Flask = Flask(__name__)

app_client_data_imp = ClientDataImplementation()
app_client_service_imp = ClientServiceImplementation(app_client_data_imp)
app_account_data_imp = AccountDataImplementation()
app_account_service_imp = AccountServiceImplementation(app_account_data_imp)

## Hello world test to ensure the app is running and the base HTTPS path has been configured correctly.
@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello world!"

## Create a new client.
@app.route("/newclient", methods=["POST"])
def api_create_new_client():
    try:
        received_json: dict = request.get_json()
        first_name = received_json["firstName"]
        last_name = received_json["lastName"]
        result = app_client_service_imp.create_new_client(first_name, last_name)
        result_dictionary = result.client_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except DatabaseConnection as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except Exception as exception:
        message = {
            "message": "Something unknown went wrong. Please contact administration.",
            "errorCode:": str(exception)}
        return jsonify(message), 400

## Create a new account with a client.
@app.route("/<client_id>/newaccount", methods=["POST"])
def api_create_new_account(client_id: str):
    try:
        received_json: dict = request.get_json()
        starting_amount = received_json["startingAmount"]
        result = app_account_service_imp.create_new_account(client_id, starting_amount)
        result_dictionary = result.account_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        return jsonify(message)
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
    except DatabaseConnection as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except Exception as exception:
        message = {
            "message": "Something unknown went wrong. Please contact administration.",
            "errorCode:": str(exception)}
        return jsonify(message), 400

## View account information.
@app.route("/<client_id>/<account_id>/view", methods=["GET"])
def api_view_account_information(client_id: str, account_id: str):
    try:
        result = app_account_service_imp.view_account_information(client_id, account_id)
        result_dictionary = result.account_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {"message": str(exception)}
        return message, 400
    except DatabaseConnection as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except Exception as exception:
        message = {
            "message": "Something unknown went wrong. Please contact administration.",
            "errorCode:": str(exception)}
        return jsonify(message), 400

## View all of a client's accounts.
@app.route("/<client_id>/viewall", methods=["GET"])
def api_view_all_client_accounts(client_id: str):
    try:
        result = app_client_service_imp.view_all_client_accounts(client_id)
        result_dictionary = result.client_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except NoAccounts as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except ConnectionError as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except Exception as exception:
        message = {
            "message": "Something unknown went wrong. Please contact administration.",
            "errorCode:": str(exception)}
        return jsonify(message), 400

## Withdraw from an account.
@app.route("/<client_id>/<account_id>/withdraw", methods=["POST"])
def api_withdraw_from_account(client_id: str, account_id: str):
    try:
        received_json: dict = request.get_json()
        withdraw_amount = received_json["withdrawAmount"]
        result = app_account_service_imp.withdraw_from_account(client_id, account_id, withdraw_amount)
        result_dictionary = result.account_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except InadequateFunds as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except DatabaseConnection as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except Exception as exception:
        message = {
            "message": "Something unknown went wrong. Please contact administration.",
            "errorCode:": str(exception)}
        return jsonify(message), 400

## Deposit into an account.
@app.route("/<client_id>/<account_id>/deposit", methods=["POST"])
def api_deposit_into_account(client_id: str, account_id: str):
    try:
        received_json: dict = request.get_json()
        deposit_amount = received_json["depositAmount"]
        result = app_account_service_imp.deposit_into_account(client_id, account_id, deposit_amount)
        result_dictionary = result.account_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except DatabaseConnection as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except Exception as exception:
        message = {
            "message": "Something unknown went wrong. Please contact administration.",
            "errorCode:": str(exception)}
        return jsonify(message), 400

## Transfer money between two accounts.
@app.route("/<client_id>/transfer", methods=["POST"])
def api_transfer_between_accounts(client_id: str):
    try:
        received_json = request.get_json()
        account_from = received_json["accountFrom"]
        account_to = received_json["accountTo"]
        transfer_amount = received_json["transferAmount"]
        result = app_client_service_imp.transfer_between_accounts(client_id, account_from, account_to, transfer_amount)
        result_dictionary = result.client_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except InadequateFunds as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except NoAccounts as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except DatabaseConnection as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except Exception as exception:
        message = {
            "message": "Something unknown went wrong. Please contact administration.",
            "errorCode:": str(exception)}
        return jsonify(message), 400

## Delete an account.
@app.route("/<client_id>/<account_id>/deleteaccount", methods=["POST"])
def api_delete_account(client_id: str, account_id: str):
    try:
        result = app_account_service_imp.delete_account(client_id, account_id)
        result_dictionary = {"message": result}
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except FundsStillExist as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except DatabaseConnection as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except Exception as exception:
        message = {
            "message": "Something unknown went wrong. Please contact administration.",
            "errorCode:": str(exception)}
        return jsonify(message), 400

## Delete a client.
@app.route("/<client_id>/deleteclient", methods=["POST"])
def api_delete_client(client_id: str):
    try:
        result = app_client_service_imp.delete_client(client_id)
        result_dictionary = {"message": result}
        result_json = jsonify(result_dictionary)
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except AccountsStillExist as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except DatabaseConnection as exception:
        message = {"message": str(exception)}
        return jsonify(message), 400
    except Exception as exception:
        message = {
            "message": "Something unknown went wrong. Please contact administration.",
            "errorCode:": str(exception)}
        return jsonify(message), 400

## Oh we runnin' boios.
app.run()