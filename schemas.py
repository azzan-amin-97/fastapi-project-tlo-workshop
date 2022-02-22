from datetime import datetime
from pydantic import BaseModel


class Booking(BaseModel):
    name: str = "Aiman"
    pax: int = 0
    roomType: str = "Single Pod / Family Suite / Grand Deluxe"
    checkIn: datetime = "2022-01-10 12:15:21"
    checkOut: datetime = "2022-01-03 15:30:25"
    paymentStatus: str  = "paid / unpaid"


class UpdateBooking(BaseModel):
    pax: int = 0
    roomType: str = "Single Pod / Family Suite / Grand Deluxe"
    checkIn: datetime = "0000-00-00 00:00:00"
    checkOut: datetime = "0000-00-00 00:00:00"

