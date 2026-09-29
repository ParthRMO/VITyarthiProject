
# VITyarthi - Student Management System

VITyarthi is a simple **Python-based Student Management System** designed to make basic student data easier to manage and access.

The project is a **console-based application** where users can add students, search for students, manage attendance, enter marks, and calculate grades.

## Features

### 1. Student Management

* Add a new student
* Prevent duplicate student IDs
* View all registered students
* Search for a student using their ID
* Store basic student information:

  * Student ID
  * Name
  * Course
  * Semester

### 2. Attendance Management

* Mark students as Present or Absent
* Keep track of total classes
* Calculate attendance percentage
* Display:

  * Total classes
  * Classes attended
  * Classes missed
  * Attendance percentage

### 3. Academic Performance

* Enter marks out of 100
* Validate marks between 0 and 100
* Automatically calculate grades based on marks

### 4. Grade Calculation

The current grading system is:

|    Marks | Grade |
| -------: | :---: |
| 90 - 100 |   A+  |
|  80 - 89 |   A   |
|  70 - 79 |   B   |
|  60 - 69 |   C   |
|  50 - 59 |   D   |
| Below 50 |   F   |

## Menu Options

When the program starts, the following menu is displayed:

```text
STUDENT MANAGEMENT SYSTEM

1. Add Student
2. View students
3. Search Student
4. Mark Attendance
5. Calculate Attendance
6. Enter Marks
7. Calculate Grade
8. Exit
```

## Technologies Used

* **Python 3**
* Python dictionaries
* Python lists
* Functions
* Loops
* Conditional statements
* Exception handling
* Console-based input/output

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd VITyarthiProject
```

### 3. Run the Python program

```bash
python project.py
```

If your system uses `python3`, use:

```bash
python3 project.py
```

## Example

### Adding a Student

```text
--- Add student----

Enter student ID: 101
Enter your name: Rahul
Enter your course: CSE
Enter your semester: 1

Student added successfully!!
```

### Marking Attendance

```text
---Mark Attendance---

Enter Student ID: 101
Enter P/A: P

Marked present!
```

### Calculating Attendance

```text
---Attendance---

Enter the ID: 101

total classes: 5
present: 4
absent: 1
Attendance: 80.0 %
```

### Calculating Grade

```text
---Grade---

Enter the ID: 101

Marks: 85.0
Grade: A
```

## Project Structure

```text
VITyarthiProject/
│
├── project.py
└── README.md
```

## How the Project Works

The program stores student information using a **list of dictionaries**.

Each student is represented like this:

```python
student = {
    "id": stu_id,
    "name": name,
    "course": course,
    "semester": semester,
    "present": 0,
    "total": 0,
    "marks": 0
}
```

The list stores multiple student records:

```python
students = []
```

Functions are then used to perform different operations on this data, such as adding students, searching for students, recording attendance, and calculating grades.

## Input Validation

The project includes basic input validation.

For example, student IDs must be entered as integers:

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")
```

The program also checks:

* Duplicate student IDs
* Valid attendance input (`P` or `A`)
* Marks between 0 and 100
* Whether a student exists before performing operations

## Current Limitations

This is a beginner-level console project, so there are some limitations:

* Student data is stored only while the program is running.
* Data is lost when the program is closed.
* There is no graphical user interface.
* There is no database integration.
* Attendance is currently recorded one class at a time.
* Marks are stored as a single value rather than subject-wise marks.

## Future Improvements

Some planned improvements for the project include:

* [ ] Add file-based data storage
* [ ] Add database support
* [ ] Add subject-wise marks
* [ ] Add multiple attendance subjects
* [ ] Generate complete student reports
* [ ] Add an attendance report
* [ ] Add a graphical user interface
* [ ] Add login/authentication
* [ ] Add student update and delete options
* [ ] Improve input validation
* [ ] Add data export functionality

## Learning Goals

This project was created to practice fundamental Python programming concepts, including:

* Variables and data types
* Lists and dictionaries
* Functions
* Loops
* Conditional statements
* Exception handling
* User input
* Basic program structure
* Working with student records

Author

Parth Mohire

CSE Core Engineering
VIT Bhopal

