f = open("MyData.txt",'r')

#print(f.readline())
#print(f.readline())

f1 = open("TestData.txt",'w')

for data in f:
    f1.write(data)

f2 = open("DSC_0014.JPG",'rb')

p1 = open("Mypic.JPG",'wb')

for i in f2:
    p1.write(i)
    
