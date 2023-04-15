# TUPLES
# Find the following indexes in the list below -2,[-4:-1]
aTuple = (100, 200, 300, 400, 500)
print(aTuple[-2])
print(aTuple[-4:-1])

# Find the output 
colors = "Yellow", 20, "Red"
a, b, c = colors
print(a)

# Choose the correct way to access value 20 from the following tuple
fruits = ("Orange", [10, 20, 30], (5, 15, 25))
print(fruits[1][1])

# oneTuple = (100)
# print(oneTuple * 2)

# SET
# Find the element at the first index 
# colorList = {"Yellow", "Orange", "Black"}
# print(colorList[1])

language = {"English","French","German"}
print(language.remove("German"))


# Returns a set of values that are in the first set but not in the second set
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}
set3 = set2.difference(set1)
print(set3)

setA = {10, 20, 30, 40, 50}
setB = {60, 70, 10, 30, 40, 80, 20, 50}
print(setA.issubset(setB))
print(setA.issuperset(setB))

varieties = {"Yellow", "Orange", "Black"}
varieties.add("Blue")
varieties.add("Orange")
print(varieties)

# FUNCTIONS
# define these additional 4 functions;
# subtract
# divide
# multiply
# remainder
# Each function accepts two arguments and returns the appropriate output.
def subtract(a,b):
    answer = a - b
    return answer

def divide(a,b):
    answer = a / b
    return answer

def multiply(a,b):
    answer = a * b
    return answer

def remainder(a,b):
    answer = a % b
    return answer




