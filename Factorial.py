def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f

x = 5

result = fact(x)
print(result)

#fact with recursion

def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n-1)
result1 = fact_rec(x)
print(result1)
