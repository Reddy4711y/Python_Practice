'''
- Functions is a Block of Code that performs a Specific task and mainly
  help to Organizing code ,reusing code And Improving the Readability
- def Keyword = To Define a Function 
'''

def add_numbers(numbers):
  a=0
  for i  in numbers:
    a+=i
  return a;

print(add_numbers([2,3,4,5,6]))

# Fallback Parameters  - If we cant pass any Argument then Default We Will Set One Parameter 

def fallback_param_demo(name="Reddy"):
  print(f"Hi {name} . Welcome to the Top 1%")

fallback_param_demo("Hemanth") # Here We Are Passing the Argument So it Will Ignore fallback
fallback_param_demo() #Here We cant pass Any argument So the fallback will taken

'''
Positional Arguments And Keyword Arguments 
- For the Positional Arguments they Dont Have the Key value Pairs 
- For the Keyword Arguments they have the key value Pairs 
'''

#Positional Arguments 

def positional_arg_demo(*args):
  for i in args:
    print ("Positional Args ",i)

positional_arg_demo(1,2,3,4,5,6,7,8,9,10) #These Are the Positional Arguments 

#Keyword Arguments 
def keyword_arg_demo(**kwargs):
  for key,value in kwargs.items():
    print("Keyword Args ",key," ",value)

keyword_arg_demo(name="Hemanth Reddy",age=24)