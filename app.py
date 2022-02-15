from fastapi import FastAPI
from schemas import Booking, UpdateBooking
from crud import generate_booking_id, add, update, delete, get_booking_by_id, delete

app = FastAPI()


@app.get('/')
def root():
    return {"message":"Welcome to TLO FastAPI Workshop!"}


@app.post('/bookings')
def create_booking(bookingObj: Booking):
    newBookingId = generate_booking_id(bookingObj)
    add(newBookingId, bookingObj)
    return {
        "status": True,
        "bookingId": newBookingId,
        "message": "Booking created successfully"
    }

@app.put('/bookings/{bookingId}')
def update_booking(bookingId, bookingObj: UpdateBooking):
    result = update(bookingId, bookingObj)
    return {
        "status": result['status'],
        "bookingId": bookingId,
        "message": result['message'],
        "booking": result['booking']
    }

@app.delete('/bookings/{bookingId}')
def cancel_booking(bookingId):
    result = delete(bookingId)
    return {
        "status": result['status'],
        "message": result['message'],
    }

@app.get('/bookings/{bookingId}')
def view_booking(bookingId):
    result = get_booking_by_id(bookingId)
    return {
        "status": result['status'],
        "message": result['message'],
        "booking": result['booking']
    }
    