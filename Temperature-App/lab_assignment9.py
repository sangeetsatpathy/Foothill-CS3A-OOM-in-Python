"""
    Assignment 11: Table with Temperature Data
    Submitted by Sangeet Satpathy
    Submitted:  December 5, 2021

    Assignment 11: Implemented the print_temp_by_day_time() function, which prints a table of average temperature
    readings(taken by active sensors) for a week, divided up into each of the hours of the day.

    Assignment 10: Implemented previous dataset creations and added code onto it to allow the user to check the
    minimum, maximum, and average temperature readings of active sensors as well as the average temperature reading
    at a certain day and time.

    Assignment 9: Combined Assignment 8 and Assignment 7 to form a program which can read file data, store it
    into a TempDataset object, and name the dataset. This functionality was implemented into the menu.
"""
import math

current_unit = 0
UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
}
DAYS = {
    0: "SUN",
    1: "MON",
    2: "TUE",
    3: "WED",
    4: "THU",
    5: "FRI",
    6: "SAT",
}

HOURS = {
    0: "Mid-1AM  ",
    1: "1AM-2AM  ",
    2: "2AM-3AM  ",
    3: "3AM-4AM  ",
    4: "4AM-5AM  ",
    5: "5AM-6AM  ",
    6: "6AM-7AM  ",
    7: "7AM-8AM  ",
    8: "8AM-9AM  ",
    9: "9AM-10AM ",
    10: "10AM-11AM",
    11: "11AM-NOON",
    12: "NOON-1PM ",
    13: "1PM-2PM  ",
    14: "2PM-3PM  ",
    15: "3PM-4PM  ",
    16: "4PM-5PM  ",
    17: "5PM-6PM  ",
    18: "6PM-7PM  ",
    19: "7PM-8PM  ",
    20: "8PM-9PM  ",
    21: "9PM-10PM ",
    22: "10PM-11PM",
    23: "11PM-MID ",
}


class TempDataset:
    """TempDataset is a class that creates objects that can perform queries on a temperature dataset passed into it."""
    numObjects = 0

    def __init__(self):
        """Initializes a TempDataset object"""
        self._data_set = None
        self._name = "Unnamed"
        TempDataset.numObjects += 1

    @property
    def name(self):
        """Accesses the name of the dataset"""
        return self._name

    @name.setter
    def name(self, newName):
        """Sets the name of the data set so long as the name has a length
        within the range of 3 and 20, inclusive."""
        if len(newName) in range(3, 21):
            self._name = newName
        else:
            raise ValueError

    def process_file(self, filename):
        """Reads the specified file and processes the data, moving sets of values into a list"""
        try:
            my_file = open(filename, "r")
        except FileNotFoundError:
            return False

        self._data_set = []
        for each_line in my_file:
            vals = each_line.split(",")
            if vals[3] == "TEMP":
                day = int(vals[0])
                time = int(math.floor(float(vals[1]) * 24))
                sensor = int(vals[2])
                temp = float(vals[4])
                line_readings = (day, time, sensor, temp)
                self._data_set.append(line_readings)
        my_file.close()
        return True

    def get_summary_statistics(self, active_sensors):
        """Returns the Minimum, Maximum, and Average of all the temperature
        readings taken by active sensors."""
        if self._data_set is None or len(active_sensors) == 0:
            return None
        active_readings = [d for (a, b, c, d) in self._data_set if c in active_sensors]
        sum_readings = 0
        for i in active_readings:
            sum_readings += i

        current_min = active_readings[0]
        current_max = active_readings[0]
        for m in active_readings:
            if m < current_min:
                current_min = m
            if m > current_max:
                current_max = m

        max_reading = round(current_max, 2)
        min_reading = round(current_min, 2)
        average_reading = round(sum_readings / len(active_readings), 2)
        return (min_reading, max_reading, average_reading)

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        """Returns the average temperature reading out of all the temperature
        readings taken from active sensors at a specified day and time."""
        if self._data_set is None or active_sensors is None:
            return None
        return_sum = 0
        matching_readings = [d for (a, b, c, d) in self._data_set if a == day if b == time if c in active_sensors]
        if len(matching_readings) == 0:
            return None
        for i in matching_readings:
            return_sum += i
        average = return_sum / len(matching_readings)
        return average

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if self._data_set is None:
            return None
        return 0

    def get_loaded_temps(self):
        """Returns the amount of temperature readings that have been loaded so far."""
        if self._data_set is None:
            return None
        return len(self._data_set)

    @staticmethod
    def get_num_objects():
        """A class method which returns the number of object instances of
        this class that have been created."""
        return TempDataset.numObjects


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
    """Prints the main menu, from which the user can select what they want to do."""
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
    """Creates a new file. This method creates a dataset and allows the user to name it,
    so long as the inputted name is in the range of 3 to 20 characters, inclusive."""
    inputted_file = input("Please enter the filename of the new dataset: ")
    processed_bool = dataset.process_file(inputted_file)
    if not processed_bool:
        print("File was not found, please enter a valid file name.")
        return
    files_loaded = dataset.get_loaded_temps()
    print(f"Loaded {files_loaded} samples")
    while dataset.name == "Unnamed":
        inputted_name = input("Please provide a 3 to 20 character name for the dataset: ")
        try:
            dataset.name = inputted_name
        except ValueError:
            print("Invalid dataset name, please enter a name only within the range of 3 to 20 characters.")


def choose_units():
    """Chooses which units to enter, filtering out invalid numbers or non-integer values."""
    global current_unit
    print(f"Current units in {UNITS[current_unit][0]}")
    print("Choose new units:")
    for i in UNITS:
        print(f"{i} - {UNITS[i][0]}")
    valid_input = False
    while not valid_input:
        try:
            unit_choice = int(input("Which unit?"))
            if unit_choice in UNITS:
                valid_input = True
                current_unit = unit_choice
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Please only enter a number.")


def change_filter(sensor_list, active_sensors):
    """Change the filters."""
    print("Change Filter Function Called")


def print_summary_statistics(dataset, active_sensors):
    """Prints a summary of the statistics"""
    summary_stats = dataset.get_summary_statistics(active_sensors)
    if summary_stats is None:
        print("Please load data file and make sure at least one sensor is active.")
        return
    print("Summary Statistics for Test Week")
    min_temp_celsius = summary_stats[0]
    max_temp_celsius = summary_stats[1]
    avg_temp_celsius = summary_stats[2]

    min_temp_current_unit = round(convert_units(min_temp_celsius, current_unit), 2)
    max_temp_current_unit = round(convert_units(max_temp_celsius, current_unit), 2)
    avg_temp_current_unit = round(convert_units(avg_temp_celsius, current_unit), 2)
    print(f"Minimum Temperature: {min_temp_current_unit} {UNITS[current_unit][1]}")
    print(f"Maximum Temperature: {max_temp_current_unit} {UNITS[current_unit][1]}")
    print(f"Average Temperature: {avg_temp_current_unit} {UNITS[current_unit][1]}")


def print_temp_by_day_time(dataset, active_sensors):
    """Prints a table of the average temperature readings of a dataset
     based on the active sensors, the day, and the time."""
    num_datasets = dataset.get_loaded_temps()
    if num_datasets is None:
        print("Please load a file first.")
        return
    print(f"Average Temperatures for {dataset.name}")
    print("Units are in " + UNITS[current_unit][0])
    print(f"{DAYS[0]:>16}{DAYS[1]:>6}{DAYS[2]:>6}{DAYS[3]:>6}{DAYS[4]:>6}{DAYS[5]:>6}{DAYS[1]:^9}")
    for hr in range(0, 24):
        line_readings = [dataset.get_avg_temperature_day_time(active_sensors, d, hr) for d in range(0, 7)]
        print(f"{HOURS[hr]:<10}", end="")
        for i in range(len(line_readings)):
            if line_readings[i] is None:
                line_readings[i] = "---"
                print(f"{line_readings[i]:>6}", end="")
            else:
                line_readings[i] = convert_units(line_readings[i], current_unit)
                print(f"{line_readings[i]:>6.1f}", end="")
        print()


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
    """Main method, where the program is executed."""
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
    current_set = TempDataset()
    while (True):
        try:
            print_menu()
            choice = int(input("What is your choice?"))
            if choice == 1:
                new_file(current_set)
            elif choice == 2:
                choose_units()
            elif choice == 3:
                change_filter(sensors, sorted_sensor_list, filter_list)
            elif choice == 4:
                print_summary_statistics(current_set, filter_list)
            elif choice == 5:
                print_temp_by_day_time(current_set, filter_list)
            elif choice == 6:
                print_histogram(current_set, filter_list)
            elif choice == 7:
                print("Thank you for using the STEM Center Temperature Project")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("*** Please enter a number only. ***")


if __name__ == "__main__":
    main()

r"""
C:\Users\sange\PycharmProjects\AssignmentTwo\venv\Scripts\python.exe C:\Users\sange\PycharmProjects\AssignmentTwo\lab_assignment9.py
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice?1
Please enter the filename of the new dataset: C:\Users\sange\PycharmProjects\AssignmentTwo\Temperatures2017-08-06.csv
Loaded 11724 samples
Please provide a 3 to 20 character name for the dataset: aaa
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice?2
Current units in Celsius
Choose new units:
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Which unit?1
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
Type the sensor to toggle (e.g. 4201) or x to end: 4204
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end: 4205
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]
Type the sensor to toggle (e.g. 4201) or x to end: Out
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside
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
What is your choice?5
Print Temp by Day/Time Function Called
Average Temperatures for aaa
Units are in Fahrenheit
             SUN   MON   TUE   WED   THU   FRI   MON   
Mid-1AM     68.8  68.4  72.7  71.3  70.6  70.7  66.8
1AM-2AM     69.0  68.3  72.5  71.1  70.3  70.5  66.9
2AM-3AM     69.1  68.3  72.3  70.9  70.0  70.4  67.0
3AM-4AM     69.2  68.1  72.2  70.8  69.8  70.3  67.0
4AM-5AM     69.2  68.1  72.1  70.6  69.7  70.1  67.1
5AM-6AM     69.2  68.0  72.1  70.5  69.6  70.0  67.1
6AM-7AM     68.8  67.9  72.1  70.1  69.4  69.6  67.1
7AM-8AM     68.1  68.1  71.8  70.0  69.5  69.2  67.1
8AM-9AM     67.4  68.1  71.1  69.5  69.7  68.3  67.1
9AM-10AM    67.3  69.1  71.5  69.4  70.6  67.1  67.2
10AM-11AM   67.1  70.4  72.3  69.9  71.5  66.6  67.2
11AM-NOON   66.9  70.9  73.2  70.4  72.2  66.6  66.6
NOON-1PM    66.8  71.2  73.1  71.3  72.1  66.3  65.9
1PM-2PM     66.7  71.9  73.6  72.3  71.9  66.1  65.5
2PM-3PM     66.9  72.8  74.3  73.1  72.3  66.1  65.2
3PM-4PM     66.7  73.3  74.7  74.0  72.7  66.1  65.0
4PM-5PM     66.7  73.8  75.1  74.4  73.4  66.0  64.9
5PM-6PM     66.7  74.2  75.7  74.9  74.0  66.0  64.9
6PM-7PM     66.7  73.5  75.1  74.6  73.5  65.8  64.8
7PM-8PM     67.2  73.4  74.0  73.4  72.5  65.7  64.8
8PM-9PM     67.8  73.4  73.0  72.6  71.7  65.4  64.7
9PM-10PM    68.1  73.3  72.2  71.7  71.1  65.5  64.9
10PM-11PM   68.3  73.2  71.8  71.3  70.9  66.3  65.5
11PM-MID    68.6  73.0  71.5  70.9  70.8  66.6  65.7
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
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside
Type the sensor to toggle (e.g. 4201) or x to end: 4213
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room [ACTIVE]
Out: Outside
Type the sensor to toggle (e.g. 4201) or x to end: 4218
4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside
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
What is your choice?5
Print Temp by Day/Time Function Called
Average Temperatures for aaa
Units are in Fahrenheit
             SUN   MON   TUE   WED   THU   FRI   MON   
Mid-1AM      ---   ---   ---   ---   ---   ---   ---
1AM-2AM      ---   ---   ---   ---   ---   ---   ---
2AM-3AM      ---   ---   ---   ---   ---   ---   ---
3AM-4AM      ---   ---   ---   ---   ---   ---   ---
4AM-5AM      ---   ---   ---   ---   ---   ---   ---
5AM-6AM      ---   ---   ---   ---   ---   ---   ---
6AM-7AM      ---   ---   ---   ---   ---   ---   ---
7AM-8AM      ---   ---   ---   ---   ---   ---   ---
8AM-9AM      ---   ---   ---   ---   ---   ---   ---
9AM-10AM     ---   ---   ---   ---   ---   ---   ---
10AM-11AM    ---   ---   ---   ---   ---   ---   ---
11AM-NOON    ---   ---   ---   ---   ---   ---   ---
NOON-1PM     ---   ---   ---   ---   ---   ---   ---
1PM-2PM      ---   ---   ---   ---   ---   ---   ---
2PM-3PM      ---   ---   ---   ---   ---   ---   ---
3PM-4PM      ---   ---   ---   ---   ---   ---   ---
4PM-5PM      ---   ---   ---   ---   ---   ---   ---
5PM-6PM      ---   ---   ---   ---   ---   ---   ---
6PM-7PM      ---   ---   ---   ---   ---   ---   ---
7PM-8PM      ---   ---   ---   ---   ---   ---   ---
8PM-9PM      ---   ---   ---   ---   ---   ---   ---
9PM-10PM     ---   ---   ---   ---   ---   ---   ---
10PM-11PM    ---   ---   ---   ---   ---   ---   ---
11PM-MID     ---   ---   ---   ---   ---   ---   ---
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
