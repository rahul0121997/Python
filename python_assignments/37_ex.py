# Two lists
countries = ['India', 'Japan', 'Germany']
capitals = ['New Delhi', 'Tokyo', 'Berlin']

# Merge using a loop
country_dict = {}
for i in range(len(countries)):
    country_dict[countries[i]] = capitals[i]

print("Country-Capital Dictionary:", country_dict)
