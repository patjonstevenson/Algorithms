# Write a function power() that given value a and exponent b will compute 
# a^b. It would be silly to have the function say return a^b.

def power(a, b):
    result = 1
    for i in range(0, b):
        result *= a
    return result


def rec_power(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return rec_power(a, b+1) / a
    else:
        return a * rec_power(a, b-1)

