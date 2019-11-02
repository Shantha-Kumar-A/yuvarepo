def fib(num):
    a = 0
    b = 1
    if num <= 0:
        print("Enter a number greater than zero")
    elif num == 1:
            print(a)
    else:
         print(a,end=" ")
         print(b,end=" ")
         for i in range(2,num):
             c = a + b
             a = b
             b = c
             print(c ,end=" ")

x = 6
fib(x)
print("") #to begin with new line
def fib_lim(num):
    a = 0
    b = 1
    if num <= 0:
        print("Enter a number greater than zero")
    elif num == 1:
            print(a)
    else:
         print(a,end=" ")
         print(b,end=" ")
         for i in range(2,num):
             c = a + b
             if c >= num:
                 break
             else:
                 a = b
                 b = c
                 print(c ,end=" ")
			 
fib_lim(50)
