class ClientData:
    def __init__(self, first_name: str, last_name: str, client_id: str):
        self.first_name = first_name
        self.last_name = last_name
        self.client_id = client_id
        self.client_accounts = {}

    def __str__(self):
        return f"{self.last_name}, {self.first_name}\nClient ID: {self.client_id}"

    def client_to_dictionary(self) -> dict:
        dictionary = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "clientID": self.client_id
        }

        for key in self.client_accounts.keys():
            dictionary[key] = self.client_accounts[key]

        return dictionary