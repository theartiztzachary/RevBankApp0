from entities.client_interface import ClientInterface
from entities.client_data import ClientData
from utilities.connection_manager import connection

class ClientDataImplementation(ClientInterface):
    client_id_value = 1

    def create_new_client(self, first_name: str, last_name: str) -> ClientData:
        temp_first = first_name.lower()
        temp_last = last_name.lower()
        client_id = f"{temp_first[0]}{temp_last[0]}{self.client_id_value}"
        ClientDataImplementation.client_id_value += 1
        sql_query = "insert into clients values(%s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql_query, (first_name, last_name, client_id))
        connection.commit()
        new_client = ClientData(first_name, last_name, client_id)
        return new_client

    def view_all_client_accounts(self, client_id: str) -> ClientData:
        pass

    def transfer_between_accounts(self, client_id: str, account_from_id: str, account_to_id: str, transfer_amount: float) -> ClientData:
        pass

    def delete_client(self, client_id: str) -> bool:
        pass