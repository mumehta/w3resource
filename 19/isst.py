def formatted_is_string(s):
  if len(s) >= 2 and s[:2] == "Is":
    return s
  else:
    return "Is" + s

s = input("Enter anything: ")
print("The Is String is: %s" % (formatted_is_string(s)))