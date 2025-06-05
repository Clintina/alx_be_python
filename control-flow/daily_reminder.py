# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority using match-case (Python 3.10+ required)
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task. Stay on top of it!"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Invalid priority input for task: '{task}'. Please enter high, medium, or low."

# Final reminder message formatting
print(f"Reminder: '{task}' is a {priority} priority task.", end="")

# Add urgency if time-bound
if time_bound == "yes":
    print(" That requires immediate attention today!")
else:
    print(" Consider completing it when you have free time.")

# Print the customized reminder
print(reminder)