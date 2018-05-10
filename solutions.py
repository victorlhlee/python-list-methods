#List methods allow you to modify lists. The following are list methods for you to practice with.

#append(element) adds a single element to the list
#1. Fu Sheng is also deserving to be in the Kung Fu Legends list. Add him in and print your results.

kungfu_legends = ['Bruce Lee', 'Jackie Chan', 'Jet Li', 'Donnie Yen']

kungfu_legends.append('Fu Sheng')
print(kungfu_legends)

#insert (index, element) adds a new element at any position in your list.
#2. I just bought a pair of Vivo shoes! Please add Vivo to my kicks list and print the results.

kicks_list = ['Nike', 'Adidas', 'Vans', 'Pro-Keds', 'slippahs']

kicks_list.insert(2, 'Vivo')
print(kicks_list)

#remove(element) removes a single element from the list
#3. I am allergic to cats and hence not a big cat lover. Help me remove cats from the list below.

fav_pets = ['pugs', 'ducks', 'pigs', 'cats', 'goats', 'giraffes']

fav_pets.remove('cats')
print(fav_pets)

#pop(index) removes the element at the given index position
#4. I love me some chocolate but hate coconuts. Remove Almond Joy from the list below.

candy = ['Kit Kat', 'Twix', 'Reese Peanut Butter Cups', 'Almond Joy', 'M&Ms', 'Snickers', 'Hersheys']

candy.pop(3)
print(candy)

#extend(list) adds elements from another list 
#5. Your significant other just gave you a new RSVP list to add into your list. Add the new list and print your results.

party_list = ['Snoop', 'Drake', 'Rihanna', 'Ed Sheeran', 'Migos']
new_rsvp = ['Bruce', 'Fu Sheng', 'Khalid']

party_list.extend(new_rsvp)
print(party_list)

#index(element) searches an element in the list and returns its index
#6. Find the index position of Grimace from the mcdonalds list below and print your result.

mcdonalds = ['Ronald', 'Mayor McCheese', 'Hamburglar', 'Officer Big Mac', 'Grimace', 'Birdie the Early Bird', 'Fry Kids', "Uncle O'Grimacey" ]

grimace_pos = mcdonalds.index('Grimace')
print(grimace_pos)

#count(element) counts how many times an element is in a list
#7. Find how many 'wish' are in the list below and print your result.

wishful = ['I', 'wish', 'to', 'wish', 'the', 'wish', 'you', 'wish', 'to', 'wish', 'but', 'if', 'you', 'wish', 'the', 'wish', 'the', 'witch', 'wishes', 'I', 'wont', 'wish', 'the', 'wish', 'you', 'wish', 'to', 'wish']

wish_count = wishful.count('wish')
print(wish_count)

#reverse() reverses the elements of a given list
#8. Use the force, or in this case the reverse method to help Yoda make some sense with his motivational talk to the young Jedi interns.*/

yoda = ['try', 'no', 'is', 'there', 'not', 'do', 'or', 'do']

yoda.reverse()
print(yoda)