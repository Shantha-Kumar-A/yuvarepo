av = 5
x = int(input("Enter the number of candies you want"))
i = 1

while i <= x:
    if i > av:
        print
        break
        
    print("CANDY")
    i += 1    

print("Bye")

for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)

print("Bye")

for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)
print('Bye')
