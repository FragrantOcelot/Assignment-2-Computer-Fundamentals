"""
DigitalPayment Module
---------------------
A specialized payment type using a digital wallet (PayPal, ApplePay, etc.).
"""

from payment import Payment

class DigitalPayment(Payment):
    """
    Subclass of Payment for digital wallet transactions.
    """

    def __init__(self, payment_id: int, amount: float, payment_method: str, wallet_id: str):
        """
        :param payment_id: Unique payment ID
        :param amount: Payment amount
        :param payment_method: e.g. 'DigitalWallet'
        :param wallet_id: ID associated with a specific digital wallet
        """
        super().__init__(payment_id, amount, payment_method)
        self._walletID = wallet_id

    def getWalletID(self) -> str:
        return self._walletID

    def setWalletID(self, w: str) -> None:
        self._walletID = w

    def processPayment(self) -> None:
        """
        Overrides parent's method with wallet-specific logic.
        """
        # Could add logic to contact the digital wallet provider.
        print(f"Processing digital wallet payment via {self._walletID}.")
        super().processPayment()

    def __str__(self) -> str:
        parent_str = super().__str__()
        return f"{parent_str}, WalletID={self._walletID}"
