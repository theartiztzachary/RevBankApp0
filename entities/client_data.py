class ClientData:
    def __init__(self, first_name: str, last_name: str, client_id: str, database_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.client_id = client_id
        self.database_id = database_id
        self.client_accounts = {}

    def __str__(self):
        return f"{self.last_name}, {self.first_name}\nClient ID: {self.client_id}"