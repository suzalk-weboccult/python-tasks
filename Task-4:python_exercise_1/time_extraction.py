"""
This module provides functionality to extract components from a timestamp.

Functions:
- year(timestamp): Extracts the year from the timestamp.
- month(timestamp): Extracts the month from the timestamp.
- date(timestamp): Extracts the date from the timestamp.
- time(timestamp): Extracts the time from the timestamp.
"""

# Lambda functions to extract components from a timestamp
year = lambda x: x[0:4]   # Extracts the year
month = lambda x: x[5:7]  # Extracts the month
date = lambda x: x[8:10]  # Extracts the date
time = lambda x: x[11:]   # Extracts the time

# Take user input for the timestamp
timestamp = input("Enter the timestamp in the format 'YYYY-MM-DD HH:mm:SS.ssssss': ")

# Extract and print individual components
print("Year:", year(timestamp))
print("Month:", month(timestamp))
print("Date:", date(timestamp))
print("Time:", time(timestamp))
