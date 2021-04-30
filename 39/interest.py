def compound_interest(p, r, t):
    return p * pow(( 1 + r/100 ), t)

amt, interest, time = 10000, 3.5, 7
print(compound_interest(amt, interest, time))