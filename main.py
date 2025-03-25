"""
test_app.py
-----------
This script demonstrates 8 major test scenarios for the Royal Stay Hotel System,
each with 2 examples. It uses the classes defined in separate modules:
(guest.py, loyaltyaccount.py, servicerequest.py, room.py, booking.py, invoice.py,
 payment.py, digitalpayment.py, cardpayment.py).
"""

from guest import Guest
from loyalty_account import LoyaltyAccount
from service_request import ServiceRequest
from room import Room
from booking import Booking
from invoice import Invoice
from payment import Payment
from digital_payment import DigitalPayment
from card_payment import CardPayment

def test_guest_account_creation():
    print("=== TEST 1: GUEST ACCOUNT CREATION ===")
    
    # Example 1: Bruce Wayne
    bruce = Guest(name="Bruce Wayne", email="bruce@wayneenterprises.com", phone="111-222-3333")
    bruce.createAccount()  # demonstration of account creation
    print(bruce)
    
    # Example 2: Jordan Belfort
    jordan = Guest(name="Jordan Belfort", email="jordan@wallstreet.com", phone="999-888-7777")
    jordan.createAccount()
    print(jordan)
    
    print("=== END TEST 1 ===\n")

def test_search_rooms():
    print("=== TEST 2: SEARCHING FOR AVAILABLE ROOMS ===")
    
    # Create a few rooms
    room1 = Room(room_number=101, room_type="Single", amenities=["Wi-Fi"], price_per_night=120.0, is_available=True)
    room2 = Room(room_number=102, room_type="Double", amenities=["Wi-Fi", "TV"], price_per_night=150.0, is_available=False)
    room3 = Room(room_number=103, room_type="Suite", amenities=["Wi-Fi", "Mini-Bar", "TV"], price_per_night=300.0, is_available=True)
    
    all_rooms = [room1, room2, room3]

    # Example 1: Bruce Wayne searches for available rooms
    available_rooms = [r for r in all_rooms if r.isAvailable()]
    print("Bruce Wayne sees these available rooms:")
    for r in available_rooms:
        print(r)

    # Example 2: Jordan Belfort also searches
    # (Exact same logic, but let's pretend it's a separate scenario)
    print("\nJordan Belfort sees these available rooms:")
    for r in available_rooms:
        print(r)

    print("=== END TEST 2 ===\n")

def test_make_room_reservation():
    print("=== TEST 3: MAKING A ROOM RESERVATION ===")
    
    # Create two guests
    bruce = Guest("Bruce Wayne", "bruce@wayneenterprises.com", "111-222-3333")
    jordan = Guest("Jordan Belfort", "jordan@wallstreet.com", "999-888-7777")
    
    # Create a room
    room101 = Room(room_number=101, room_type="Single", amenities=["Wi-Fi"], price_per_night=120.0, is_available=True)
    
    # Example 1: Bruce books room 101
    booking_bruce = Booking(booking_id=1001, check_in_date="2025-04-01", check_out_date="2025-04-03")
    print("Bruce's booking before confirmation:", booking_bruce)
    
    # Example 2: Jordan books same room (simultaneous scenario)
    booking_jordan = Booking(booking_id=1002, check_in_date="2025-04-02", check_out_date="2025-04-05")
    print("Jordan's booking before confirmation:", booking_jordan)
    
    print("=== END TEST 3 ===\n")

def test_booking_confirmation():
    print("=== TEST 4: BOOKING CONFIRMATION NOTIFICATION ===")
    
    # Create bookings
    booking1 = Booking(booking_id=1001, check_in_date="2025-04-01", check_out_date="2025-04-03")
    booking2 = Booking(booking_id=1002, check_in_date="2025-04-02", check_out_date="2025-04-05")

    # Example 1: Confirm Bruce Wayne's booking
    booking1.confirmBooking()
    
    # Example 2: Confirm Jordan Belfort's booking
    booking2.confirmBooking()
    
    print("=== END TEST 4 ===\n")

def test_invoice_generation():
    print("=== TEST 5: INVOICE GENERATION FOR A BOOKING ===")
    
    # Example 1: Invoice for Bruce Wayne
    invoice_bruce = Invoice(invoice_id=3001, nightly_rate=120 * 2, additional_charges=50.0, discounts=20.0)
    print(invoice_bruce)
    invoice_bruce.generateInvoice()  # prints total
    
    # Example 2: Invoice for Jordan Belfort
    invoice_jordan = Invoice(invoice_id=3002, nightly_rate=150 * 3, additional_charges=0.0, discounts=0.0)
    print(invoice_jordan)
    invoice_jordan.generateInvoice()
    
    print("=== END TEST 5 ===\n")

def test_different_payment_methods():
    print("=== TEST 6: PROCESSING DIFFERENT PAYMENT METHODS ===")
    
    # Example 1: DigitalPayment for Bruce Wayne
    payment_bruce = DigitalPayment(payment_id=4001, amount=250.0, payment_method="DigitalWallet", wallet_id="WAYNE-WALLET-123")
    payment_bruce.processPayment()
    print(payment_bruce)

    # Example 2: CardPayment for Jordan Belfort
    payment_jordan = CardPayment(payment_id=4002, amount=450.0, payment_method="CreditCard", card_number="1234567890123456")
    payment_jordan.processPayment()
    print(payment_jordan)
    
    print("=== END TEST 6 ===\n")

def test_display_reservation_history():
    print("=== TEST 7: DISPLAYING RESERVATION HISTORY ===")

    # For a real system, you'd store each Guest's bookings in a list. Let's simulate it:
    bruce = Guest("Bruce Wayne", "bruce@wayneenterprises.com", "111-222-3333")
    bookingA = Booking(booking_id=9001, check_in_date="2025-05-01", check_out_date="2025-05-03")
    bookingB = Booking(booking_id=9002, check_in_date="2025-06-01", check_out_date="2025-06-05")
    
    # Simulate that Bruce made these bookings
    bruce_bookings = [bookingA, bookingB]

    # Example 1: Bruce's reservation history
    print("Bruce Wayne's Reservation History:")
    for b in bruce_bookings:
        print(b)

    # Example 2: Jordan Belfort with 1 previous booking
    jordan = Guest("Jordan Belfort", "jordan@wallstreet.com", "999-888-7777")
    bookingC = Booking(booking_id=9003, check_in_date="2025-07-01", check_out_date="2025-07-02")
    jordan_bookings = [bookingC]

    print("\nJordan Belfort's Reservation History:")
    for b in jordan_bookings:
        print(b)
    
    print("=== END TEST 7 ===\n")

def test_cancel_reservation():
    print("=== TEST 8: CANCELLATION OF A RESERVATION ===")
    
    # Example 1: Cancel Bruce Wayne's booking
    booking1 = Booking(booking_id=5001, check_in_date="2025-08-01", check_out_date="2025-08-03")
    booking1.cancelBooking()
    print(booking1)

    # Example 2: Cancel Jordan Belfort's booking
    booking2 = Booking(booking_id=5002, check_in_date="2025-08-05", check_out_date="2025-08-07")
    booking2.cancelBooking()
    print(booking2)
    
    print("=== END TEST 8 ===\n")

def main():
    test_guest_account_creation()
    test_search_rooms()
    test_make_room_reservation()
    test_booking_confirmation()
    test_invoice_generation()
    test_different_payment_methods()
    test_display_reservation_history()
    test_cancel_reservation()

if __name__ == "__main__":
    main()
