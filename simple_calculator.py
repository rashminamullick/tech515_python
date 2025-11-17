#what is a module
#smallest piece of software in Python
#single file

import maths_operations
#Mini-calculator



first_num = int(input("Enter the first number: "))
second_num: int = int(input("Enter the second number: "))
result = maths_operations.add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")