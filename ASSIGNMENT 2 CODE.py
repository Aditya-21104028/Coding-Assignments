#ASSIGNMENT 2

#......................QUESTION 1.......................

print('ANSWER 1')

input_str ='Python is a case sensitive language'


#part (a)
print('(a): ', len(input_str))

#part (b)
print('(b): ', input_str[::-1])

#part (c)
new_str =input_str[slice(10,27)]
print('(c): ', new_str)

#part (d)
print('(d): ', input_str.replace('a case sensitive', 'object oriented'))

#part (e)
print('(e): ', input_str.index('a'))

#part (f)
print('(f): ', input_str.replace(' ', ''))
print('\n')


#.......................QUESTION 2......................

print('ANSWER 2')

name='Aditya Kumar'
sid='21104028'
department='Electrical Engineering'
cgpa='9.9'

print('Hey,',name,'Here!','\nMy SID is',sid,'\nI am from', department,'department and my CGPA is',cgpa)
print('\n')


#.......................QUESTION 3......................

print('ANSWER 3')

a=56
b=10

print('(a): ', a&b)
print('(b): ', a|b)
print('(c): ', a^b)
print('(d): ', a<<2, b<<2)
print('(e): ', a>>2, b>>4)
print('\n')


#......................QUESTION 4.......................

print('ANSWER 4')

x=int(input('Enter first number: '))
y=int(input('Enter second number: '))
z=int(input('Enter third number: '))

if x>y:
    if x>z:
        print('Greatest number is: ',(x))
    else:
        print('Greatest number is: ',(z))

elif x<y:
    if y<z:
        print('Greatest number is: ',(z))
    else:
        print('Greatest number is: ',(y))

print('\n')


#......................QUESTION 5.......................

print('ANSWER 5')

_str=input('Enter a string: ')
if 'name' in _str:
    print('Yes')
else:
    print('No')

print('\n')


#......................QUESTION 6.......................

print('ANSWER 6')

side1=int(input('Enter length of side 1: '))
side2=int(input('Enter length of side 2: '))
side3=int(input('Enter length of side 3: '))

if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
    print('Yes')
else:
    print('No')
    
print('\n')


# THANKS 

          

        
    
        









      








