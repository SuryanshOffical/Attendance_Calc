# Attendance_Calc

A Python-based attendance calculator that helps calculate mandatory attendance requirements for multiple courses.

## Features:

- Supports multiple courses
- Takes total course lectures as input
- Takes lectures attended and missed so far as input
- Allows a custom mandatory attendance percentage
- Calculates remaining number of lectures
- Calculates the minimum number of future lectures that need to be attended
- Calculates how many remaining lectures can be missed
- Provides an attendance status
- Displays a summary of all the courses

## Requirements:

- Python 3.x
- No external Python libraries are required

## Setup

1. Clone the repository:

   git clone https://github.com/YourUsername/attendance-calculator.git

2. Enter the project directory:

   cd attendance-calculator

3. Make sure Python 3.x is installed:

   python --version

## Running the Program

Run the following command:

   python attendance_calculator.py

The program will ask for the number of courses and then collect the attendance information for each course.

## Input Information

For each course, the program requires:

- Course name
- Total number of lectures in the course
- Number of lectures attended so far
- Number of lectures not attended so far
- Mandatory overall attendance percentage

## Output

The program displays:

- Current overall attendance percentage
- Number of lectures remaining
- Minimum lectures that need to be attended
- Number of lectures that can still be missed
- Attendance status
- Final attendance summary for all courses