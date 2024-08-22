def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return None

def bmi_category(bmi):
    if bmi is None:
        return "Invalid BMI"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
    except ValueError:
        print("Please enter valid numbers for height and weight.")
        return

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    if bmi is not None:
        print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI Category: {category}")

if __name__ == "__main__":
    main()
