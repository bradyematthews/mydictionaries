import random

phonebook ={}
phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

#Keys are the names of the individuals. Values are the corresponding phone numbers. There are 3 key-pairs.


print()
print('*****  start section 1 - print dictionary ********')
print()

mydictionary = dict(m=8, n=9)
print(mydictionary)

print(len(phonebook))       #Tells you the dictionary length
print(type(phonebook))      #Tells you the dictionary type




print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()
name = "Chris"


#phone = phonebook['Chris']
#print(phone)
#or (36-37) or (39)
print(phonebook['Chris'])



if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")


print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Chris'] = "555-0123"     #Updated Chris' phone number
phonebook['Joe'] = "555-4444"       #Joe is not in original phonebook, this appended him into it

print(phonebook)



print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)

del phonebook['Chris']      #Will only delete if it finds the match, if not it doesn't delete anything

print(phonebook)




print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for k in phonebook:
    print(f"the key is {k} and the value is {phonebook[k]}")      #Iterates through the keys, not the values. To get the corresponding values in that spot, give the dictionary the key and you get back the phone number
# How do you get the phone number? You call the dictionary (phonebook) and give it the key
#What you use for your iterator "k" is irrelevant as long as you use the consistent, same one

for value in phonebook.values():    #  .values method allows you to cycle/iterate through just the values side
    print(value)

for k,v in phonebook.items():
    print(f"the key is {k} and the value is {value}")


for ph_tuple in phonebook.items(): #  .items method gives you both the key and the value
    print(ph_tuple)



print()
print('*****  end section 5 ********')
print()




print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('chris', '999') # Giev it a default value just incase no match is found. You avoid the key and value errors
print(phone)

phonebook.clear() # .clear Clears out all the elements in your dictionary but does not delete the elements
print(phone)


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

remove = phonebook.pop('Chris', 'not found') #Also has a default method
print(remove)
print(phonebook)    #Pop takes out key-value pair from dictionary



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#Supposed to work using the random module. Picks random key value pair and pops it out of the dictionary for you. The random doesn't work, only the popping works.
a = phonebook.popitem()

print(a)
print(phonebook)



print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

phonebook_list = list(phonebook) #Using list function on a dictionary, the default option is always going to be the key.
print(phonebook_list) #Gives list of the keys. 
random_key = random.choice(phonebook_list)
print(random_key)
 #This random.choice method only works on lists
print(phonebook[random_key])


#Print the same thing as right above but in one line of code, eliminate variable names when they aren't needed
#print(list(phonebook), phonebook[random_key]) #My attempt in class
print(phonebook[random.choice(list(phonebook))]) #Right way to do it in class

print()
print('*****  end section 9 ********')
print()








