fruits =     ["apple","banana","cherry","mango"]
vegetables = ["potato","tomoto","radish"]
meat =       ["chicken","fish","turkey"]

# fruits = ("apple","banana","cherry","mango","apple")
# vegetables = ("potato","tomoto","radish")
# meat = ("chicken","fish","turkey")



# food = [fruits,vegetables,meat]
# print(food[1][1])

food = [["apple","banana","cherry","mango"],
        ["potato","tomoto","radish"],
        ["chicken","fish","turkey"]]

for fruit  in food:
    for item in fruit:
        print(item, end = " ")

#2d collection with nested loop to print number pad

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))