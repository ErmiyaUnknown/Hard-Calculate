import math

def op(x):
            
    expr1 = (x ** 5/3) + math.tan(math.radians(x))
    expr2 = 3.14 ** 2 + math.tan(math.radians(math.sin(x)**2)) ** -1

    result = math.gcd(int(expr1), int(expr2))

    print(result)
 
            
try:
    
    while True:
        x = int(input("Enter 'x': "))

        if x == 0:
            break
         
        else:
            op(x) 

except:
    print("Error x must be integer!")   