num = int(input("Enter number: "))

if num < 100:
    print("Number less then 100")
elif num >= 100 and num < 1000:
    print("Number between 100 and 1000")
elif num >= 1000 and num < 2000:
    print("Number between 1000 and 2000")
else:
    print("Number is 2000 or more")