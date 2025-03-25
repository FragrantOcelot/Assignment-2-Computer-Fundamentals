"""
Payment Module
--------------
Generic payment class for handling transactions (credit, debit, digital, etc.).
"""

class Payment:
    """
    Parent class for payment. Subclasses might specialize for card or digital wallets.
    """

    def __init__(self, payment_id: int, amount: float, payment_method: str):
        """
        :param payment_id: Unique payment identifier
        :param amount: Payment amount
        :param payment_method: 'CreditCard', 'DigitalWallet', etc.
        """
        self._paymentID = payment_id
        self._amount = amount
        self._paymentMethod = payment_method

    def getPaymentID(self) -> int:
        return self._paymentID

    def getAmount(self) -> float:
        return self._amount

    def setAmount(self, a: float) -> None:
        self._amount = a

    def getPaymentMethod(self) -> str:
        return self._paymentMethod

    def setPaymentMethod(self, m: str) -> None:
        self._paymentMethod = m

    def processPayment(self) -> None:
        """
        Placeholder for actual payment processing logic.
        """
        print(f"Processing {self._paymentMethod} payment #{self._paymentID} for amount {self._amount:.2f}")

    def __str__(self) -> str:
        return (f"Payment(ID={self._paymentID}, Method={self._paymentMethod}, "
                f"Amount={self._amount:.2f})")
