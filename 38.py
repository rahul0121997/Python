from collections import Counter
lst = [1, 2, 3, 1, 2, 1, 4, 5,5,5,5,1,1,1,1,1,1]

d = {}

# for i in lst:
#     d[i] = d.get(i, 0) + 1  

# res = max(d.items(), key=lambda x : x[1])
# print(res)

# data = [(k,v) for k,v in d.items()]

# data.sort(reverse = True)
# print(data[0])  


# using counter 
c = Counter(lst)

print(c.most_common(1))

#using element method of counter

s = Counter(a=2, b=3)
print(tuple(s.elements()))