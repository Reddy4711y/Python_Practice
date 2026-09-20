'''
- Tuples Are Ordered Collection of Items 
- Tuples Are immutable 
- Tuple Syntax - ()
'''

tuple_example=("Hemanth",2,3,"Reddy")
print(tuple_example)
print(tuple_example[2])
print(tuple_example+tuple_example)
print(tuple_example*4)

for i in tuple_example:
  print(i)

# tuple_example[1]='redd'  This Will Not Support item Assignment Because tuples Are Immutable 

# tuple Methods 
print(tuple_example.count('Hemanth'))
print(tuple_example.index("Reddy"))

# packing And unpacking tuple 
packing_tuple =1,2,"Hemanth"
print(packing_tuple)
a,b,c=packing_tuple
print(a)
a,*c=packing_tuple
print(c)

# Nested Tuples 
nested_tuples =((1,2,4,"Reddy"),("Hi","Hemanth",1000))
for i in nested_tuples:
  for j in i:
    print(j,"--")