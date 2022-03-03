class AccountData:
    account_id_value = 1

    def __init__(self, client_id: str, starting_amount: float):
        self.holding_client = client_id
        self.account_id = f"{client_id}{self.account_id_value}"
        AccountData.account_id_value += 1
        self.current_balance = starting_amount