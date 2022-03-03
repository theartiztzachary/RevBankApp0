class ClientData:
    client_id_value = 1

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        temp_first = first_name.lower()
        temp_last = last_name.lower()
        self.client_id = f"{temp_first[0]}{temp_last[0]}{self.client_id_value}"
        ClientData.client_id_value += 1
        self.client_accounts = {}