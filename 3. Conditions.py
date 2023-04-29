name = "Vahe"
height = 1.83
weight = 97
bmi = weight / height ** 2

if bmi < 25:
    print(f'{name}\`s weight is normal with BMI ${bmi}')
elif bmi < 30:
    print(f'{name}\'s weight is not normal with BMI ${bmi}')
else:
    print(f'{name}\'s weight is more than normal with BMI ${bmi}')