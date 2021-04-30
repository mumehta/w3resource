def make_decision(num1, num2):
    return True if num1 == num2 or num1 + num2 == 5 or num1 - num2 == 5 else False

print(make_decision(1,2))
print(make_decision(2,2))
print(make_decision(2,3))
print(make_decision(18,13))
print(make_decision(20,30))
