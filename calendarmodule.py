# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar


month, day, year = map(int, input().split())


day_index = calendar.weekday(year, month, day)


print(calendar.day_name[day_index].upper())
