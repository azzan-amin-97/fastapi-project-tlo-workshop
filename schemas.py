from datetime import datetime
from pydantic import BaseModel, Field, validator


class Booking(BaseModel):
    name: str = None
    pax:int = Field(...,gt=0, title="Number of guests",description="The guest must be more than 1 person")
    roomType: str = Field(..., title="Room Type",description="Room Type => Single Pod / Family Suite / Grand Deluxe")
    checkIn: datetime = Field(..., title="Check In Date",description="YYYY-mm-dd HH:mm:ss")
    checkOut: datetime = Field(..., title="Check Out Date",description="YYYY-mm-dd HH:mm:ss")
    paymentStatus: str  = Field(...,title="Payment Status",description="Status => Paid / Unpaid")
    status: str = "active"
    

class UpdateBooking(BaseModel):
    pax: int = 0
    roomType: str = "Single Pod / Family Suite / Grand Deluxe"
    checkIn: datetime = "0000-00-00 00:00:00"
    checkOut: datetime = "0000-00-00 00:00:00"

