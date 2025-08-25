d = {'red':2, 'black':2, 'green':1, "orange":1, 'pink':None, 'yellow':3,'black': 1}



for k,v in d.items():
    if v is not None:
        print(k,v,end= ' ')
        
