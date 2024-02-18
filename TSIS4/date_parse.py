from datetime import datetime, timedelta

def subtract_days_from_current_date(days):
    current_date = datetime.now()
    subtracted_date = current_date - timedelta(days=days)
    return subtracted_date


result_date = subtract_days_from_current_date(5)
print("Current date:", datetime.now().strftime("%Y-%m-%d"))
print( result_date.strftime("%Y-%m-%d"))



def get_date_info():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    return yesterday, today, tomorrow


yesterday, today, tomorrow = get_date_info()
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))



def drop_microseconds(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


current_datetime = datetime.now()
datetime_without_microseconds = drop_microseconds(current_datetime)
print("Datetime with microseconds:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)




def date_difference_in_seconds(date1, date2):
    difference = date2 - date1
    difference_seconds = difference.total_seconds()
    return abs(difference_seconds)  


date_format = "%Y-%m-%d %H:%M:%S"
date_str1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference between the two dates in seconds:", difference_seconds)