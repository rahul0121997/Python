# find the compound intrest

def compound_intrest(principal, rate, time):
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    return ci

res = compound_intrest(10000,10.25,5)
print(res)