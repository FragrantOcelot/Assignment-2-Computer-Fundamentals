"""
Guest Module
------------
Defines the Guest class for the Royal Stay Hotel System.
"""

class Guest:
    """
    Represents a hotel guest with personal information and loyalty points.
    """

    def __init__(self, name: str, email: str, phone: str, loyalty_points: int = 0):
        """
        Constructor for Guest.

        :param name: Guest's full name
        :param email: Guest's email address
        :param phone: Guest's phone number
        :param loyalty_points: Initial loyalty points (default=0)
        """
        self._name = name
        self._email = email
        self._phone = phone
        self._loyaltyPoints = loyalty_points

    def getName(self) -> str:
        return self._name

    def setName(self, n: str) -> None:
        self._name = n

    def getEmail(self) -> str:
        return self._email

    def setEmail(self, e: str) -> None:
        self._email = e

    def getPhone(self) -> str:
        return self._phone

    def setPhone(self, p: str) -> None:
        self._phone = p

    def getLoyaltyPoints(self) -> int:
        return self._loyaltyPoints

    def setLoyaltyPoints(self, points: int) -> None:
        self._loyaltyPoints = points

    def createAccount(self) -> None:
        """
        Placeholder method to simulate account creation logic.
        """
        print(f"Account created for {self._name} (Email: {self._email})")

    def updateProfile(self) -> None:
        """
        Placeholder method to simulate profile update logic.
        """
        print(f"Profile updated for {self._name}.")

    def __str__(self) -> str:
        """
        Returns a string representation of the Guest.
        """
        return f"Guest(name={self._name}, email={self._email}, phone={self._phone}, loyaltyPoints={self._loyaltyPoints})"
