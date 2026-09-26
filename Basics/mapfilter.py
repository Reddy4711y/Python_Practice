# Map And Filter 
'''
map() -   This Map function Transform each item
filter() - This Filter function Keep/remove items(filter() checks every item → keeps the items that satisfy the condition.)

NOTE - map()    →  same count,  different values

filter() →  same values, fewer count

'''

# map()

#Apply this function to each item, give me a new list.
numbers = [2,3,4,5,6,7,8]
def square_item(item):
  return item*item
result=list(map(square_item,numbers))
print(result)

#If We Will use the Lambda Function 
result_with_lambda=list(map(lambda item:item**2, numbers))
print(result_with_lambda)


# Actually map is the Iterator  if Once COnsumed then Next one Dont have the chance
iterations=map(lambda a:a**2,numbers)
print("First Time using the Iteration:",list(iterations)) # [4, 9, 16, 25, 36, 49, 64]
print("Second Time using the Iteration:",list(iterations)) # [] -> Because the iterator was already consumed. 


'''
It stores/retains the iterator state and references needed to produce the values, not all the calculated results.
map(...)
   │
   ├── function → lambda a: a**2
   │
   ├── input → numbers
   │
   └── current position → 0
   '''

#Filter 

def remove_odd(number):
  return number%2 == 0

remove_odd_filter=list(filter(remove_odd,numbers))
print("Remove odd Filter -",remove_odd_filter)

remove_odd_filter_lambda=list(filter(lambda item:item%2==0,numbers))
print("Remove odd filter Lambda Elements -",remove_odd_filter_lambda)