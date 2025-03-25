"""
Invoice Module
--------------
Represents billing information associated with a booking.
"""

class Invoice:
    """
    Contains financial details like nightly rate, additional charges, and discounts.
    """

    def __init__(self, invoice_id: int, nightly_rate: float, additional_charges: float = 0.0, discounts: float = 0.0):
        """
        :param invoice_id: Unique invoice identifier.
        :param nightly_rate: Base cost per night (could be from Room info).
        :param additional_charges: Sum of extra fees or services.
        :param discounts: Sum of discounts applied to this invoice.
        """
        self._invoiceID = invoice_id
        self._nightlyRate = nightly_rate
        self._additionalCharges = additional_charges
        self._discounts = discounts

    def getInvoiceID(self) -> int:
        return self._invoiceID

    def getTotal(self) -> float:
        """
        Convenience method to get the total amount due.
        """
        return self.calculateTotal()

    def generateInvoice(self) -> None:
        """
        Placeholder to simulate finalizing the invoice for printing or emailing.
        """
        print(f"Invoice {self._invoiceID} generated. Total = {self.calculateTotal():.2f}")

    def calculateTotal(self) -> float:
        """
        Calculates total cost = nightlyRate + additionalCharges - discounts
        """
        return (self._nightlyRate + self._additionalCharges) - self._discounts

    def __str__(self) -> str:
        return (f"Invoice(ID={self._invoiceID}, NightlyRate={self._nightlyRate}, "
                f"Extras={self._additionalCharges}, Discounts={self._discounts}, "
                f"Total={self.getTotal():.2f})")
