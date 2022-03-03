from entities.account_service_interface import AccountServiceInterface

class AccountServiceImplementation(AccountServiceInterface):
    def create_new_account(self, client_id: str) -> str:
        pass

    def view_account_balance(self, client_id: str, account_id: str) -> float:
        pass

    def withdraw_from_account(self, client_id: str, account_id: str, withdraw_amount: float) -> float:
        pass

    def deposit_into_account(self, client_id: str, account_id: str, deposit_amount: float) -> float:
        pass

    def delete_account(self, client_id: str, account_id: str) -> bool:
        pass