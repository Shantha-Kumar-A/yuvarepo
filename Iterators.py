#sample iterator using inbuilt keywords

nums = [1,2,3,4,5]

n = iter(nums)
for i in nums:
    
   print(i)

#creating our own iterator

class Topten():

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = Topten()

print(next(values))

for i in values:
    print(i)
