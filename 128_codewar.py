def XO(s1):
    s = s1.lower()
    x_count = s.count('x')
    o_count = s.count('o')
    
       
    if x_count == o_count :
        return True
    elif x_count == 0 and o_count == 0:
        return True
    else:
        return False
        
print(XO('ooxXm'))