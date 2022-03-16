from flask import Flask, request, jsonify
import logging

from data_access_layer.client_data_implementation import ClientDataImplementation
from service_layer.client_service_implementation import ClientServiceImplementation
from data_access_layer.account_data_implementation import AccountDataImplementation
from service_layer.account_service_implementation import AccountServiceImplementation

from utilities.custom_exceptions import InvalidDataType, ClientIDNotFound, AccountIDNotFound, NoAccounts, InadequateFunds, FundsStillExist, AccountsStillExist

app: Flask = Flask(__name__)

logging.basicConfig(filename="transaction_history.log", encoding="utf-8", level=logging.DEBUG)

app_client_data_imp = ClientDataImplementation()
app_client_service_imp = ClientServiceImplementation(app_client_data_imp)
app_account_data_imp = AccountDataImplementation()
app_account_service_imp = AccountServiceImplementation(app_account_data_imp)

## Hello world test to ensure the app is running and the base HTTPS path has been configured correctly.
@app.route("/greeting", methods=["GET"])
def hello_world():
    logging.info("Greeting message sent.")
    return "Hello world!"

## Create a new client.
@app.route("/clients", methods=["POST"])
def api_create_new_client():
    try:
        received_json: dict = request.get_json()
        first_name = received_json["firstName"]
        last_name = received_json["lastName"]
        result = app_client_service_imp.create_new_client(first_name, last_name)
        result_dictionary = result.client_to_dictionary()
        result_json = jsonify(result_dictionary)
        logging.info(f"{result.first_name} {result.last_name} became a client with Client ID {result.client_id}.")
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except Exception as exception:
        message = {"message": "Something unknown went wrong. Please contact administration."}
        logging.error(str(exception))
        return jsonify(message), 400

## Create a new account with a client.
@app.route("/clients/<client_id>/account", methods=["POST"])
def api_create_new_account(client_id: str):
    try:
        received_json: dict = request.get_json()
        starting_amount = received_json["startingAmount"]
        result = app_account_service_imp.create_new_account(client_id, starting_amount)
        result_dictionary = result.account_to_dictionary()
        result_json = jsonify(result_dictionary)
        logging.info(f"Client {result.client_id} created a new account with Account ID {result.account_id}.")
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message)
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message)
    except Exception as exception:
        message = {"message": "Something unknown went wrong. Please contact administration."}
        logging.error(str(exception))
        return jsonify(message), 400

## View account information.
@app.route("/clients/<client_id>/account/<account_id>", methods=["GET"])
def api_view_account_information(client_id: str, account_id: str):
    try:
        result = app_account_service_imp.view_account_information(client_id, account_id)
        result_dictionary = result.account_to_dictionary()
        result_json = jsonify(result_dictionary)
        logging.info(f"{result.client_id} viewed account {result.account_id}.")
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return message, 400
    except Exception as exception:
        message = {"message": "Something unknown went wrong. Please contact administration."}
        logging.error(str(exception))
        return jsonify(message), 400

## View all of a client's accounts.
@app.route("/client/<client_id>/accounts", methods=["GET"])
def api_view_all_client_accounts(client_id: str):
    try:
        result = app_client_service_imp.view_all_client_accounts(client_id)
        result_dictionary = result.client_to_dictionary()
        result_json = jsonify(result_dictionary)
        logging.info(f"{result.client_id} viewed all of their accounts.")
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except NoAccounts as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except Exception as exception:
        message = {"message": "Something unknown went wrong. Please contact administration."}
        logging.error(str(exception))
        return jsonify(message), 400

## Withdraw from an account.
@app.route("/client/<client_id>/account/<account_id>/withdraw", methods=["POST"])
def api_withdraw_from_account(client_id: str, account_id: str):
    try:
        received_json: dict = request.get_json()
        withdraw_amount = received_json["withdrawAmount"]
        result = app_account_service_imp.withdraw_from_account(client_id, account_id, withdraw_amount)
        result_dictionary = result.account_to_dictionary()
        result_json = jsonify(result_dictionary)
        logging.info(f"{result.client_id} withdrew {withdraw_amount} from {result.account_id}.")
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except InadequateFunds as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except Exception as exception:
        message = {"message": "Something unknown went wrong. Please contact administration."}
        logging.error(str(exception))
        return jsonify(message), 400

## Deposit into an account.
@app.route("/client/<client_id>/account/<account_id>/deposit", methods=["POST"])
def api_deposit_into_account(client_id: str, account_id: str):
    try:
        received_json: dict = request.get_json()
        deposit_amount = received_json["depositAmount"]
        result = app_account_service_imp.deposit_into_account(client_id, account_id, deposit_amount)
        result_dictionary = result.account_to_dictionary()
        result_json = jsonify(result_dictionary)
        logging.info(f"{result.client_id} deposited {deposit_amount} into {result.account_id}.")
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except Exception as exception:
        message = {"message": "Something unknown went wrong. Please contact administration."}
        logging.error(str(exception))
        return jsonify(message), 400

## Transfer money between two accounts.
@app.route("/client/<client_id>/transfer", methods=["POST"])
def api_transfer_between_accounts(client_id: str):
    try:
        received_json = request.get_json()
        account_from = received_json["accountFrom"]
        account_to = received_json["accountTo"]
        transfer_amount = received_json["transferAmount"]
        result = app_client_service_imp.transfer_between_accounts(client_id, account_from, account_to, transfer_amount)
        result_dictionary = result.client_to_dictionary()
        result_json = jsonify(result_dictionary)
        logging.info(f"{result.client_id} transferred {transfer_amount} from {account_from} to {account_to}.")
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except InadequateFunds as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except NoAccounts as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except Exception as exception:
        message = {"message": "Something unknown went wrong. Please contact administration."}
        logging.error(str(exception))
        return jsonify(message), 400

## Delete an account.
@app.route("/client/<client_id>/account/<account_id>", methods=["DELETE"])
def api_delete_account(client_id: str, account_id: str):
    try:
        result = app_account_service_imp.delete_account(client_id, account_id)
        result_dictionary = {"message": result}
        result_json = jsonify(result_dictionary)
        logging.info(f"{client_id} deleted account {account_id}.")
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except AccountIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except FundsStillExist as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except Exception as exception:
        message = {"message": "Something unknown went wrong. Please contact administration."}
        logging.error(str(exception))
        return jsonify(message), 400

## Delete a client.
@app.route("/client/<client_id>", methods=["DELETE"])
def api_delete_client(client_id: str):
    try:
        result = app_client_service_imp.delete_client(client_id)
        result_dictionary = {"message": result}
        result_json = jsonify(result_dictionary)
        logging.info(f"{client_id} removed from the service.")
        return result_json, 200
    except InvalidDataType as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except ClientIDNotFound as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except AccountsStillExist as exception:
        message = {"message": str(exception)}
        logging.error(str(exception))
        return jsonify(message), 400
    except Exception as exception:
        message = {"message": "Something unknown went wrong. Please contact administration."}
        logging.error(str(exception))
        return jsonify(message), 400

## Oh we runnin' boios.
app.run()