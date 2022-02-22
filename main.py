from fastapi import FastAPI
from schemas import Booking, UpdateBooking
from crud import generate_booking_id, add, update, delete, get_all_bookings, get_booking_by_id

app = FastAPI(title="Hotel Booking API", description="")


@app.get('/', tags=['Customer Booking API'])
def root():
    return {"message":"Welcome to TLO FastAPI Workshop!"}


# Function: create_booking()
# Parameters: bookingObj
# Return: status, message, bookingId
@app.post('/bookings', tags=['Customer Booking API'])
def create_booking(bookingObj: Booking):
    newBookingId = generate_booking_id(bookingObj)
    add(newBookingId, bookingObj)
    return {
        "status": True,
        "bookingId": newBookingId,
        "message": "Booking created successfully"
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
    result = delete(bookingId)
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


# Function: view_all_bookings() - Use API Key
# Return: status, message, booking
# Use `get_all_bookings()` function to get all booking details
# @app.get('/bookings/{api_key}', tags=['Admin Booking API'])
def retrieve_all_bookings(api_key):
    result = get_all_bookings()
    return {
        "status": result['status'],
        "message": result['message'],
        "booking": result['booking']
    }

# Function: update_payment_status() - Use API Key
# Return: status, message, booking
# Use `update_payment()` function to update payment status


# Function: get_daily_bookings() - Use API Key
# Parameters: date (format: 2022-01-01)
# Return: date, number_of_bookings
# Use `get_num_of_bookings_by_date()` function to get daily booking details


