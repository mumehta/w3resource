from datetime import date
date1 = date(2014, 7, 2)
date2 = date(2021, 7, 11)

print("Days between %s and %s are: " % (date1.strftime("%x"), date2.strftime("%x")))
print(date2 - date1)