from fastapi import FastAPI
from schemas import Booking, UpdateBooking
import pandas as pd
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
    updated_booking = update(bookingId, bookingObj)
    return {
        "status": True,
        "bookingId": bookingId,
        "message": "Booking updated successfully",
        "booking": updated_booking
    }

@app.delete('/bookings/{bookingId}')
def cancel_booking(bookingId):
    delete(bookingId)
    return {
        "status": True,
        "message": "Booking deleted successfully",
    }

@app.get('/bookings/{bookingId}')
def view_booking(bookingId):
    booking_info = get_booking_by_id(bookingId)
    return {
        "status": True,
        "message": "Booking retrieved successfully",
        "booking": booking_info
    }




def generate_booking_id(booking_obj):
    bookingId = booking_obj.check_in.strftime("%Y%m%d-%H%M%S") + "-" + booking_obj.name
    return bookingId
    
def add(bookingId, booking_obj):
    df_booking = fetch_data()
    booking_dict = booking_obj.dict()
    booking_dict['bookingId'] =  bookingId
    df_booking.append(booking_dict)
    save_data(df_booking)

def update(bookingId, booking_obj):
    df_booking = fetch_data()
    df_booking.loc[df_booking['bookingId']==bookingId, 'pax'] = booking_obj.pax
    df_booking.loc[df_booking['bookingId']==bookingId, 'roomType'] = booking_obj.roomType
    df_booking.loc[df_booking['bookingId']==bookingId, 'checkIn'] = booking_obj.checkIn
    df_booking.loc[df_booking['bookingId']==bookingId, 'checkOut'] = booking_obj.checkOut
    save_data(df_booking)
    updated_booking = list(df_booking.loc[df_booking['bookingId']==bookingId].T.to_dict('dict').values())[0]
    return updated_booking

def delete(bookingId):
    df_booking = fetch_data()
    df_booking.drop(bookingId, axis=0, inplace=True)
    save_data(df_booking)

def get_booking_by_id(bookingId):
    df_booking = fetch_data()
    booking_info = df_booking.loc[df_booking['bookingId']==bookingId].T.to_dict('dict').values())[0]
    return booking_info

def fetch_data():
    df_booking = pd.read_csv('data/booking_data.csv')
    return df_booking

def save_data(df):
    df.to_csv('data/booking_data.csv', index=False)