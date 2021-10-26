# /////////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python Stack > Python > Fundamentals: Functions Basic 1
# By:   Virgilio D. Cabading Jr.    Created: Oct 25, 2021
# /////////////////////////////////////////////////////////////

def print_desc(description) :
    print()
    print("////////////////////////////////////////////////////////////////////////////")
    print(description)
    print()

# /////////////////////////////////////////////////////////////
print_desc("#1")

# Prediction: prints 5

def number_of_food_groups():                                    
    return 5
print(number_of_food_groups())

# /////////////////////////////////////////////////////////////
print_desc("#2")

# Prediction: error undefined function

def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# /////////////////////////////////////////////////////////////
print_desc("#3")

# Prediction: print 5 as the number of books on hold

def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# /////////////////////////////////////////////////////////////
print_desc("#4")

# Prediction: print 5 as the number of fingers

def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# /////////////////////////////////////////////////////////////
print_desc("#5")

# Prediction: prints 5 twice
# actual result, function returns none

def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# /////////////////////////////////////////////////////////////
print_desc("#6")

# Prediction: print 3, 5, none
# Actual" prints 3, 5 then gives error for trying to add none

def add(b,c):
    print(b+c)
# print(add(1,2) + add(2,3))

# /////////////////////////////////////////////////////////////
print_desc("#7")

# Prediction: print 25

def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# /////////////////////////////////////////////////////////////
print_desc("#8")

# Prediction: print 100 --> print 10

def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

"""
# /////////////////////////////////////////////////////////////
print_desc("#9")

# Prediction: 

def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# /////////////////////////////////////////////////////////////
print_desc("#10")

# Prediction: 

def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# /////////////////////////////////////////////////////////////
print_desc("#11")

# Prediction: 

b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

# /////////////////////////////////////////////////////////////
print_desc("#12")

# Prediction: 

b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# /////////////////////////////////////////////////////////////
print_desc("#13")

# Prediction: 

b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# /////////////////////////////////////////////////////////////
print_desc("#14")

# Prediction: 

def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# /////////////////////////////////////////////////////////////
print_desc("#15")

# Prediction: 

def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

"""