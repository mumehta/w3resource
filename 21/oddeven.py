num = int(input("Enter number: "))
def odd_or_even(num):
    return "even" if num%2==0 else "odd"

print("The number is: %s" % odd_or_even(num))