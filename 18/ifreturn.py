def fun(num1, num2, num3):
    if num1 == num2 == num3:
        return 3*3*num1
    else:
        return num1 + num2 + num3

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

print("Your answer is: %i " % fun(num1, num2, num3))