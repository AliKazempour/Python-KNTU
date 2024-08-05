
# Question 7: Determine Age Category

age = int(input("Please enter your age :"))
if age <= 12:
    print("Age category:Child")
elif 13 <= age <= 19:
    print("Age category:Teenager")
elif 20 <= age <= 64:
    print("Age category:Adult")
else:
    print("Age category:Senior")

# Example :

# number = 5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# ......
# 5 * 10 = 50

number = int(input("Please enter number:"))
for i in range(1, 11):
    print(f"i = {i}")
    print(f"{number} * {i} = {number * i}")


# n= 10 ---->1,2,3,4,5,6,7,8,9,10 /2,4,6,8,10 ---> even  / 1,3,5,7,9 --->odd
number = int(input("please enter number : "))
for i in range(1, number+1):
    print(f"i = {i}")
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

# String Concating
name = "Ali"
family = "Kazempour"
full_name = name + " "+family
print(full_name)
print(name[0])  # A
print(name[::-1])  # ilA

# Repetition
new_name = 3 * name
print(new_name)


# multi_line using docstring
senetnce = """Programming is one of the best jobs in the world.
                In this course , We learn python .
            """

text = "the Amazing Spider-Man"
print(text.upper())
print(text.lower())
print(text.swapcase())

text2 = "Python is one of the best programming language"
new_text2 = text.replace("Python","C++").replace("best","hardest")
print(new_text2)
print("cpp" in text2)
print("python" in text2)


# 1 ....10
for i in range(1,11):
    print(i)

# n = 10 ---> 10 9 8 7 .....1
n = int(input("please enter number : "))
for i in range(10,0,-1):
    print(i)
