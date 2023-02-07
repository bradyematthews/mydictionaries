# 1) print out the value for the key 'history' using the dictionary below


sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

# sampleDict only has 1 key ('Class'). The value of 'Class' is another dictionary (Everything after it). That dictionary has 1 key as well ('Student')
# 'Studnet" has 2 keys ("name" and "Marks")
score = sampleDict["class"]["student"]['marks']['history']
print(score)


# 2) Add 2 inches to the son's height. (If you have a question like this, make sure you don't hardcode it. It says add, not set)

dict={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}

# My answer (I did it wrong because I hardcoded it.)
# dict["son's height"] = "34"
# print(dict)

# Correct way from Professor B
dict["son's height"] += 2

print(dict)


# 3) Given a Python dictionary, Change Brad’s salary to 8500 (hardcode this value directly opposed to do a calculation)

sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

# My answer
# sampleDict['emp3'['salary']] = 

#Correct answer from professor B
sampleDict["emp3"]['salary'] = 8500
print(sampleDict)



# 4 )Given the dictionary below, add a new key - 'work' with the values shown below:
#       "work": ["Apology", "Phaedo", "Republic", "Symposium"]

dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

# My answer
dict['work'] = ["Apology", "Phaedo", "Republic", "Symposium"]

# Correct answer from professor B
dict['work'] = ["Apology", "Phaedo", "Republic", "Symposium"]

print(dict)

