# Daily Reminder Script

# Prompt for task details
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task description cannot be empty. Please try again.")

# Loop to ensure valid priority input
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ("high", "medium", "low"):
        break
    print("Please enter a valid priority: high, medium, or low.")

# Loop to ensure valid time-bound input
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ("yes", "no"):
        break
    print("Please answer with 'yes' or 'no'.")

# Use match-case for priority
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done today if possible.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to do it soon.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority but time-sensitive task. Don't forget to do it today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
