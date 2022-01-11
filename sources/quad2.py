# ax**2 + bx + c = 0

#import complex math
import cmath

#user input
a = float(input("a?"))
b = float(input("b?"))
c = float(input("c?"))

# discriminant
delta = (b**2) - (4*a*c)

# quadratic formula
r1 = (-b-cmath.sqrt(delta))/(2*a)
r2 = (-b+cmath.sqrt(delta))/(2*a)

# result
print(f"The roots are {r1} and {r2}. ") 
