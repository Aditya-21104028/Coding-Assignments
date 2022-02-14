# ************* QUESTION 1 *****************

print("ANSWER 1")
print("\n")

def word_occ(str):
    lst = str.split()
    dct = dict()

    for i in lst:
        if i in dct:
            dct[i] += 1

        else:
            dct[i]=1

    return dct

def char_occ(str):
    dct = dict()

    for i in str:
        if i in dct:
            dct[i] += 1

        else:
            dct[i]=1

    return dct

str = input("Enter a string: ")
lst = str.split()

if len(lst)==1:   
    print(char_occ(str))

else:
    print(word_occ(str))

print("\n")

#**************** QUESTION 2 *****************

print("ANSWER 2")
print("\n")

year= int(input("Enter a year (1800-2025): ")) 

if 1800<=year<=2025 and year % 4 == 0:
    leapyear = True

elif 1800<=year<=2025 and year % 4 != 0:
    leapyear = False 

else:
    print("Error: Year out of range")
    
month= int(input("Enter a month (1-12): ")) 

if leapyear:
    if month in (1,3,5,7,8,10,12):
        month_days = 31

    elif month in (4,6,9,11):
        month_days = 30

    elif month<=1 or month>=12:
        print("Error: Month not valid")
        
    else:    
        month_days = 29

else:
    if month in (1,3,5,7,8,10,12):
        month_days = 31

    elif month in (4,6,9,11):
        month_days = 30

    elif month<=1 or month>=12:
        print("Error: Month not valid")

    else:
        month_days = 28
    

date= int(input("Enter a date (1-31): ")) 

if date<month_days and 1<=date<=31:
    date += 1
    
elif date==31 and month==12:
    date = 1
    month = 1
    year += 1

elif date<=1 or date>=31 :
    print("Error: Date not valid")

else:
    date = 1
    month += 1

print("The next date of the given date is: ", year, month, date)
print("\n")


#*************** QUESTION 3 *****************

print("ANSWER 3")
print("\n")


def square(lst):
    sq=[]

    for i in range(0, len(lst)):
        a = [(lst[i], lst[i]**2)]
        sq.append(a)
        i += 1
    return sq

n= int(input("Enter length of list: "))
lst=[]
for i in range(0,n):
    element = int(input("Enter element of list: "))
    lst.append(element)
    i += 1
    
    
print(square(lst))
print("\n")



#*************** QUESTION 4 ****************

print("ANSWER 4")
print("\n")

grade_point= int(input("Enter Grade Point: "))

if grade_point == 4:
    print("Your Grade is ‘D’ and 'Poor' Performance.")

elif grade_point == 5:
    print("Your Grade is ‘C’ and 'Below Average' Performance.")

elif grade_point == 6:
    print("Your Grade is ‘C+’ and 'Average' Performance.")

elif grade_point == 7:
    print("Your Grade is ‘B’ and 'Good' Performance.")

elif grade_point == 8:
    print("Your Grade is ‘B+’ and 'Very Good' Performance.")

elif grade_point == 9:
    print("Your Grade is ‘A’ and 'Excellent' Performance.")

elif grade_point == 10:
    print("Your Grade is ‘A+’ and 'Outstanding' Performance.")

else:
    print("Error")
print("\n")



#***************** QUESTION 5 ******************

print("ANSWER 5")
print("\n")


str1= "ABCDEFGHIJK"
length= len(str1)

for i in range(0, length):
    for j in range(0, i):
        print(" ", end="")

    for j in range(0, length-i*2):
        print(str1[j], end="")

    print()    
print("\n")


#**************** QUESTION 6 ******************

print("ANSWER 6")
print("\n")

# part(a)
print("6(a)")

dct=dict()
ask= "Y"

while(ask=="Y"):
    sid= int(input("Enter SID: "))
    name= input("Enter student name: ")
    dct[sid] = name
    ask= input("Type 'Y' to continue: ")

print(dct)
print("\n")


# part(b)
print("6(b)")

dct2= sorted(dct.items(), key= lambda item:item[1])
print(dct2)
print("\n")


# part(c)
print("6(c)")

dct3= sorted(dct.items())
print(dct3)
print("\n")


# part(d)
print("6(d)")

sid_input= int(input("Enter SID: "))
print("Student with given SID is: ", dct[sid_input])
print("\n")



#*************** QUESTION 7 ********************

print("ANSWER 7")
print("\n")

def fibonacci(n):
    f= [0,1]

    for i in range(2, n+1):
        a= f[i-1] + f[i-2]
        f.append(a)
        
    return f

n= int(input("Enter number of terms: "))
print(fibonacci(n))
print("\n")

sum=0
for i in range(0, n+1):
    sum += 1
    avg= sum/n

print("The average of the Fibonacci series is: ", avg)
print("\n")




#****************** QUESTION 8 *****************

print("ANSWER 8")
print("\n")

set1= {1,2,3,4,5}
set2= {2,4,6,8}
set3= {1,5,9,13,17}

# part(a)
print("8(a)")

new_set1= set1.symmetric_difference(set2)
print(new_set1)
print("\n")


# part(b)
print("8(b)")

new_set2= new_set1.symmetric_difference(set3)
print(new_set2)
print("\n")


# part(c)
print("8(c)")

new_set3= set1 & set2 | set2 & set3 | set3 & set1
print(new_set3)
print("\n")


# part(d)
print("8(d)")

new_set4= {1,2,3,4,5,6,7,8,9,10} 
new_set5= new_set4.difference(set1)
print(new_set5)
print("\n")


# part(e)
print("8(e)")

new_set6= new_set4.difference(set1 | set2 | set3)
print(new_set6)
print("\n")














    
    


























    
    








    

    


    




    
    
    
    
    
        
    

    





    
    
