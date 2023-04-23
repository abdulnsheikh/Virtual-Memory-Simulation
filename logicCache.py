# Name: Abdulnaser Sheikh
# Date: April 22th, 2023
# University: UNIVERSITY OF NEBRASKA OMAHA
#             College of Information Science and Technology
# Course: Operating Systems

from queue import Queue  # Importing Queue class from queue module
from typing import List  # Importing List from typing module
from logicMap import MemMap  # Importing MemMap class from logicMap module

class MemCache:
    def __init__(self, size: int, process_number: int): 
        """
        Constructor method to initialize MemCache object.

        :param size: Maximum number of MemMap objects that can be stored in the cache.
        :param process_number: Process number to which the cache belongs.
        """
        self.queue = Queue()  # Initializing a Queue object
        self.total_hits = 0  # Initializing total_hits attribute to 0
        self.total_misses = 0  # Initializing total_misses attribute to 0
        self.size = size  # Initializing size attribute with the passed parameter
        self.process_number = process_number  # Initializing process_number attribute with the passed parameter

    def process(self, mm: MemMap) -> None: 
        """
        Method to process a MemMap object.

        :param mm: MemMap object to be processed.
        :return: None.
        """
        if mm in self.queue.queue:  # Checking if the MemMap object is already in the cache
            self.queue.queue.remove(mm)  # Removing the MemMap object from the cache
            self.total_hits += 1  # Incrementing total_hits attribute
        else: 
            self.total_misses += 1  # Incrementing total_misses attribute
            if self.queue.qsize() == self.size:  # Checking if the cache is full
                self.queue.get()  # Removing the oldest MemMap object from the cache
        self.queue.put(mm)  # Adding the MemMap object to the cache

    def get_ratio(self) -> float: 
        """
        Method to calculate the hit ratio of the cache.

        :return: Hit ratio of the cache.
        """
        return self.total_hits / (self.total_hits + self.total_misses) if self.total_hits + self.total_misses > 0 else 0.0

    def __str__(self) -> str: 
        """
        Method to return a string representation of the MemCache object.

        :return: String representation of the MemCache object.
        """
        return f"Process #: {self.process_number}, Hit Ratio: {self.get_ratio() * 100:.2f}%"  # Returning a formatted string with process_number and hit ratio.
