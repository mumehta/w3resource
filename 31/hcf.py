import math
from collections import Counter

def all_factors(num):
    l = list()
    for i in range(1, num+1):
        if num % i == 0:
            l.append(i)
    return l

def factors(num):
    orig_num = num
    l = list()
    l.append(1)
    i = 2
    while num > 1:
        if num % i == 0:
            num = num/i
            l.append(i)
            continue
        else:
            i += 1
    print("Factor of %i are %s" % (orig_num, l))
    return l

def highest_common_factor(numbers):
    c = list()
    for num in numbers:
        f1 = factors(num)
        c.append(Counter(f1))
    cnt = Counter()
    for i, c1 in enumerate(c, start=1):
        if i == 1:
            cnt = c1
        cnt = cnt & c1
    l = list(cnt.elements())
    return math.prod(l)


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("Highest common factor of %i and %i is %i" % (n1, n2, highest_common_factor([n1, n2])))