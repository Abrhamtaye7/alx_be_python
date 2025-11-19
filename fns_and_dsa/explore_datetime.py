from datetime import datetime, timedelta


def display_current_datetime():
    display_current_datetime = datetime.now()
    return display_current_datetime


print(
    f"Current date and time: {display_current_datetime().strftime('%Y-%m-%d %H:%M:%S')}")


def number_of_days():
    while True:
        try:
            days = int(
                str(input("Enter the number of days to add to the current date: ")))
            return days
        except ValueError:
            print("Please enter a valid integer.")


calculate_future_date = display_current_datetime() + \
    timedelta(days=number_of_days())
print(f"Future date: {calculate_future_date.strftime('%Y-%m-%d')}")
