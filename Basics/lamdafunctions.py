'''
Lambda Functions are Small Anonymous functions defined using the lambda keyword.
They can have any number of Arguments but only one expression 
Syntax - lambda arguments: expression

Lambda is normally used when you need a small, simple function for a short time. 

'''

# A Normal Function 
def add(a, b):
    return a + b  

#The Above function With the LAMBDA
add= lambda a,b: a+b

#Ex:1 - Create a lambda that returns the square of a number.
square= lambda a:a*a

print("Square :",square(10))

#Ex:2 - Create a lambda that adds two numbers.
add_numbers= lambda a,b:a+b

print("Add two Numbers ",add_numbers(80,10))

#Ex:3 Create a lambda that checks whether a number is even.
even_number= lambda a:  a%2 == 0 

print("Even_number:",even_number(5))

#Ex:4 Square of Each Number in the List 
numbers=[1,2,3,4,5]

#With the Normal Loops
for i in numbers:
    print( i**2 )
#With the list And the map 
new_squarednum=list(map(lambda x:x**2,numbers))
#For filter
filter_evn=list(filter(lambda x:x%2==0,numbers))
print(filter_evn)

#Ex:5 Create a lambda that returns the larger of two numbers.
larger_of_twonumbers=lambda a,b: a if a>b else b  
print("Larger of two numbers :",larger_of_twonumbers(10,20)) 