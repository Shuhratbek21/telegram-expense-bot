# price = 10  #numbers
# rating = 4.9  #floats
# name = "Mosh" #strings                                                                                                                                                                                                                                                                                                                                                                                                                     
# is_published = False  #booleans
# print(price)

# full_name="John Smith"
# age=20
# is_new = True


# name = input('What is yor name?  ')
# print('Hi ' + name)

# name = input('What is your name? ')
# color= input('What is yor favourite color? ')
# print(name + ' likes ' + color )

# birth_year = input("Birth year: ")
# print(type(birth_year))
# age = 2023 - int(birth_year)        ***
# print(type(age))
# print(age)

# weight_lbs=input('Weight (lbs)?: ')
# weight_kg=int(weight_lbs) * 0.45
# print(weight_kg)

# course1 = "Python's Course for Beginners"
# course2 = 'Python Course for "Beginners"'
# print(course1)
# print(course2)

# course = "Python's Course for Beginners"
# another = course[:]
# print(course[0])
# print(course[-1])
# print(course[0:])
# print(course[:5])
# print(course[:])

# another = course[:]
# print(another)

# name = "Jennifer"
# print(name[1:-1])

# first = 'John'
# last = 'Smith'
# message = first + ' ['+ last + '] is a coder'
# print(message)
# msg = f'{first} [{last}] is a coder' #formattedString
# print(msg) 

# course = "Python for Beginners"
# print(len(course))

# print(course.upper()) #method
# print(course.lower())  
# print(course.title())
# print(course.find('Beginners'))
# print(course.find('O'))
# print(course.find('P'))
# print(course.replace('Beginners', 'Absolute Beginners'))
# print(course.replace('beginners', 'Absolute Beginners'))
# print(course.replace('P', 'J'))

# print('Python' in course)   #boolean
# print('python' in course)  

#arithmetic operators

# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# x = 10
# x = x + 3
# x+= 3    #augmented assignment operator
# print(x)

# x = 10
# x-= 3
# print(x)

# x = 10 + 3 * 2  #operator precedence
# print(x)

# exponentiation 2**2
# paranthesis()

# x = (2+3)*10-3
# print(x)

# import math
# print(math.ceil(2.9))
# print(math.floor(2.9))

# x = 2.9
# print(round(x))
# print(abs(-2.9))            #Python 3 math module /browser search

#IF STATEMENTS

# is_hot = True

# if is_hot: 
    #print("It is a hot day")
    # print("Drink plenty of water")

# print("Enjoy your day")

# is_hot = True #/False
# is_cold= True #/False

# if is_hot: 
#     print("It is a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It is a cold day")
#     print("Wear warm clothes")
# else:
#     print("It is a lovely day")

# print("Enjoy your day")

# price=1000000
# has_good_credit = True

# if has_good_credit:
#     down_payment=0.1*price 
# else: 
#     down_payment=0.2*price 
# print(f"Down payment: ${down_payment}")


#Logical Operators

# has_high_income=True #/Flase
# has_good_credit=True #/False

# if has_high_income and has_good_credit:
#     print('Eligible for loan')

# if has_high_income or has_good_credit:
#     print('Eligible for loan')
 
# has_good_credit=True 
# has_criminal_record=True  #/False

# if has_good_credit and not has_criminal_record:
#     print('Eligible for loan')


# def reverse_string(string):
#     return string[::-1]                               
# print(reverse_string("world"))



#Logical Operators

# temperature=35    
#                                 #Comparison Operators
# if temperature==30:
#     print("It`s a hot a day")
# else:
#     print("It`s not a hot day")


name="Jwscnskcnlsdcnksldkcnslkdcnlaskcnasl;kcn;ascn;ascn;askncawecwedwedwedewascl"

if len(name)<3:
    print("Name must be at least 3 characters")
elif len(name)>50:
    print("Name can be a maximum of 50 characters")
else: 
    print("Name looks nice")






# total_income = 50000
# total_expenses = 6000

# def add_income(amount):
#     global total_income
#     total_income += amount

# def add_expense(amount):
#     global total_expenses
#     total_expenses += amount

# def calculate_balance():
#     return total_income - total_expenses

# # print("Income:", total_income)
# # print("Expenses:", total_expenses)
# print("Balance:", calculate_balance())























