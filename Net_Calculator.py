def calculate_usage():
    # Constants
    monthly_quota = 250  # Total monthly data in GB
    total_days_in_month = 30  # Total days in the month

    # User input
    data_used = float(input("Enter the amount of data used so far (in GB): "))
    data_left = float(input("Enter the amount of data left (in GB): "))
    days_left = int(input("Enter the number of days left in the month: "))

    # Calculate total data used
    total_data_used = data_used + data_left

    # Calculate daily allowance
    daily_allowance = monthly_quota / total_days_in_month

    # Calculate average daily usage so far
    average_daily_usage = data_used / (total_days_in_month - days_left)

    # Calculate total allowance for the remaining days
    total_remaining_allowance = daily_allowance * days_left

    # Calculate the remaining balance
    remaining_balance = data_left - total_remaining_allowance

    # Check if the user has exceeded their daily allowance
    if average_daily_usage > daily_allowance:
        print(f"You have exceeded your daily allowance of {daily_allowance:.2f} GB/day.")
    else:
        print(f"You are within your daily allowance of {daily_allowance:.2f} GB/day.")

    # Check remaining balance
    if remaining_balance < 0:
        print(f"You will exceed your quota by {-remaining_balance:.2f} GB.")
    else:
        print(f"You have an extra {remaining_balance:.2f} GB left.")

if __name__ == "__main__":
    calculate_usage()
