age = int(input('Enter your age (full): '))

if age > 18:

    height = int(input('Enter your height (in centimeters): '))
    weight = int(input('Enter your weight (in kilograms): '))

    body_mass_index = weight / ((height*0.01)**2)

    if body_mass_index < 18.5:
        bmi_user = "You are underweight"
        advise = "You need to gain at least " + str(round(18.5 - age)) + "kilograms."
    elif 18.5 <= body_mass_index <= 24.9:
        bmi_user = "You have a normal body weight "
        advise = "Keep it up!"
    elif 25 <= body_mass_index <= 29.9:
        bmi_user = "You are overweight"
        advise = "You need to lose at least " + str(round(age-24.9)) + " kilograms."
    elif body_mass_index >= 30:
        bmi_user = "You have signs of obesity"
        advise = "You need to lose at least " + str(round(age-29.9)) + " kilograms."

    perfect_weight_min = 18.5*(height*0.01)**2
    perfect_weight_max = 24.9*(height*0.01)**2

    print('Your perfect weight: from ' + str(round(perfect_weight_min)) + " to " + str(round(perfect_weight_max)) + " kilograms.")
    
else:
    bmi_user = "For pregnant women and children under 18, BMI does not give the right picture."

print(bmi_user)
print(advise)


