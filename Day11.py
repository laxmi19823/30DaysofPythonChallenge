from datetime import datetime

# Get user input for both dates
date1_str = input("Enter the first date (DD-MM-YYYY): ")
date2_str = input("Enter the second date (DD-MM-YYYY): ")

# Convert string to datetime objects
date1 = datetime.strptime(date1_str, "%d-%m-%Y")
date2 = datetime.strptime(date2_str, "%d-%m-%Y")

# Calculate difference in days
difference = abs((date1 - date2).days)

print(f"\nNumber of days between {date1_str} and {date2_str} is: {difference} days")
