# BMI Calculator

## 📋 Description
A Python-based Body Mass Index (BMI) calculator that allows users to calculate their BMI, get health category classification, and receive personalized advice. Users can check multiple BMI calculations in a single session.

## 🎯 Features
- ✅ User-friendly interactive interface
- ✅ Calculates BMI using standard formula (BMI = weight / height²)
- ✅ Classifies BMI into 4 health categories
- ✅ Provides personalized health advice
- ✅ Input validation for positive values
- ✅ Error handling for invalid inputs
- ✅ Loop to check multiple BMIs without restarting
- ✅ User-friendly exit message

## 📊 BMI Categories and Advice
| BMI Range | Category | Advice |
|-----------|----------|--------|
| Below 18.5 | Underweight | Eat healthy and gain weight. |
| 18.5 - 24.9 | Normal | Great! Maintain your lifestyle. |
| 25.0 - 29.9 | Overweight | Exercise regularly. |
| 30.0 and above | Obese | Consult a doctor. |

## 🚀 How to Use

### Prerequisites
- Python 3.x installed on your system

### Running the Program
```bash
python bmi_calculator.py
```

### Example Execution
```
====== BMI CALCULATOR ======
Enter your name: John
Enter your weight (kg): 70
Enter your height (meters): 1.75

John, your BMI is: 22.86
Category: Normal
Advice: Great! Maintain your lifestyle.

Check another BMI? (yes/no): no
Thank you 👋
```

## 💡 How It Works
1. **Input Phase**: Takes name, weight (kg), and height (meters) from user
2. **Validation**: Checks if weight and height are positive values
3. **Calculation**: Computes BMI using the formula: BMI = weight / (height²)
4. **Categorization**: Determines health category based on BMI range
5. **Output**: Displays BMI, category, and health advice
6. **Loop**: Asks user if they want to check another BMI
7. **Exit**: Thanks the user and exits the program

## 🔍 Error Handling
- Validates positive values for weight and height
- Handles invalid (non-numeric) input gracefully with try-except
- Displays clear error messages
- Allows user to retry after errors

## 💡 Example Calculations
- Weight: 60 kg, Height: 1.70 m → BMI: 20.76 (Normal)
- Weight: 80 kg, Height: 1.75 m → BMI: 26.12 (Overweight)
- Weight: 50 kg, Height: 1.60 m → BMI: 19.53 (Normal)
- Weight: 90 kg, Height: 1.70 m → BMI: 31.14 (Obese)

## 📚 Learning Outcomes
This project demonstrates:
- While loops and control flow
- Conditional statements (if-elif-else)
- User input and output handling
- Error handling with try-except blocks
- String formatting with f-strings
- Variables and data types (int, float, string)
- Logic and calculations

## 🎓 OIBSIP Task
**Task**: BMI Calculator (First Task)  
**Language**: Python  
**Status**: ✅ Completed  
**Date**: June 2026  
**Repository**: [Padmaja04/OIBSIP](https://github.com/Padmaja04/OIBSIP)
