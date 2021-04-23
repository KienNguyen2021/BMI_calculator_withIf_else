weight = float(input ("enter your weights in kg : "))
height = float(input ("enter your height in meter : "))

bmi = float (weight / (height ** 2)) # 2 power 2
bmi_integer = "{:.2f}".format (bmi)

if bmi < 18.5:
  print(f" Your BMI is {bmi_integer} Underweight")

elif bmi < 25 :
    print(f" Your BMI is {bmi_integer} Normal Weight")
elif bmi < 30 :
  print(f" Your BMI is {bmi_integer} Overweight")   
elif bmi < 35 :
  print(f" Your BMI is {bmi_integer} Obese")   
else :
  print(f" Your BMI is {bmi_integer} Clinically Obese")  
