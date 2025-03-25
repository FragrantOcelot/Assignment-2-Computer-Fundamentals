"""
Room Module
-----------
Manages hotel room details such as type, amenities, and price.
"""

class Room:
    """
    Represents a hotel room with its attributes and availability status.
    """

    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float, is_available: bool = True):
        """
        :param room_number: Unique room identifier.
        :param room_type: 'Single', 'Double', 'Suite', etc.
        :param amenities: List of amenities (e.g. ['Wi-Fi','TV','Mini-bar']).
        :param price_per_night: Nightly cost for the room.
        :param is_available: Boolean indicating availability.
        """
        self._roomNumber = room_number
        self._type = room_type
        self._amenities = amenities
        self._pricePerNight = price_per_night
        self._isAvailable = is_available

    def getRoomNumber(self) -> int:
        return self._roomNumber

    def setRoomNumber(self, num: int) -> None:
        self._roomNumber = num

    def getType(self) -> str:
        return self._type

    def setType(self, t: str) -> None:
        self._type = t

    def getAmenities(self) -> list:
        return self._amenities

    def setAmenities(self, a: list) -> None:
        self._amenities = a

    def getPricePerNight(self) -> float:
        return self._pricePerNight

    def setPricePerNight(self, p: float) -> None:
        self._pricePerNight = p

    def isAvailable(self) -> bool:
        return self._isAvailable

    def setAvailability(self, status: bool) -> None:
        self._isAvailable = status

    def __str__(self) -> str:
        return (f"Room(number={self._roomNumber}, type={self._type}, "
                f"amenities={self._amenities}, price={self._pricePerNight}, "
                f"isAvailable={self._isAvailable})")
