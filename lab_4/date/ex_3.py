from datetime import datetime

def drop_microseconds(dt):
    dt_without_microseconds = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    return dt_without_microseconds

if __name__ == "__main__":

    original_datetime = datetime(2024, 3, 2, 12, 30, 45, 987654)

    datetime_without_microseconds = drop_microseconds(original_datetime)

    print("Original datetime:", original_datetime)
    print("Datetime without microseconds:", datetime_without_microseconds)