from fastapi import FastAPI, status, Request
from schemas import Booking, UpdateBooking
from fastapi.encoders import jsonable_encoder
from crud import generate_booking_id, add, update, cancel, get_booking_by_id
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI(title="Hotel Booking API", description="")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"status": False, "message":"Booking failed. Missing required parameter"}),
    )
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=400,
        content={"message": f"{exc.name}"},
    )

@app.get('/', tags=['Customer Booking API'])
def root():
    return {"message":"Welcome to TLO FastAPI Workshop!"}


# Function: create_booking()
# Parameters: bookingObj
# Return: status, message, bookingId
@app.post('/bookings', tags=['Customer Booking API'])
def create_booking(bookingObj: Booking):
    newBookingId = generate_booking_id(bookingObj)
    result = add(newBookingId, bookingObj)

    if not result['status']:
        return JSONResponse(
        status_code=400,
        content={"message": result['message'],"status":False},
    )

    return {
        "status": result['status'],
        "bookingId": newBookingId,
        "message": result['message']
    }

# Function: update_booking()
# Parameters: bookingId, bookingObj
# Return: status, message, bookingId, booking
@app.put('/bookings/{bookingId}', tags=['Customer Booking API'])
def update_booking(bookingId, bookingObj: UpdateBooking):
    result = update(bookingId, bookingObj)
    return {
        "status": result['status'],
        "bookingId": bookingId,
        "message": result['message'],
        "booking": result['booking']
    }

# Function: cancel_booking()
# Parameters: bookingId
# Return: status, message
@app.delete('/bookings/{bookingId}', tags=['Customer Booking API'])
def cancel_booking(bookingId):
    result = cancel(bookingId)
    return {
        "status": result['status'],
        "message": result['message'],
    }

# Function: view_booking()
# Parameters: bookingId
# Return: status, message, booking
@app.get('/bookings/{bookingId}', tags=['Customer Booking API'])
def view_booking(bookingId):
    result = get_booking_by_id(bookingId)
    return {
        "status": result['status'],
        "message": result['message'],
        "booking": result['booking']
    }

