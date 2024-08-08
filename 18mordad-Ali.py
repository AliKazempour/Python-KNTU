
# while loop
# 1
# 2
# 3
# 4
# 5

count = 1
while count<=5:
    print(count)
    count+=1

# guss_game

import random

number_to_guss = random.randint(1,100)
# print(number_to_guss)
guss = None
while guss!=number_to_guss:
    guss = int(input("please guss number between 1 to 100 :"))
    if guss > number_to_guss:
        print("number_to_guss is smaller than guss")
    elif number_to_guss > guss:
        print("guss is smaller than number_to_guss")

print("Good,you win the game",number_to_guss)

# finding max in a list with while loop

n = int(input("please enter number :"))
numbers = []

for i in range(n):
    number = int(input("enter number :"))
    numbers.append(number)

# print(numbers)
max_number = numbers[0]
index = 1
while index < len(numbers):
    if numbers[index]> max_number:
        max_number = numbers[index]
    index+=1

print(f"Max is {max_number}")

# fact(5) = 5 *4 * 3 * 2 *1  N>=1 ;fact(0)=1

number = int(input("please enter number : "))
fact = 1
if number < 0:
    print("We can't")
elif number == 0:
    print(1)
else:
    for i in range(1,number+1):
        print(i)
        fact = fact * i
    print(f"fact({number}) is {fact}")

# claculating average in numbers list
def claculate_avg(numbers):
    if len(numbers) == 0 :
        return 0
    else:
        return sum(numbers)/len(numbers)

n = int(input("please enter number :"))
numbers_list = []
for i in range(n):
    number = int(input("enter number : "))
    numbers_list.append(number)

avg = claculate_avg(numbers_list)
print(f"avg is {avg}")


# find max with for loop

def find_max(numbers):
    if len(numbers) == 0 :
        return None
    else:
        max_number = numbers[0]
        for num in numbers:
            if num > max_number:
                max_number = num
        return max_number

n = int(input("please enter number :"))
numbers_list = []
for i in range(n):
    number = int(input("enter number : "))
    numbers_list.append(number)

max = find_max(numbers_list)
print(f"Max is {max}")


def is_palindrom(s):
    return s == s[::-1]
    # return s == reversed(s)


word = input("please enter a word : ")
if is_palindrom(word):
    print(f"{word} is palindrom")
else:
    print(f"{word} is not palindrom")


def fact(n):
    if n < 0 :
        return "fact must not be negative"
    elif n == 0 :
        return 1
    else:
        result = 1
        for i in range(1,n+1):
            result*=i
        return result

number = int(input("please enter number : "))
print(fact(number))


import random
n = int(input("please enter number : "))
numbers = []

for i in range(n):
    number = random.randint(1, 1000)
    numbers.append(number)

print(numbers)
sorted_list = sorted(numbers)
print(sorted_list)
numbers.sort()
print(numbers)
numbers.sort(reverse=False)
print(numbers)
numbers.sort(reverse=True)
print(numbers)

