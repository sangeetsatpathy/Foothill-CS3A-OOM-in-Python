"""
    Assignment Seven: Filter List
    Submitted by Sangeet Satpathy
    Submitted:  November 7, 2021

    Assignment 7: Add code to allow users to check and modify which sensors are active,
    defining the methods change_filter() and print_filter().

    Assignment 6: Use recursion to sort an inputted list, making a method named
    recursive_sort()

    Assignment 4: Add code to store values regarding sensors and the rooms in which
    they are located. This utilizes several new data types, including lists,
    tuples, and dictionaries.

    Assignment 3: Replace main function to print a menu, where users can pick
    what function they want to run, using stub functions for now.

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


def print_menu():
    print("Main Menu")
    print("---------")
    print("1 - Process a new data file")
    print("2 - Choose units")
    print("3 - Edit room filter")
    print("4 - Show summary statistics")
    print("5 - Show temperature by date and time")
    print("6 - Show histogram of temperatures")
    print("7 - Quit")


def new_file(dataset):
    """Creates a new file."""
    print("New File Function Called")


def choose_units():
    """Chooses which units to enter."""
    print("Choose Units Function Called")


def change_filter(sensor_list, active_sensors):
    """Change the filters."""
    print("Change Filter Function Called")


def print_summary_statistics(dataset, active_sensors):
    """Prints a summary of the statistics"""
    print("Summary Statistics Function Called")


def print_temp_by_day_time(dataset, active_sensors):
    """Prints the temperature by either the day or the time."""
    print("Print Temp by Day/Time Function Called")


def print_histogram(dataset, active_sensors):
    """Prints a histogram showcasing the data."""
    print("Print Histogram Function Called")


def recursive_sort(list_to_sort, key=0):
    """Sorts a given list using bubble sort via recursion."""
    copy_list = [i for i in list_to_sort]
    length = len(copy_list)
    if length == 1:
        return copy_list
    for i in range(0, length):
        if copy_list[i - 1][key] > copy_list[i][key]:
            temp = copy_list[i - 1]
            copy_list[i - 1] = copy_list[i]
            copy_list[i] = temp
    return recursive_sort(copy_list[0:length - 1], key) + copy_list[length - 1: length]


def print_filter(sensor_list, filter_list):
    """Prints all the sensors along with which ones are active and which ones are not."""
    for k in sensor_list:
        if k[2] in filter_list:
            print(k[0] + ": " + k[1] + " [ACTIVE]")
        else:
            print(k[0] + ": " + k[1])


def change_filter(sensors, sensor_list, filter_list):
    """Provides an interface to allow user to set sensors as inactive by removing them from the
    filter list."""
    sensors = {k[0]: k[2] for k in sensor_list}
    while True:
        print_filter(sensor_list, filter_list)
        user_choice = input("Type the sensor to toggle (e.g. 4201) or x to end: ")
        if user_choice == "x":
            return
        if user_choice not in sensors:
            print("Invalid sensor")
        else:
            filter_list.remove(sensors[user_choice])


def main():
    # sensor_0 through sensor_10 are the tuples to be stored as values in the dictionary
    sensor_0 = ("STEM Center", 0)
    sensor_1 = ("Foundations Lab", 1)
    sensor_2 = ("CS Lab", 2)
    sensor_3 = ("Workshop Room", 3)
    sensor_4 = ("Tiled Room", 4)
    sensor_10 = ("Outside", 10)

    sensors = {"4213": sensor_0, "4201": sensor_1, "4204": sensor_2,
               "4218": sensor_3, "4205": sensor_4, "Out": sensor_10}

    sensor_list = [(key, sensors[key][0], sensors[key][1]) for key in sensors]
    # For each key in the dictionary, the key and the elements within the value's tuple are added.

    filter_list = [sensors[i][1] for i in sensors]  # list of sensor numbers

    sorted_sensor_list = recursive_sort(sensor_list)  # Sorts by room number
    while (True):
        try:
            print_menu()
            choice = int(input("What is your choice?"))
            if choice == 1:
                new_file(None)
            elif choice == 2:
                choose_units()
            elif choice == 3:
                change_filter(sensors, sorted_sensor_list, filter_list)
            elif choice == 4:
                print_summary_statistics(None, None)
            elif choice == 5:
                print_temp_by_day_time(None, None)
            elif choice == 6:
                print_histogram(None, None)
            elif choice == 7:
                print("Thank you for using the STEM Center Temperature Project")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("*** Please enter a number only. ***")


"""
The following code is to test my data types. This was provided by Professor Murphy. """

if __name__ == "__main__":
    main()

r"""
C:\Users\sange\PycharmProjects\AssignmentTwo\venv\Scripts\python.exe C:/Users/sange/PycharmProjects/AssignmentTwo/lab_assignment3.py
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice?3
4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end: 4201
4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end: 4205
4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end: 4000
Invalid sensor
4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end: x
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice?7
Thank you for using the STEM Center Temperature Project

Process finished with exit code 0

"""
