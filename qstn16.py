employees={}
n=int(input("enter the number of elements:"))
for i in range(3):
    name=input("enter the name of employee:")
    salary=input("enter employee's salary:")
    employees[name]=salary
l=list(employees.items())
l.sort()
print('Ascending order is ',l)
l.sort(reverse=true)
print('desending order is',l)
dict=dict(l)
print(dict)
