# Name: Abdulnaser Sheikh
# Date: April 22th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

# Importing necessary modules
import sys
import os
from typing import List
from srcCode.logicCache import MemCache
from srcCode.logicParser import theParser

# Initializing global variable theParser
objectParser = None

# Main function that takes command line arguments and runs the cache simulation
def main(args: List[str]) -> None:
    # Validating the input arguments
    parameters = validate_arguments(args)

    global objectParser
    if parameters:
        # Parsing memory map from the file using objectParser
        mml = objectParser.get_file_memory_map()

        # Creating a list of MemCache objects, one for each process in the memory map
        cache_list = [MemCache(parameters[i + 1], objectParser.get_process_numbers()[i]) for i in range(len(objectParser.get_process_numbers()))]

        # Processing each MemMap object in the memory map and updating the corresponding cache
        for mm in mml:
            cache_list[mm.get_process_number() - 1].process(mm)

        # Calculating and printing the hit ratio for each cache
        average = 0.0
        for c in cache_list:
            print(c)
            average += c.get_ratio()

        # Calculating and printing the average hit ratio
        average /= len(cache_list)
        print(f"Average: {average * 100:.2f}%")

    else:
        # If input arguments are invalid, print error message
        print("ERROR: !!!!", file=os.sys.stderr)

# Function to validate the command line arguments
def validate_arguments(args: List[str]) -> List[object]:
    # Initializing variables and flags for validating the input arguments
    arguments = []
    arguments_valid = True

    # Checking if the number of input arguments is sufficient
    if len(args) == 0 or len(args) == 1:
        print("ERROR: python3 Main.py file_name.txt x1 x2 x3 x4", file=os.sys.stderr)
        arguments_valid = False
    else:
        # Getting the input file name and checking if the file exists
        input_file_name = args[0]
        input_file = os.path.abspath(input_file_name)
        if not os.path.exists(input_file):
            print("ERROR: python3 Main.py file_name.txt x1 x2 x3 x4", file=os.sys.stderr)
            arguments_valid = False
        else:
            arguments.append(input_file)

        # Parsing the cache sizes from the input arguments
        if arguments_valid:
            for i in range(1, len(args)):
                arguments.append(int(args[i]))

        # Parsing the memory map file using theParser and validating the number of allocations
        if arguments_valid:
            global objectParser
            objectParser = theParser(arguments[0])
            try:
                number_of_processes = len(objectParser.parse_process_numbers())

                # Checking that the number of allocations in the file matches the number of processes specified
                if number_of_processes != len(arguments) - 1:
                    print("allocations ≠ the number of processes", file=os.sys.stderr)
                    arguments_valid = False

            except IOError as e:
                print(e, file=os.sys.stderr)

    # Clearing the arguments list if they are invalid
    if not arguments_valid:
        arguments.clear()

    return arguments

if __name__ == "__main__":
    main(sys.argv[1:])
