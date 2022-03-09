def client_id_only(client_id: str):
    new_dict = {
        "Client ID": client_id
    }
    return new_dict

def account_id_only(account_id: str):
    new_dict = {
        "Account ID": account_id
    }
    return new_dict

def account_with_amount(account_id: str, account_balance: float):
    new_dict = {
        "Account ID": account_id,
        "Current Balance": account_balance
    }
    return new_dict