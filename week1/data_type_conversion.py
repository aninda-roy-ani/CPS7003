# Taking user input

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))

# Calculating age and BMI

age = 2024 - birth_year
bmi = weight/(height*height)
'''
print("Summary for Human "+name+":")
print("-------------------------")
print("Age :   ",age,"(Born ",birth_year,")")
print("Weight :",weight,"kg")
print("Height :",height,"m")
print("BMI:    ",bmi)
'''

print('''
Summary for Human ''' + name + ''':
-------------------------
Age:    ''' + str(age) + ''' (Born ''' + str(birth_year) + ''')
Weight: ''' + str(weight) + ''' kg
Height: ''' + str(height) + ''' m
BMI:    ''' + str(bmi) + '''
''')