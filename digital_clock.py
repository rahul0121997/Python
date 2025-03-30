import time
my_time = int(input("enter the time in seconds: "))

for x in reversed(range(0,my_time)):
    second = x % 60
    min = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"{hour:02}:{min:02}:{second:02}")
    time.sleep(1)
