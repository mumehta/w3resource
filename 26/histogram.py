s = input("Enter list of numbers (without comma): ")
n = [int(n) for n in s.split(" ")]
histogram_character = input("Histogram characher (single character, e.g. . (dot)): ")

def draw_histogram(num_list, histogram_character):
    for n in num_list:
        print(histogram_character*n)

draw_histogram(n, histogram_character)
