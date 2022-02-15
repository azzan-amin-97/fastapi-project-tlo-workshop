import pandas as pd

def generate_booking_id(booking_obj):
    bookingId = booking_obj.checkIn.strftime("%Y%m%d-%H%M%S") + "-" + booking_obj.name
    return bookingId
    

def add(bookingId, booking_obj):
    df_booking = fetch_data()
    booking_dict = booking_obj.dict()
    booking_dict['bookingId'] =  bookingId
    df_booking = df_booking.append(booking_dict, ignore_index=True)
    save_data(df_booking)
    print('Booking saved!')

def update(bookingId, booking_obj):
    df_booking = fetch_data()
    num_of_rows = len(df_booking.loc[df_booking['bookingId']==bookingId])
    if num_of_rows>0:
        df_booking.loc[df_booking['bookingId']==bookingId, 'pax'] = booking_obj.pax
        df_booking.loc[df_booking['bookingId']==bookingId, 'roomType'] = booking_obj.roomType
        df_booking.loc[df_booking['bookingId']==bookingId, 'checkIn'] = booking_obj.checkIn
        df_booking.loc[df_booking['bookingId']==bookingId, 'checkOut'] = booking_obj.checkOut
        save_data(df_booking)
        updated_booking = list(df_booking.loc[df_booking['bookingId']==bookingId].T.to_dict('dict').values())[0]
        message = 'Booking updated successfully'
        status = True
    else:
        updated_booking = {}
        message = 'Cannot found the booking ID'
        status = False
    return {"status": status, "message": message, "booking":updated_booking}

def delete(bookingId):
    df_booking = fetch_data()
    filer_df = df_booking.loc[df_booking['bookingId']==bookingId]
    if len(filer_df)>0:
        row_index = (filer_df.index)[0]
        df_booking.drop(labels=row_index, axis=0, inplace=True)
        save_data(df_booking)
        message = 'Booking deleted successfully'
        status = True
    else:
        message = 'Cannot found the booking ID'
        status = False
    return {"status": status, "message": message}

def get_booking_by_id(bookingId):
    df_booking = fetch_data()
    filter_df = df_booking.loc[df_booking['bookingId']==bookingId]
    if len(filter_df)>0:
        booking_info = list(filter_df.T.to_dict('dict').values())[0]
        message = 'Booking retrieved successfully'
        status = True
    else:
        booking_info = {}
        message = 'Cannot found the booking ID'
        status = False

    return {"status": status, "message": message, "booking":booking_info}

def get_all_bookings():
    pass

def fetch_data():
    df_booking = pd.read_csv('data/booking_data.csv')
    return df_booking

def save_data(df):
    df.to_csv('data/booking_data.csv', index=False)