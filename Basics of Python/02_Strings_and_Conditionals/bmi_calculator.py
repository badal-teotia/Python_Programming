# WAP to give BMI

weight = float(input("Weight in kg: "))
height = float(input("Height in metres: "))

if height <= 0:
    print("Height must be greater than zero.")
else:
    bmi = weight / (height ** 2)

    if bmi >= 25:
        condition = "Overweight"
    elif bmi >= 19.5:
        condition = "Normal"
    else:
        condition = "Underweight"

    print("Your BMI:", bmi)
    print("Your condition:", condition)
