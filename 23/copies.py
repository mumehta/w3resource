def char_copies(string, repeat):
    return string * repeat if len(string) < 2 else string[:2] * repeat

st = input("Enter any string: ")
repeat = int(input("Enter repeatition type: "))
print(char_copies(st, repeat))