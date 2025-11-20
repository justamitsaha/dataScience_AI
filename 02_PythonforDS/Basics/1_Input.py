import sys
#REPL Read Evaluate Print Loop  
x = input("Enter 1st number: ")    
y = input("Enter 2nd number: ")
print(type(x))
x = int(x)
y = int(y)
z = x+y;
print(z)

c = input('Enter charecter: ')
print(c[0])
#or
c = input('Enter charecter: ')[0]
print(c)

result= eval(input("Enter an expression: "))
print(result)

#assign values from arguments passed 
# index 0 is for file name so arguments starts from 1
# example  & C:/Amit/Imp/python-3.13.7-embed-amd64/python.exe c:/Amit/workspace/Java/dataScience_AI/02_PythonforDS/0_Basics.py 7 9
x = sys.argv[1]
y = sys.argv[2]
print(int(x) *int(y))

print(dir())