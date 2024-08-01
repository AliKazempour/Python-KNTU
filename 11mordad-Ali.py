
# Question 1: Grade Calculation and Pass/Fail Status

score = int(input("Please enter your score:"))

if 90 <= score <= 100:
    print("Excellent")
elif 70 <= score <= 89:
    print("Good")
elif 50 <= score <= 69:
    print("Pass")
else:
    print("Fail")

#######################################################


# Question 6: Employee Salary Calculation

hours_worked = int(input("Please enter the number of hours worked:"))
hourly_wage = int(input("Please enter the hourly wage:"))
if hours_worked > 40:
    salary = (hours_worked - 40) * hourly_wage * 1.5 + 40 * hourly_wage
    print(f"Total salary:${salary}")
else:
    salary = hours_worked * hourly_wage
    print(f"Total salary:${salary}")

##################################################

name = input("please enetr your name :")
print("My name is ", name)
print(f"My name is {name}")  # f-string


# for loop

# range function
# range(1,10)  1 ----- 9 / by-default-step : 1
# range (1,11,2)  1 , 3 , 5 , 7 , 9 / step : 2

for i in range(1, 4, 2):  # i = i + 2
    print("Hello World", i)

# 1 + 2 + 3 + ..... + n
sum = 0
n = int(input())        # n = 3 ---> range(1,4) --> i = 1 , 2 , 3
for i in range(1, n+1):
    print(f"sum : {sum} , i : {i}")
    sum = sum + i
print(f"Answer is : {sum}")


#  1 - 2 + 3 - 4 + 5 - 6 + .......

# road 1

n = int(input())
sum_positive = 0
sum_negative = 0
for i in range(1, n+1, 2):
    # sum_positive = i + sum_positive
    sum_positive += i
for i in range(2, n+1, 2):
    # sum_negative = i + sum_negative
    sum_negative += i


print(f"Answer is : {sum_positive - sum_negative}")


# road 2
n = int(input())
sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum -= i
        # sum = sum - i
    else:
        sum += i
        # sum = sum + i

print(f"Answer is : {sum}")


# a,A,e,E,i,I,o,O,u,U

word = "Ali Kazempour"
# print(word[1])  # output : A
print(word[1:])   # output  : li Kazempour
print(word[::-1])  # output  : ruopmezaK ilA
print(word[1::2])  # output  : l aepu

word = input("enter a string please : ")  # example : Ali Kazempour
sound = "aAeEiIoOuU"
counter = 0
for i in word:
    if i in sound:
        print(f"i : {i} ,counter : {counter}")
        counter = counter + 1
print(f"Count is : {counter}")
