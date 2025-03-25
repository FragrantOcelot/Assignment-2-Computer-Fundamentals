"""
LoyaltyAccount Module
---------------------
Manages guest loyalty points logic.
"""

class LoyaltyAccount:
    """
    Holds the guest's loyalty points and methods to add/redeem them.
    """

    def __init__(self, points: int = 0):
        """
        Constructor for LoyaltyAccount.

        :param points: Initial loyalty points (default=0)
        """
        self._points = points

    def getPoints(self) -> int:
        return self._points

    def setPoints(self, p: int) -> None:
        self._points = p

    def addPoints(self, p: int) -> None:
        """
        Adds loyalty points to the account.
        """
        self._points += p

    def redeemPoints(self, p: int) -> None:
        """
        Redeems points if possible (placeholder logic).
        """
        if p <= self._points:
            self._points -= p
            print(f"Redeemed {p} points. Remaining balance: {self._points}")
        else:
            print("Not enough points to redeem.")

    def __str__(self) -> str:
        return f"LoyaltyAccount(points={self._points})"
