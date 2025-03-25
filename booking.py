"""
Booking Module
--------------
Represents a reservation made by a guest for a specific room.
"""

class Booking:
    """
    Stores booking details such as ID, check-in/out dates, and booking status.
    """

    def __init__(self, booking_id: int, check_in_date: str, check_out_date: str, status: str = "Pending"):
        """
        :param booking_id: Unique booking ID.
        :param check_in_date: Check-in date (string or date object).
        :param check_out_date: Check-out date.
        :param status: 'Pending', 'Confirmed', 'Canceled', etc.
        """
        self._bookingID = booking_id
        self._checkInDate = check_in_date
        self._checkOutDate = check_out_date
        self._status = status

    def getBookingID(self) -> int:
        return self._bookingID

    def getCheckInDate(self) -> str:
        return self._checkInDate

    def getCheckOutDate(self) -> str:
        return self._checkOutDate

    def getStatus(self) -> str:
        return self._status

    def setStatus(self, s: str) -> None:
        self._status = s

    def confirmBooking(self) -> None:
        """
        Mark this booking as confirmed.
        """
        self._status = "Confirmed"
        print(f"Booking {self._bookingID} is now CONFIRMED.")

    def cancelBooking(self) -> None:
        """
        Cancel the booking, marking status as canceled.
        """
        self._status = "Canceled"
        print(f"Booking {self._bookingID} is now CANCELED.")

    def __str__(self) -> str:
        return (f"Booking(ID={self._bookingID}, CheckIn={self._checkInDate}, "
                f"CheckOut={self._checkOutDate}, Status={self._status})")
