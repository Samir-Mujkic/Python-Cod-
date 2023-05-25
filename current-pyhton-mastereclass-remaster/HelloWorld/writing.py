#cities = ["Adelaide", "Alice Spirngs", "Darwin", "Melbourne", "Sydney"]

#with open("cities.txt", "w") as city_file:
 #   for city in cities:
 #       print(city, file=city_file)

#cities = []

#with open("cities.txt", "r") as city_file:
#    for city in city_file:
 #        cities.append(city)

#print(cities)
#for city in cities:
 #   print(city)

citiess = ["Aldelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("citiess.txt", "r") as city_file:
    for city in city_file:
        citiess.append(city)

print(citiess)
for city in citiess:
    print(city)