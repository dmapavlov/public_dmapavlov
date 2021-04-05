import datetime


user_date = input().split()
user_days = int(input())


our_date = datetime.date(int(user_date[0]), int(user_date[1]), int(user_date[2]))
delta = datetime.timedelta(days=user_days)
data = our_date + delta
print(data.year, data.month, data.day)
