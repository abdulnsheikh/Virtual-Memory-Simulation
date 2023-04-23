# Name: Abdulnaser Sheikh
# Date: April 22th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

from typing import List  # import the List type from the typing module
from srcCode.logicMap import MemMap  # import the MemMap class from the logicMap module

class theParser:
    """
    A class to parse an input file and extract memory maps and process numbers.
    """

    def __init__(self, input_file: str):
        """
        Constructor method to initialize theParser object.

        :param input_file: path of the input file.
        """
        self.input_file = input_file  # initialize the input_file attribute with the passed parameter
        self.file_memory_map = []  # initialize an empty list for file memory map
        self.process_numbers = []  # initialize an empty list for process numbers

    def parse_file(self) -> List[MemMap]:
        """
        Method to parse the input file and create a list of MemMap objects.

        :return: A list of MemMap objects.
        """
        with open(self.input_file, 'r') as f:  # open the input file in read mode
            for line in f:  # loop through each line in the file
                split = line.split()  # split the line into a list of strings
                process_number = int(split[0])  # convert the first string to integer and assign it to process_number variable
                frame_number = int(split[1])  # convert the second string to integer and assign it to frame_number variable
                mm = MemMap(process_number, frame_number)  # create a MemMap object with process_number and frame_number as arguments
                self.file_memory_map.append(mm)  # add the MemMap object to file_memory_map list

        return self.file_memory_map  # return the file_memory_map list

    def parse_process_numbers(self) -> List[int]:
        """
        Method to parse the input file and extract the unique process numbers.

        :return: A list of unique process numbers.
        """
        if not self.file_memory_map:  # check if file_memory_map is empty
            self.parse_file()  # call parse_file method to populate file_memory_map

        for mm in self.file_memory_map:  # loop through each MemMap object in file_memory_map
            if mm.get_process_number() not in self.process_numbers:  # check if the process number of the MemMap object is already in process_numbers list
                self.process_numbers.append(mm.get_process_number())  # add the process number to process_numbers list

        return self.process_numbers  # return the process_numbers list

    def get_file_memory_map(self) -> List[MemMap]:
        """
        Method to get the file_memory_map attribute.

        :return: The file_memory_map attribute.
        """
        return self.file_memory_map  # return the file_memory_map attribute

    def get_process_numbers(self) -> List[int]:
        """
        Method to get the process_numbers attribute.

        :return: The process_numbers attribute.
        """
        return self.process_numbers  # return the process_numbers attribute
