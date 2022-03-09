class ClientDataInit:
    client_id_value = 1

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        temp_first = first_name.lower()
        temp_last = last_name.lower()
        self.client_id = f"{temp_first[0]}{temp_last[0]}{self.client_id_value}"
        ClientDataInit.client_id_value += 1
        self.database_id = 0

    def __str__(self):
        return f"{self.last_name}, {self.first_name}\nID: {self.client_id}"

class ClientData:
    def __init__(self, first_name: str, last_name: str, client_id: str, database_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.client_id = client_id
        self.database_id = database_id
        self.client_accounts = []