# Software Testing and Quality Assurance - Assignment 2
# Name:     Karan Singh
# NetID:    kds662
# Purpose:  this assignment's goal is to create a BMI calculator
#           through a Test-Driven Development (TDD) approach

import pytest

def BMI_calc(weight_lb, feet, inches):

    weight_kg = convert_lb_to_kg(weight_lb)
    height_m = convert_feet_inch_to_m(feet, inches)
    BMI = (weight_kg / (height_m * height_m))

    return round(BMI, 1)

def BMI_calc_category(BMI):
    # [0, 18.5)
    if (BMI >= 0) and (BMI < 18.5):
        BMI_category = "Underweight"
    # [18.5, 24.9]
    elif (BMI >= 18.5) and (BMI <= 24.9):
        BMI_category = "Normal"
    # [25, 29.9]
    elif (BMI >= 25) and (BMI <= 29.9):
        BMI_category = "Overweight"
    # [30, infinity)
    elif BMI >= 30:
        BMI_category = "Obese"
    else:
        BMI_category = "Error"

    return BMI_category

def convert_lb_to_kg(weight_lb):
    weight_kg = weight_lb * 0.45
    return weight_kg

def convert_feet_inch_to_m(feet, inches):
    total_inches = (feet * 12) + inches
    height_m = total_inches * 0.025
    return height_m

def main():
    print("Welcome to our BMI Calculator\n")
    while(1):
        weight_lb = int(input("Please enter your weight (in pounds): "))
        print("Please enter your height -")
        feet = int(input("(in feet): "))
        inches = int(input("(inches): "))
        BMI = BMI_calc(weight_lb, feet, inches)
        BMI_category = BMI_calc_category(BMI)
        print("Your BMI is: " + str(round(BMI, 2)))
        print("Your BMI category is: " + BMI_category)
        continue_loop = input("\nWould you like to continue (Y): ")
        if continue_loop != "Y":
            print("Thank you.")
            break

# Weak N x 1 Test Cases
# [0, 18.5): -0.1, 0, 9, 18.4, 18.5
# [18.5, 24.9]: 18.4, 18.5, 22, 24.9, 25
# [25, 29.9]: 24.9, 25, 27, 29.9, 30
# [30, infinity) 29.9, 30, 45

# Pytest Testing
# [0, 18.5): -0.1, 0, 9, 18.4, 18.5
@pytest.mark.parametrize("BMI, BMI_category", [(-0.1,"Error"), (0,"Underweight"), (9, "Underweight"), (18.4, "Underweight"), (18.5, "Normal")])
def test_BMI_calc_category_underweight(BMI, BMI_category):
    assert BMI_calc_category(BMI) == BMI_category

# [18.5, 24.9]: 18.4, 18.5, 22, 24.9, 25
@pytest.mark.parametrize("BMI, BMI_category", [(18.4,"Underweight"), (18.5,"Normal"), (22, "Normal"), (24.9, "Normal"), (25, "Overweight")])
def test_BMI_calc_category_normal(BMI, BMI_category):
    assert BMI_calc_category(BMI) == BMI_category

# [25, 29.9]: 24.9, 25, 27, 29.9, 30
@pytest.mark.parametrize("BMI, BMI_category", [(24.9,"Normal"), (25,"Overweight"), (27, "Overweight"), (29.9, "Overweight"), (30, "Obese")])
def test_BMI_calc_category_overweight(BMI, BMI_category):
    assert BMI_calc_category(BMI) == BMI_category

# [30, infinity) 29.9, 30, 45
@pytest.mark.parametrize("BMI, BMI_category", [(29.9,"Overweight"), (30,"Obese"), (45, "Obese")])
def test_BMI_calc_category_obese(BMI, BMI_category):
    assert BMI_calc_category(BMI) == BMI_category

if __name__ == "__main__":
    main()