t = ['apple', 'banana', 'cherry',123, 45, 67,'true', False, None, [1,2,3], {'a':1, 'b':2}]
print(t,type(t))
t = tuple(t)
print(t, type(t))

t1 = ('apple', 'banana', 'cherry',123, 45, 67,'true', False, None, [1,2,3], {'a':1, 'b':2})
t2 = (1,2,3,4,5)

t_concat = t1 + t2
print(t_concat, type(t_concat))
print(t_concat[0])
print(t_concat[1])
print(t_concat[2])
print(t_concat[3])
print(t_concat[0:5:2])
print(t_concat[::-1])
print(t_concat[-2])

