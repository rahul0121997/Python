principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("enter the principle: ")) 
    if principle <= 0:
        print("principle can't be zero or less than")

while rate <= 0:
    rate = float(input("enter the rate: ")) 
    if rate <= 0:
        print("rate can't be zero or less than")

while time <= 0:
    time = float(input("enter the time: ")) 
    if time <= 0:
        print("time can't be zero or less than")

total = principle * pow((1 + rate/100),time)
print(total)