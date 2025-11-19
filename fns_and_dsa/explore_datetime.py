from datetime import datetime, timedelta

# Get the current date and time
display_current_datetime = datetime.now()

# Format the datetime object as a YYYY-MM-DD string
display_current_datetime.strftime("%Y-%m-%d-%H-%M-%S")


print(
    f"Current date and time: {display_current_datetime.strftime('%Y-%m-%d-%H-%M-%S')}")

# Calculate and display the next day


def input_days():
    while True:
        try:
            days = int(
                input("Enter the number of days to add to the current date: "))
            return days
        except ValueError:
            print("Please enter a valid integer.")


calculate_future_date = display_current_datetime + timedelta(days=input_days())
print(f"Future date: {calculate_future_date.strftime('%Y-%m-%d')}")
