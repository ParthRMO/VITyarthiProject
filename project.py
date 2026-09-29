#My VITyarthi project
#making a platform for easier access to the student data
'''
Main modules
1. Student Management
* Add student
* Search student

2. Attendance
* Mark attendance
* Calculate percentage

3. Academic Performance
* Marks
* Grade calculation

4. Reports
* Attendance report
'''
students=[]

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

#adding student
def add_stu():
    print("\n--- Add student----")
    stu_id = get_int("Enter student ID: ")

    for s in students:
        if s["id"]==stu_id:
            print("Student already exists!")
            return
        
    name = input("Enter your name: ")
    course =input ("Enter your course:")
    semester = input("Enter your semester: ")

    student={
        "id": stu_id,
        "name":name,
        "course":course,
        "semester":semester,
        "present":0,
        "total":0,
        "marks":0
    }

    students.append(student)

    print("Student added successfully!!")


#Viewing added students

def view_stu():
    print("\n---All students---")

    if len(students)==0:
        print("No students found!")

    else:
        for student in students:

            print("\nStudent ID:",student["id"])
            print("\nName:",student["name"])
            print("\nCourse:",student["course"])
            print("\nSemester:",student["semester"])

            print("-------------------------")


#searching the student
def search_stu():

    print('\n---Search student---')

    student_id= get_int("Enter student ID:")
    found = False

    for student in students:
        if student["id"]==student_id:
            print('\nStudent Found!!')

            print("ID:",student["id"])
            print("Name:",student["name"])
            print("Course:",student["course"])
            print("Semester:",student["semester"])

            found=True

    if found==  False:
        print('Student not found.')


#marking the attendance

def mark_attend():
    print('\n---Mark Attendance---')

    student_id=get_int('Enter Student ID:')

    found = False

    for student in students:
        if student['id']==student_id:
            status =input('Enter P/A:').upper()

            if status=="P":
                student['present']+=1
                student['total']+=1

                print('Marked present!')

            elif status=='A':
                student['total']+=1

                print('Marked absent')

            else:
                print("Only P/A is allowed for input!")

            found= True
    if found==False:
        print("Student not registered")


#Calculating the attendance

def calc_attend():

    print("\n---Attendance---")

    student_id=get_int("Enter the ID:")

    found= False

    for student in students:
        if student["id"]==student_id:
            found= True
            if student['total']==0:
                print('no attendance recorded')

            else :
                percentage=(student["present"]/student["total"]*100)

                print("\ntotal classes:",student["total"])
                print("\npresent:",student["present"])
                print("\nabsent:",student["total"]-student['present'])
                print("Attendance:",round(percentage,2),"%")

            

    if found==False:
        print("Student not found.")


#Enter Marks

def enter_marks():
    print("\n---Enter marks---")

    student_id=get_int("Enter the ID:")

    found=False

    for student in students:
        if student["id"]==student_id:

            marks=float(input("Enter Marks out of 100:"))

            if marks>=0 and marks<=100:
                student["marks"]=marks

                print("Marks Entered successfully!")

            else:
                print("Marks must be in between 0 to 100.")

            found = True

    if found== False:
        print("Student not found.")


#Calculating grade

def calc_grade():
    print("\n---Grade---")

    student_id=get_int("Enter the ID:")

    found= False

    for student in students :

        if student["id"]==student_id:

            marks=student["marks"]

            if marks>=90:
                grade="A+"

            elif marks>=80:
                grade="A"

            elif marks>=70:
                grade="B"

            elif marks>=60:
                grade="C"

            elif marks>=50:
                grade="D"

            else:
                grade="F"

            print("\nMarks:",marks)
            print("Grade:",grade)

            found= True

    if found== False:
        print("student not found!")


#Main menu designing

while True:

    print("\n")
    print("STUDENT MANAGEMENT SYSTEM")

    print("1.Add Student")
    print("2.View students")
    print("3.Search Student")
    print("4.Mark Attendance")
    print("5.Calculate Attendance")
    print("6.Enter Marks")
    print("7.Calculate Grade")
    print("8.Exit")

    choice=input("\nEnter Your Choice:")

    if choice=="1":
        add_stu()

    elif choice=="2":
        view_stu()

    elif choice=="3":
        search_stu()

    elif choice=="4":
        mark_attend()

    elif choice=="5":
        calc_attend()

    elif choice=="6":
        enter_marks()

    elif choice=="7":
        calc_grade()

    elif choice=="8":
        print("Thank you!!")
        break

    else:
        print("invalid input!")
    