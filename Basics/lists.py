'''
- Lists Are Ordered ,Mutable Collection of Items .
- They Can Contain of Items Different Data Types 
- List Syntax - []
'''
names=['Hemanth','reddy']
print(names)


mixed_elements=[1,2,3,"Toby"]
print(mixed_elements)

#Accessing the Lists
print(mixed_elements[1])  # 1 is the index 
print(mixed_elements[1:3])  
print(mixed_elements[-1])  
print(mixed_elements[:-1])  
print(mixed_elements[::3]) 

#Lists Methods 
names.append("Apple")  # Add the Element At the End 
print(names)
names.insert(1,"In IndexOne") # Add the Element based on Specified Index
print(names)
names.append('reddy')
names.remove('reddy') # It Will remove the first occurance of the Element (ex : reddy two times repeat now first one Will be removed )
print(names)


remove_last_element=names.pop()  #Remove And return the Last Element 
print(remove_last_element)
get_index=names.index('Hemanth') #It Will Give the index of An element 
print(get_index)
get_frequency=names.count('Apple') #It Will return the Count how many times it Will There in the List 
print(get_frequency)

names.sort() #Sort the Elements in the List in Ascending Order
print(names)
names.reverse() #Reverse the List 
print(names)
names.clear() # remove All the Elements In the List 
print(names)