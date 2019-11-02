a = 5
b = 3

try:
    print("Resource Open")    
    print(a/b)
    k = int(input("Enter a number here:"))
    print(k)
    
except ZeroDivisionError as z:
    print("Enter a valid divisor",z)
except ValueError as v:
    print("Invalid number",v)
except Exception as e:
    print("Something went wrong",e)

finally:
    print("Resource Closed")
