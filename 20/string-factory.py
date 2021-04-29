def string_factory(string, repeat):
    return string*repeat

s = input("Enter any string: ")
r = int(input("Repeat string times: "))
print(string_factory(s,r))