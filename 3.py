def BMI(w,h):
    BMI = w / (h*2)
    print(BMI)
    if BMI <18.5:
        print("Under weight")
    elif BMI>=18.5 and BMI<24.9:
        print("Normal")
    elif BMI>=25 and BMI <29.9:
        print("Overweight")
    else :
        print("Obese")
w = float(input("Enter your weight in kgs:"))
h = float(input("Enter your height meters:"))
BMI(w,h)