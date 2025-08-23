from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date(no_of_days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=no_of_days)
    return future_date
    
def main():
    display_current_datetime()
    no_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(no_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()