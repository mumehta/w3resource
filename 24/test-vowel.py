def test_vowel(c):
    return "vowel" if c.lower() in ['a','e','i','o','u'] else "consonent"

char = input("Enter any character: ")
print("The entered character %s is: %s" % (char, test_vowel(char)))