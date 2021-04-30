def sum(num1, num2, num3):
    if num1 == num2 or num2 == num3 or num3 == num1:
        return 0
    else:
        return num1 + num2 + num3

print(sum(2, 3, 4))
print(sum(3, 3, 4))