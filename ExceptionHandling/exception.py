'''
- Exception handling Allows you to handle the Erros Gracefully
- Exceptions are Events that disrupt the normal flow of a program .
'''

try:
  a=b
except:
 print("Some Variable is not defined")

try:
  a=b
except NameError as name:
  print(name)

try:
  result=1/0
except ZeroDivisionError as zero:
  print(zero)

try:
  a=1/0
except Exception as parent_exception:
  print("This Exception class is parent_exception - ",parent_exception)

#file with Exception handling 
try:
  with open('anyname.txt','r') as file:
    file.read()
except Exception as parent_exception:
  print(parent_exception)

