row = 5

for i in range(row):
     print("*" * i + " " * 2*(row - i) +"*" * i)

for i in range(row, 0,-1):
     print("*" * i + " " * 2 *(row - i) + "*" * i)

for i in range(row):
     print(" " *(row - i) + "* " * i)

for i in range(row , 0 ,-1):
     print(" " *(row - i) + "* " * i)