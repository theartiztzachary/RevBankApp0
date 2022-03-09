class AccountDataInit:
    account_id_value = 1

    def __init__(self, client_id: str, starting_amount: float):
        self.holding_client = client_id
        self.account_id = f"{client_id}{self.account_id_value}"
        AccountDataInit.account_id_value += 1
        self.current_balance = starting_amount
        self.database_id = 0

    def __str__(self):
        return f"Account ID: {self.account_id}\nCurrent Balance: {self.current_balance}"

class AccountData:
    def __init__(self, client_id: str, account_id: str, account_balance: float, database_id: int):
        self.client_id = client_id
        self.account_id = account_id
        self.account_balance = account_balance
        self.database_id = database_id