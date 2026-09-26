import math  # Normal Way of Import 
print(math.sqrt(10))

from math import sqrt,pi  #Some other Way of Import 
print("Square Root - ",sqrt(2))
print("Pi value - ",pi)

import math as mathoo #Using Alisases 
print("mathoo Pi -",mathoo.pi)

from math import *  # Without specifying Any methods it Will Automatically Will use every method in the math if We Specify the * 
print(sqrt(3))
print(pi)


# Custom packages Usage 
import custom_packages.add as any_name_cheechu
print("Custom Add Package - ",any_name_cheechu.add_numbers(10,90))