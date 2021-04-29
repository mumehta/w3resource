num = int(input("Enter test value"))
l = list(range(10))

def test_presence(num, lst):
    return "present" if num in lst else "not present"

print("The num %i is %s in %s" % (num, test_presence(num, l), str(l).strip('[]')))