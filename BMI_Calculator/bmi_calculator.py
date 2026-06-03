# BMI Calculator 

while True:
    print("\n====== BMI CALCULATOR ======")

    try:
        name = input("Enter your name: ")

        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (meters): "))

        if weight <= 0 or height <= 0:
            print("Please enter valid positive values!")
            continue

        bmi = weight / (height ** 2)

        print(f"\n{name}, your BMI is: {round(bmi, 2)}")

        if bmi < 18.5:
            category = "Underweight"
            advice = "Eat healthy and gain weight."
        elif bmi < 25:
            category = "Normal"
            advice = "Great! Maintain your lifestyle."
        elif bmi < 30:
            category = "Overweight"
            advice = "Exercise regularly."
        else:
            category = "Obese"
            advice = "Consult a doctor."

        print("Category:", category)
        print("Advice:", advice)

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    choice = input("\nCheck another BMI? (yes/no): ").lower()
    if choice != "yes":
        print("Thank you ")
        break
