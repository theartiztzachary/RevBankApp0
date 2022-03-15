
# # Delete an account.
# @app.route("/deleteaccount/<clientID>/<accountID>", methods=["POST"])
# def api_delete_account(clientID: str, accountID: str):
#     try:
#         result = app_account_service_imp.delete_account(clientID, accountID) #hm
#         result_dictionary = {
#             "Message": "Account deleted successfully."
#         }
#         result_json = jsonify(result_dictionary)
#         return result_json, 200
#     except InvalidDataType as exception:
#         message = {
#             "message": str(exception)
#         }
#         return jsonify(message), 400
#     except AccountIDNotFound as exception:
#         message = {
#             "message": str(exception)
#         }
#         return jsonify(message), 400
#     except ClientIDNotFound as exception:
#         message = {
#             "message": str(exception)
#         }
#         return jsonify(message), 400
#     except:
#         message = {
#             "message": "Something went completely wrong. Please contact administration."
#         }
#         return jsonify(message), 400
#
# # Remove a client.
# @app.route("/deleteclient/<clientID>", methods=["POST"])
# def api_delete_client(clientID: str):
#     try:
#         result = app_client_service_imp.delete_client(clientID) #hm but again
#         result_dictionary = {
#             "Message": "Client removed successfully. We are sorry to see you go."
#         }
#         result_json = jsonify(result_dictionary)
#         return result_json, 200
#     except InvalidDataType as exception:
#         message = {
#             "message": str(exception)
#         }
#         return jsonify(message), 400
#     except ClientIDNotFound as exception:
#         message = {
#             "message": str(exception)
#         }
#         return jsonify(message), 400
#     except:
#         message = {
#             "message": "Something went completely wrong. Please contact administration."
#         }
#         return jsonify(message), 400
#
# app.run()
