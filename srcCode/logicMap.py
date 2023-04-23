# Name: Abdulnaser Sheikh
# Date: April 22th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

class MemMap:
    def __init__(self, process_number, frame_number):
        self.process_number = process_number  # store the process number of the memory map
        self.frame_number = frame_number  # store the frame number of the memory map

    def get_process_number(self):
        return self.process_number  # return the process number of the memory map

    def get_frame_number(self):
        return self.frame_number  # return the frame number of the memory map

    def __str__(self):
        return "Process number {}, Frame Number: {}".format(self.process_number, self.frame_number)  # return a string representation of the memory map

    def __eq__(self, other):
        if self is other:  # if the two objects are the same
            return True

        if not isinstance(other, MemMap):  # if the other object is not of type MemMap
            return False

        # if both objects have the same process number and frame number
        return (self.frame_number == other.frame_number and
                self.process_number == other.process_number)
