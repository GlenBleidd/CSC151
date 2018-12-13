import csv
# import fileinput


def menu():
    print("\nWhat to do: ")
    print("[1] - Display Students List")
    print("[2] - Add Student")
    print("[3] - Delete Student by ID")
    print("[4] - Update List")
    print("[5] - Exit")


def display():
    print("\nCurrent Student List\n")
    with open('student_list.csv') as d_file:
        student = csv.reader(d_file)
        for row in student:
            print', '.join(row)
    d_file.close()


def add():
    print("Input the Student's Information")
    with open('student_list.csv', 'a') as a_file:
        a_writer = csv.writer(a_file)
        id_num = raw_input("ID #: ")
        f_name = raw_input("First Name: ")
        l_name = raw_input("Last Name: ")
        course = raw_input("Course: ")
        year = raw_input("Year: ")
        gender = raw_input("Gender: ")
        a_writer.writerow([id_num, f_name, l_name, course, year, gender])
    a_file.close()


def delete():
    arr = []
    del_id = raw_input("Input the ID Number: ")
    d_file = open('student_list.csv', 'r')
    for line in d_file:
        x = line.split(',')
        idnum = x[0]
        if idnum == del_id:
            print "Student Deleted"
        else:
            arr.append(line)
            
            opt_del = open('student_list.csv', 'w')
            opt_del.writelines(arr)
            opt_del.close()


def update():
    upd = raw_input("\nEnter ID #: ")
    u_file = open('student_list.csv', 'r')
    arr = []
    for line in u_file:
        x = line.split(',')
        idnum = x[0]
        if idnum == upd:
            print "\nStudent: " + line
            try:
                edit = int(raw_input("What do you want to change: "
                                     "\n[1]-ID Number"
                                     "\n[2]-First Name"
                                     "\n[3]-Last Name"
                                     "\n[4]-Course"
                                     "\n[5]-Year Level"
                                     "\n[6]-Gender"
                                     "\n[7]-Go Back"
                                     "\n\n>>>"))
            except ValueError:
                print 'Sorry that is not a number'
                update()
                continue

            else:
                if edit in range(1, 7):
                    if edit == 1:
                        n_idnum = raw_input("New ID #: ")
                        arr.append(n_idnum + ',' + x[1] + ',' + x[2] + ',' + x[3] + ',' + x[4] + ',' + x[5])
                    elif edit == 2:
                        n_fname = raw_input("New First Name: ")
                        arr.append(x[0] + ',' + n_fname + ',' + x[2] + ',' + x[3] + ',' + x[4] + ',' + x[5])
                    elif edit == 3:
                        n_lname = raw_input("New Last Name: ")
                        arr.append(x[0] + ',' + x[1] + ',' + n_lname + ',' + x[3] + ',' + x[4] + ',' + x[5])
                    elif edit == 4:
                        n_course = raw_input("New Course: ")
                        arr.append(x[0] + ',' + x[1] + ',' + x[2] + ',' + n_course + ',' + x[4] + ',' + x[5])
                    elif edit == 5:
                        n_year = raw_input("New Year Level: ")
                        arr.append(x[0] + ',' + x[1] + ',' + x[2] + ',' + x[3] + ',' + n_year + ',' + x[5])
                    elif edit == 6:
                        n_gender = raw_input("New Gender: ")
                        arr.append(x[0] + ',' + x[1] + ',' + x[2] + ',' + x[3] + ',' + x[4] + ',' + n_gender)
                    elif edit == 8:
                        menu()
        else:
            arr.append(line)

    u_file.close()
    opt_del = open('student_list.csv', 'w')
    opt_del.writelines(arr)
    opt_del.close()


menu()

while True:
    try:
        answer = int(raw_input("Input Selection: "))
    except ValueError:
        print "Error! please input a number."
        menu()
        continue

    else:
        if answer in range(1, 5):
            if answer == 1:
                display()
                menu()
            elif answer == 2:
                add()
                menu()
            elif answer == 3:
                delete()
                menu()
            elif answer == 4:
                update()
                menu()
            elif answer == 5:
                break
        else:
            print "Not an option, please select an option!"
            menu()
