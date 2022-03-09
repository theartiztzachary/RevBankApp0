class AccountData:
    def __init__(self, client_id: str, account_id: str, account_balance: float, database_id: int):
        self.client_id = client_id
        self.account_id = account_id
        self.account_balance = account_balance
        self.database_id = database_id