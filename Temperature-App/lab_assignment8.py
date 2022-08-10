"""
    Assignment Eight: Dataset Class
    Submitted by Sangeet Satpathy
    Submitted:  November 14, 2021
"""
class TempDataset:
    """TempDataset is a class that creates objects that can perform queries on a temperature dataset passed into it."""
    numObjects = 0

    def __init__(self):
        """Initializes a TempDataset object"""
        self._data_set = None
        self._name = "Unnamed"
        TempDataset.numObjects+=1

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
        return False

    def get_summary_statistics(self, active_sensors):
        if self._data_set == None:
            return None
        return (0,0,0)

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        if self._data_set == None:
            return None
        return 0

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if self._data_set == None:
            return None
        return 0

    def get_loaded_temps(self):
        if self._data_set == None:
            return None
        return 0

    @staticmethod
    def get_num_objects():
        """A class method which returns the number of object instances of
        this class that have been created."""
        return TempDataset.numObjects

"""The following code was provided by the professor to test the code."""
current_set = TempDataset()

print("First test of get_num_objects: ", end='')

if TempDataset.get_num_objects() == 1:
    print("Success")
else:
    print("Fail")

second_set = TempDataset()

print("Second test of get_num_objects: ", end='')

if TempDataset.get_num_objects() == 2:
    print("Success")
else:
    print("Fail")

print("Testing get_name and set_name: ")

print("- Default Name:", end='')

if current_set.name == "Unnamed":
    print("Success")
else:
    print("Fail")

print("- Try setting a name too short: ", end='')

try:
    current_set.name = "to"
    print("Fail")
except ValueError:
    print("Success")

print("- Try setting a name too long: ", end='')

try:
    current_set.name = "supercalifragilisticexpialidocious"
    print("Fail")
except ValueError:
    print("Success")

print("- Try setting a name just right (Goldilocks): ", end='')


try:
    current_set.name = "New Name"
    if current_set.name == "New Name":
        print("Success")
    else:
        print("Fail")
except ValueError:
    print("Fail")

print("- Make sure we didn't touch the other object: ", end='')
if second_set.name == "Unnamed":
    print("Success")
else:
    print("Fail")

print("Testing get_avg_temperature_day_time: ", end='')
if current_set.get_avg_temperature_day_time(None, 0, 0) is None:
    print("Success")
else:
    print("Fail")

print("Testing get_num_temps: ", end='')
if current_set.get_num_temps(None, 0, 0) is None:
    print("Success")
else:
    print("Fail")

print("Testing get_loaded_temps: ", end='')
if current_set.get_loaded_temps() is None:
    print("Success")
else:
    print("Fail")

print("Testing get_summary_statistics: ", end='')
if current_set.get_summary_statistics(None) is None:
    print("Success")
else:
    print("Fail")

print("Testing process_file: ", end='')
if current_set.process_file(None) is False:
    print("Success")
else:
    print("Fail")



r"""
C:\Users\sange\PycharmProjects\AssignmentTwo\venv\Scripts\python.exe C:/Users/sange/PycharmProjects/AssignmentTwo/venv/lab_assignment8.py
First test of get_num_objects: Success
Second test of get_num_objects: Success
Testing get_name and set_name: 
- Default Name:Success
- Try setting a name too short: Success
- Try setting a name too long: Success
- Try setting a name just right (Goldilocks): Success
- Make sure we didn't touch the other object: Success
Testing get_avg_temperature_day_time: Success
Testing get_num_temps: Success
Testing get_loaded_temps: Success
Testing get_summary_statistics: Success
Testing process_file: Success

Process finished with exit code 0
"""