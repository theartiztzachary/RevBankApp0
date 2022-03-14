class AccountData:
    def __init__(self, client_id: str, account_id: str, account_balance: float):
        self.client_id = client_id
        self.account_id = account_id
        self.account_balance = account_balance

    def __str__(self):
        return f"Client: {self.client_id}\nAccount ID: {self.account_id}\nCurrent Balance: {self.account_balance}"