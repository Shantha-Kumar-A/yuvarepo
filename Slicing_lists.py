my_list = [0,1,2,3,4,5,6,7,8,9]

print(my_list[1:8:2])
print(my_list[::-1]) #steps the value by -1 which means in the reverse order

S = "https://google.com"

print(S[-4:])
print(S[8:])
print(S[::2]) #steps the value by 2


# Python program to convert time 
# from 12 hour to 24 hour format 
  
# Function to convert the date format 
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        print(str1[:2])
        return "00" + str1[2:-2] 
        
    # remove the AM     
    elif str1[-2:] == "AM": 
        print(str1[-2:])
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        print(str1[:2])
        return str1[:-2] 
          
    else: 
        print(1)  
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
  
# Driver Code         
print(convert24("12:00:00 AM")) 

for i in range(-1,6,2):
	print(i)