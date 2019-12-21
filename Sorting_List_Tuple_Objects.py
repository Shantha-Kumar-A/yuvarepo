li = [9,7,4,5,6,3,2,8,1]

s_li = sorted(li,reverse=True)

print('Sorted List:\t',s_li)

li.sort(reverse=True)

print('Original List:\t',li)

tup = (9,7,4,5,6,3,2,8,1)

s_tup = sorted(tup)

print('Sorted Tuple:\t',s_tup)

di = {'name':'Yuvaraj','job':'Programming','age':25,'os':'Windows'}
s_di = sorted(di)
print('Sorted Dict\t',s_di)

li = [-5,-9,-8,1,4,5,7]

s_li = sorted(li,key=abs)

print(s_li)

class Employee():
	def __init__(self,name,age,salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('Yuvi',25,10000)
e2 = Employee('Mohan',25,11000)
e3 = Employee('Aswin',24,12000)

emp_list = [e1,e2,e3]

def e_sort(emp):
	return emp.salary
	#return emp.age
	#return emp.name

from operator import attrgetter

# s_emp_list = sorted(emp_list,key=e_sort,reverse=True)

# s_emp_list = sorted(emp_list,key=lambda e: e.name)

s_emp_list = sorted(emp_list,key=attrgetter('age'))

print(s_emp_list)
