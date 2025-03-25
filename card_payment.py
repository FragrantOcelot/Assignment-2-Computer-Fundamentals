"""
CardPayment Module
------------------
A specialized payment type using a credit or debit card.
"""

from payment import Payment

class CardPayment(Payment):
    """
    Subclass of Payment for credit/debit card transactions.
    """

    def __init__(self, payment_id: int, amount: float, payment_method: str, card_number: str):
        """
        :param payment_id: Unique payment ID
        :param amount: Payment amount
        :param payment_method: 'CreditCard' or 'DebitCard'
        :param card_number: The card used for payment
        """
        super().__init__(payment_id, amount, payment_method)
        self._cardNumber = card_number

    def getCardNumber(self) -> str:
        return self._cardNumber

    def setCardNumber(self, c: str) -> None:
        self._cardNumber = c

    def processPayment(self) -> None:
        """
        Overrides parent's method for card-specific validations.
        """
        # Placeholder for contacting card gateway, verifying cardNumber, etc.
        print(f"Validating card number: {self._cardNumber}")
        super().processPayment()

    def __str__(self) -> str:
        parent_str = super().__str__()
        return f"{parent_str}, CardNumber=****{self._cardNumber[-4:]}"
