num = int(input("Enter number: "))

def double(num):
    if abs(num) > 17:
        return (abs(num) - 17)*2
    else:
        return num

print("The number is: "+ str(double(num)))