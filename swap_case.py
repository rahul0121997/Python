def swap_case(s):
    swap = ''.join(x.upper() if x.islower() else x.lower() for x in s) 
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
