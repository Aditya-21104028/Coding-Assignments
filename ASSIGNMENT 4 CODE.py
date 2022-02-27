# *************** QUESTION 1 ***************

print("ANSWER 1")
print("\n")

def tower_of_hanoi(n, start, aux, dest):
    if n == 1:
        print("Move disc 1 from", start, "to", dest)
        return

    tower_of_hanoi(n-1, start, dest, aux)
    print("Move disc", n, "from", start, "to", dest)
    tower_of_hanoi(n-1, aux, start, dest)   

tower_of_hanoi(3, "A", "B", "C")  

print("\n")


# *************** QUESTION 2 ***************

print("ANSWER 2")
print("\n")

print("BY ITERATIVE METHOD: ")

print("\n")

n = int(input("Enter the number of rows of Pascal's Triangle: "))

def fact(N):
    f = 1
    if N == 0:
        return 1
    for I in range(2, N+1):
        f = f*I
    return f      

for i in range(n):
    for j in range(n-i+1):
        print(end=" ")

    for j in range(i+1):
        print(fact(i)//(fact(j)*fact(i-j)), end= " ")

    print()

print("\n")

print("BY RECURSIVE METHOD")

print("\n")

def Pascal_triangle(n):
    if n == 1:
        return[[1]]

    else:
        result = Pascal_triangle(n-1)
        new_row = [1]
        prev_row = result[-1]
        
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i+1])
        new_row += [1]
        result.append(new_row)
        return result   

n = int(input("Enter the number of rows: "))
triangle = Pascal_triangle(n)

for row in triangle:
    print(row)

print("\n")



# *************** QUESTION 3 ***************

print("ANSWER 3")
print("\n")

def func(a,b):
    if a>=b:
        print("The qoutient is: ", a//b)
        print("The remainder is: ", a%b)
        result = [a//b, a%b]
        return result

    else:
        print("The qoutient is: ", b//a)
        print("The remainder is: ", b%a)
        result = [b//a, b%a]
        return result

print("PART (a)")
a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
func(a,b)
print("Function is callable: ", callable(func))      
print("\n")

print("PART (b)")
print("First number is zero: ", a == 0)
print("Second number is zero: ", b == 0)
print("The qoutient is zero: ", a//b == 0)
print("The remainder is zero: ", a%b == 0)
print("\n")

print("PART (c)")
list1 = []
result = func(a,b)
for i in result:
    if i > 4:
        list1.append(i)
print("Values greater than 4 are: ", list1)
print("\n")

print("PART (d)")
set1 = set(list1)
print(set1)
print("\n")

print("PART (e)")
set2 = frozenset(set1)
print("The immutable set is: ", set2)
print("\n")

print("PART (f)")
max_val = 0
for i in set2:
    if i > max_val:
        max_val = i
print("Max. value from the given immutable set is: ", max_val)
hash_val = hash(max_val)
print("The hash value is: ", hash_val)
print("\n")



# *************** QUESTION 4 ***************

print("ANSWER 4")
print("\n")

class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        print("Object created")

    def details(self):
        print("Name: ", self.name)
        print("Roll No.: ", self.roll_no)

    def __del__(self):
        print("Object deleted")

std = Student("Aditya", "21104028")
std.details()

print("\n")



# *************** QUESTION 5 ***************

print("ANSWER 5")
print("\n")

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print("Name of the employee is: ", self.name, "and salary is: ", self.salary)

Emp1 = Employee("Mehak", "40000")
Emp2 = Employee("Ashok", "50000")
Emp3 = Employee("Viren", "60000")
Emp1.details()
Emp2.details()
Emp3.details()
print("\n")

print("PART (a)")
Emp1.salary = 70000
print("Updated salary of Mehak is: ", Emp1.salary)
print("\n")

print("PART (b)")
del Emp3
print("Record of the employee Viren deleted")
print("\n")


# *************** QUESTION 6 ***************

print("ANSWER 6")
print("\n")

George_word = input("Enter a word by George: ").lower()
Barbie_word = input("Enter a word by Barbie: ").lower()

George_list = list(George_word)
Barbie_list = list(Barbie_word)

George_list.sort()
Barbie_list.sort()
print("\n")

if len(George_word) != len(Barbie_word):
    print("Fake Freindship")

elif len(George_word) == 0:
    print("ERROR: George's word can't be empty.")    

if George_list == Barbie_list:
    print("True Friendship")  

else:
    print("Fake Friendship")

print("\n")

# DONE

            


