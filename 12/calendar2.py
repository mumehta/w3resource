import calendar

month = int(input("Enter month: "))
year = int(input("Enter year: "))

print("The calendar for %s/%s is: " % ( month, year ))

calendar.prmonth(year, month)
c = calendar.TextCalendar(firstweekday=0)
c.prmonth(theyear=year, themonth=month)