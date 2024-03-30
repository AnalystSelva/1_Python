bmi_value = float(input("Enter the BMI Index:"))
if bmi_value < 18.5:
    print("Underweight")
elif 18.5 <= bmi_value <= 24.9:
    print("Normal weight ")
elif 25 <= bmi_value <= 29.9:
    print("Overweight")
else:
    print("Very Overweight")
