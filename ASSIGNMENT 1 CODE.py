#ANSWER 1

#CALCULATE AVERAGE OF THREE NUMBERS ENTERED BY THE USER
print("ANSWER 1")

a=input("Enter first number: ")
b=input("Enter second number: ")
c=input("Enter third number: ")

d = (int(a)+ int(b)+ int(c))/3
 
print("The average of the three numbers: ", d)

print('\n')



#ANSWER 2

#CALCULATE INCOME TAX OF A PERSON
print("ANSWER 2")

x=input("Enter Gross Income: ")
y=input("Enter number of Dependents: ")
print("Standard deduction: 10000")
print("Dependent deduction: 3000")
z=int(x) - 10000 - (3000 * int(y))

print("Taxable Income: ", z)

print("Tax rate: 20%")

print("TAX: ", z*0.2)

print('\n')



#ANSWER 3

#DIFFERENT DATA TYPE VALUE IN A LIST
print("ANSWER 3")

x= ["SID:", 21104028, "NAME:", "ADITYA KUMAR" , "GENDER:", "M", "COURSE NAME:", "UG", "CGPA:", 9.8]
print(x)

print("\n")



#ANSWER 4

#SORTING MARKS OF STUDENTS
print("ANSWER 4")

p=input("ENTER MARKS OF STUDENT 1: ")
q=input("ENTER MARKS OF STUDENT 2: ")
r=input("ENTER MARKS OF STUDENT 3: ")
s=input("ENTER MARKS OF STUDENT 4: ")
t=input("ENTER MARKS OF STUDENT 5: ")

MARKS=[int(p), int(q), int(r), int(s), int(t)]

MARKS.sort()

print(MARKS)

print("\n")



#ANSWER 5(a)

#DELETING AN ELEMENT FROM A LIST
print("ANSWER 5(a)")

COLOUR = ["RED", "GREEN", "WHITE", "BLACK", "PINK", "YELLOW"]

del COLOUR[3]

print(COLOUR)
print("\n")



#ANSWER 5(b)

#REPLACING ELEMENTS FROM THE LIST
print("ANSWER 5(b)")


COLOUR[3]="PURPLE"
print(COLOUR)


#THANKS







