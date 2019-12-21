open_tup = tuple('({[') 
close_tup = tuple(')}]') 
map = dict(zip(open_tup, close_tup))
print(map)

# Python3 code to Check for  
# balanced parentheses in an expression 
def check(expression): 
      
    open_tup = tuple('({[') 
    close_tup = tuple(')}]') 
    map = dict(zip(open_tup, close_tup)) 
    queue = [] 
  
    for i in expression:
        if i in open_tup: 
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    return "Balanced"
  
# Driver code 
string = "{[]{()}}]"
print(string, "-", check(string)) 
