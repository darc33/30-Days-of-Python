import random
import numpy as np
import Resources.countries_data as countdata


extable = [[1,1,1,1,1], [2,1,2,4,8], [3,1,3,9,27], [4,1,4,16,64], [5,1,5,25,125]]

for i in extable:
    for j in i:
       print (j, end=' ')
    print ('')
print()
sent = 'Python For Everyone'

for i in sent:
    if (i.isupper()) == True:
       print(sent[sent.index(i)], end='')

print('\n')

fra = '   Coding For All      '
print (fra.strip(' '))

print()

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

def math_fun (lst):
    list_min = min(lst)
    list_max = max(lst)
    lst.append(list_min)
    lst.append(list_max)
    list_median = np.percentile(lst, 50)
    list_average = np.average(lst)
    list_range = list_max-list_min
    list_comp = (list_min-list_average) < (list_max-list_average)
    print(list_min, list_max, ages, list_median, list_average, list_range, list_comp)
math_fun(ages)
print()

age=int(input("Enter your age:"))


if age >=18:
    print("You are old enough to learn to drive")
else:
    print(f'You need {18-age} more years to learn to drive')

#LIST COMPREHENSION

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negzero = [i for i in numbers if i<=0]
print('\n',negzero,'\n')
   
#LAMBDA FUNCTION
slope = lambda x1, y1, x2, y2: (y2-y1)/(x2-x1)
print(slope(3,2,1,1))

#HIGH ORDER FUNCTIONS, DECORATORS AND CLOSURE, MAP, FILTER

def get10names(lst):
    names = [sub['name'] for sub in lst]
    random.shuffle(names)
    return names[:10]
ctrs = get10names(countdata.countries)
ctrs_upper = list(map(lambda x: x.upper(),ctrs)) #MAP
ctrs_6ltrs = list(filter(lambda x: True if len(x)>=6 else False,ctrs)) #FILTER
print(ctrs, ctrs_upper, ctrs_6ltrs)

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator #HIGH ORDER FUNCTION
@uppercase_decorator   # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting()) 

names= ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(nordic_countries, es, ru)