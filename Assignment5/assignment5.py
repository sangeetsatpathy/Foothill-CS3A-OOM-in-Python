"""
    Assignment 5: Reverse a List using Recursion
    Submitted by Sangeet Satpathy
    Submitted:  October 23, 2021
    This program utilizes recursion to reverse a list.
 """


def reverse_a_list(my_list):
    """ reverse the order of my_list """
    print(len(my_list))
    length = len(my_list)
    if length == 1:
        return my_list
    ret_value = my_list[length - 1:] + reverse_a_list(my_list[0:length - 1])
    return ret_value


def main():
    """The main program, from which everything is executed"""
    alphabet = [chr(i) for i in range(97, 123)]
    print(alphabet)
    print(reverse_a_list(alphabet))
    print(alphabet)


if __name__ == "__main__":
    main()
r"""
C:\Users\sange\PycharmProjects\AssignmentFive\venv\Scripts\python.exe C:/Users/sange/PycharmProjects/AssignmentFive/assignment5.py
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Process finished with exit code 0
"""