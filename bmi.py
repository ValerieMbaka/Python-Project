# A simple program to calculate the BMI of a person
# Prompt the user to enter their height in metres and weight in kilograms

height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi: .2f}")

# Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 40:
    category = "Overweight"
else:
    category = "Obese"

print(f"You are categorized as: {category}")


# A simple program to calculate BMI using a function
# Define the function
def calculate_bmi (user_height,user_weight):
    user_bmi = user_weight / (user_height ** 2)
    return user_bmi

# Get user input for weight and height
user_weight = float(input("Enter your weight in kilograms: "))
user_height = float(input("Enter your height in metres: "))

# Calculate the BMI and print the BMI
user_bmi = calculate_bmi(user_height,user_weight)
print(f"Your BMI is: {user_bmi: .2f}")

# Determine the BMI category
if user_bmi < 18.5:
    category = "Underweight"
elif user_bmi < 25:
    category = "Normal weight"
elif user_bmi < 40:
    category = "Overweight"
else:
    category = "Obese"

print(f"You are categorized as: {category}")

