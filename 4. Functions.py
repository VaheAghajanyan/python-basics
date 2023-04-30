# No arg function
def function1():
    print('Hello World!')
    print('Hello World2!')

# Arg function
def function2(x):
    return 2 * x

# BMI Calculator
def bmi_calc(name, height, weight):
    bmi = weight / height ** 2

    if bmi < 25:
        print(f'{name}\'s bmi is {bmi}. It means weight is normal.')
    else:
        print(f'{name}\'s bmi is {bmi}. It means weight is more than normal.')

def is_even(num):
    return num % 2 == 0

bmi_calc("Vahe", 1.83, 97)
print(is_even(5))
print(is_even(4))