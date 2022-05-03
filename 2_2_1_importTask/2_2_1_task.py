import datetime

yyyy, mm, dd = map(int, input().split())
input_date = datetime.date(yyyy, mm, dd)
delta = datetime.timedelta(days=float(input()))

result_date = input_date + delta
print('{} {} {}'.format(result_date.year, result_date.month, result_date.day))