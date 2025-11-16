# Ask the user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process priority using match case
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Modify message if task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message = "Note: " + message + ". Consider completing it when you have free time."

# Display final reminder message
print(message)

