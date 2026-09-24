'''
- Dictionaries Are Unordered Collection of Items .
- They Stored the Data in Key Value Pairs 
- Key Must Be Unique And Immutable (EG:Strings , Numbers or Tuples ) but
  Values Can be of Any Type 
- Syntax is  - {} 
'''

dict={1:"I am Hemanth","age":24,4:"Anything"}
print(dict[1])
print(dict.get(1))
print(dict.get(4,"Nothing")) #The 4 Key is not there then the Fallback is the Nothing
dict['dogname']="Toby" # If the Key is not there It Will Add
dict[1]="I am hemanth reddy" #If the Key is There It Will Update 
print(dict)

# Deleting A Key 
del dict["dogname"]
print(dict)


# Methods 
print(dict.keys())
print(dict.values())
print(dict.items())

# Merge Two Dictionaries  
dict_1={1:'Hemanth',3:4}
dict_2={2:'Reddy',3:5}
merge_dict={**dict_1,**dict_2}
print(merge_dict)

dict_test={"first_name":"Hemanth","last_name":"Reddy"}
for i in dict_test:
  print(i,dict_test[i])

nested_dict={"details":{"name":"hemanth"},"additional_details":{"age":24,'gender':"male"}}
for i in nested_dict:
  print("Parent-",i)
  for final_object in nested_dict[i]:
    print("Final-",final_object)