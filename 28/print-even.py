numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

numbers1 = [54,76,29,478,4958,6,0,34, 91]    

def print_even(numbers):
    for n in numbers:
        if n > 237:
            break
        else:
            if n%2==0:
                print(n)
        


print_even(numbers1)

