'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''



import json

infile = open("eq_data.json", "r") # "Error: No such file or dictionary: 'eq_data.json'" --> Problem fixed: Had to add both the py and json file to mydictionaries folder.

earthquakes = json.load(infile)

# 1) Print out the number of earthquakes
#print(type(earthquakes))
print("1)")
print()
# I tried doing   print(len(earthquakes))     but that showed 4, which was the 4 main categories (type, metadata, features, bbox)
# I then tried to call the metadata category and then call the "count" line in that category, but couldn't figure out how to do that.
   # #print(earthquakes["metadata"]["count"]) --> This did not work.
# Next, I figured that since the only category that held info for all earthquakes was 'features', I'd have to call into that one. To do that, I just found how many earthquakes were in the 'features' category.
print("Number of earthquakes:", len(earthquakes["features"]))
print()

# 2) Iterate through the dictionary and extract the location, magnitude, longitude and latitude of the location and put it in a
#    new dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a magnitude > 6. Print out the new dictionary.
#for earthquake in earthquakes:
   #if earthquake['mag'] in earthquakes > 6: 
               # --> MAGNITUDE must be > 6, not just earthquake in earthquakes
      #print(f"Location: {earthquake['place']}")
      #print(f"Magnitude: {earthquake['mag']}")
      #print(f"Longitude: {earthquake['cordinates']}") # 'cordinates(0)
      #print(f"Latitude: {earthquake['cordinates']}") # cordinates(1)

a = 1
eq_dict = {}


print("2)")
print()
#Test Run
#for earthquake in earthquakes["features"]:
   #if earthquake["properties"]["mag"] > 6:
      #eq_dict = {
      #((earthquake["properties"]["place"])): {
      #"Magnitude:", ((earthquake["properties"]["mag"])), 
      #"Longitude:", ((earthquake["geometry"]["coordinates"][0])),
      #"Latitude:", ((earthquake["geometry"]["coordinates"][1]))}
      #}
      
      #print(eq_dict)
#Original
for earthquake in earthquakes["features"]:
   if earthquake["properties"]["mag"] > 6:

      eq_dict[a] = [
         earthquake["properties"]["place"],
         earthquake["properties"]["mag"],
         earthquake["geometry"]["coordinates"][0],
         earthquake["geometry"]["coordinates"][1],
      ]

      a += 1

print(eq_dict)

# 3) Using the eq_dictionary, print out the information as shown below (first three shown):
print()
print("3)")
print()

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

for element in list1:
   print("Location:", eq_dict[element][0])
   print("Magnitude:", eq_dict[element][1])
   print("Longitude:", eq_dict[element][2])
   print("Latitude:", eq_dict[element][3])
   print()

"""
# Notes in class
person = {}

person[f'name'] = 'John'
person[f'name'] = 'Jack'

print(person)
# Only prints last line when you run this. Jack replaced John because the key is the same.

eqdata = {}

eqdata['location'] = 'Chile'
eqdata['location'] = 'Texas'

print(eqdata)
# This does the same thing.

eqdata = {}
for earthquake in list_of_eqs:
   location = eq['location']
   eqdata[eq[location]] = {'mag': ___, 'lat':___, 'lon':___}
# EQ[loaction] will give you Chile. Don't hardcode location in the new dictionary. 
print(eqdata)

"""