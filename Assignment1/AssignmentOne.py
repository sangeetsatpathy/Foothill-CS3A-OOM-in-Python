"""
    Assignment Two: Temperature Conversions
    Submitted by Sangeet Satpathy
    Submitted:  October 1, 2021

    Assignment 2: Add code to prompt the user for a temperature in Celsius and
    then converts that temperature to a specified different temperature
    unit.

    Assignment 1: This program demonstrates printing lines of text to the screen
"""


def convert_units(celsius_value, units):
    """Converts the Celsius value into either Fahrenheit or Kelvin. Returns result as a float.
     Takes in 2 arguments:
     1. celsius_value (float) - the temperature value to be converted, in degrees Celsius.
     2. units (int) - indicates what unit to convert to
        if units is 0, return the celsius value; if 1, convert to F; if 2, convert to K;"""
    if units == 0:
        return celsius_value
    elif units == 1:
        deg_fahren = (celsius_value * 9 / 5) + 32
        return deg_fahren
    else:  # (units==2)
        deg_kelvin = celsius_value + 273.15
        return deg_kelvin


def print_header():
    """Print a greeting."""
    print("STEM Center Temperature Project")
    print("Sangeet Satpathy")


def main():
    print_header()
    str_degrees = input("Please enter a temperature in degrees Celsius: ")
    str_unit = input("Please enter the desired conversion "
                     "(0 for no conversion, 1 to convert to Fahrenheit, 2 to Kelvin): ")
    input_degrees = float(str_degrees)
    unit = int(str_unit)
    if unit == 1:
        printed_unit = "Fahrenheit"
    elif unit == 2:
        printed_unit = "Kelvin"
    else:
        printed_unit = "Celsius"
    converted_val = convert_units(input_degrees, unit)
    output = f"That's {converted_val} degrees {printed_unit}"
    print(output)


if __name__ == "__main__":
    main()

# Sample Run 1 (Fahrenheit)
r"""
C:\Users\sange\PycharmProjects\assignment1\venv\Scripts\python.exe C:/Users/sange/PycharmProjects/assignment1/AssignmentOne.py
STEM Center Temperature Project
Sangeet Satpathy
Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 to convert to Fahrenheit, 2 to Kelvin): 1
That's 113.0 degrees Fahrenheit

Process finished with exit code 0
"""

# Sample Run 2 (Kelvin)
r"""
C:\Users\sange\PycharmProjects\assignment1\venv\Scripts\python.exe C:/Users/sange/PycharmProjects/assignment1/AssignmentOne.py
STEM Center Temperature Project
Sangeet Satpathy
Please enter a temperature in degrees Celsius: 45
Please enter the desired conversion (0 for no conversion, 1 to convert to Fahrenheit, 2 to Kelvin): 2
That's 318.15 degrees Kelvin

Process finished with exit code 0

"""
