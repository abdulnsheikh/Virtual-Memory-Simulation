<p align="center">
  <img src="https://raw.githubusercontent.com/abdulnsheikh/Virtual-Memory-Simulation/main/imageAssets/memory-stock-image.png" alt="Logo" style="border-radius: 50%;">
</p>


# Virtual Memory Simulation Program 

This is a Python-based virtual memory simulation program that takes in a memory map file and a list of cache sizes as input and simulates the caching behavior of each process in the memory map. The program uses the LRU (Least Recently Used) cache replacement policy and calculates the hit ratio for each cache and the average hit ratio across all caches.

## Usage 
To run the program, execute the Main.py file with the following command:
`python3 Main.py file_name.txt x1 x2 x3 x4`
## where 
`file_name.txt` is the name of the memory map file, 
and 
`x1`, `x2`, `x3`, `x4` are the cache sizes for each process in the memory map.

The program will output the hit ratio for each cache and the average hit ratio across all caches.
 
Authors
- [Abdulnaser Sheikh](https://github.com/abdulnsheikh/)

Acknowledgements
This project is developed as an assignment for the Operating Systems course at the 

`University of Nebraska Omaha`\
`College of Information Science and Technology`.

## License 

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
 