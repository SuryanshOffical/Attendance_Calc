# Project Statement

## Problem Statement

Students often need to keep track of their attendance and determine whether they can meet the minimum attendance requirement for their courses. Manually calculating the number of lectures that must be attended or can be missed can become difficult, especially when dealing with multiple courses.

The Attendance Calculator provides a simple command-line solution that performs these calculations and helps students understand their attendance situation.

---

## Scope

The project focuses on calculating and monitoring attendance requirements for multiple courses.

The system:

- Accepts course and attendance information from the user.
- Calculates the number of lectures remaining.
- Calculates the minimum number of remaining lectures that need to be attended.
- Calculates the number of lectures that can still be missed.
- Determines the attendance status of each course.
- Provides a summary of all entered courses.
- Validates user input to prevent invalid attendance data.

The current version is a command-line application and does not permanently store attendance data or connect to external college/university attendance systems.

---

## Target Users

The primary target users are:

- School and college students.
- University students.
- Students who need to monitor minimum attendance requirements across multiple courses.

---

## High-Level Features

- Multi-course attendance calculation.
- Minimum required lecture calculation.
- Remaining lecture calculation.
- Number of lectures that can be missed.
- Current and maximum possible attendance calculation.
- Attendance status classification:
  - Safe
  - Caution
  - Danger
  - Failed
- Input validation and error handling.
- Final attendance summary.
- Built-in testing for calculation and status logic.