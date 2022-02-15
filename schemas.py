from datetime import datetime
from lib2to3.pytree import Base
from pydantic import BaseModel

# class Booking(BaseModel):
#     bookingId: str
#     name: str
#     pax: int
#     roomType: str
#     checkIn: datetime
#     checkOut: datetime
#     paymentStatus: str 


class Booking(BaseModel):
    name: str = "undefined"
    pax: int = 0
    roomType: str = "default"
    checkIn: datetime = "0000-00-00 00:00:00"
    checkOut: datetime = "0000-00-00 00:00:00"
    paymentStatus: str  = "none"


class UpdateBooking(BaseModel):
    pax: int = 0
    roomType: str = "default"
    checkIn: datetime = "0000-00-00 00:00:00"
    checkOut: datetime = "0000-00-00 00:00:00"
