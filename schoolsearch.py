#Nadia Wohlfarth, Kai Trias, Karla Sunjara
#CSC 365. Fall 2019
#Lab 1-1 
def check_txt_file(line):
    data = line.strip().split(",")
    if len(data) != 8:
        exit(1)
    return data


def student_command_with_b(last_name):
    try:
        file = open("students.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if data[0] == last_name:
            print(data[0]+","+data[1]+","+data[4])
    file.close()


def student_command_without_b(last_name):
    try:
        file = open("students.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if data[0] == last_name:
            print(data[0]+","+data[1]+","+data[2]+","+data[3]+","+data[6]+","+data[7])
    file.close()


def student_command(user_input):
    parsed_input = user_input.strip().split(" ")

    if len(parsed_input) == 1:
        student_command_without_b(parsed_input[0])

    if len(parsed_input) == 2:
        if parsed_input[1] == "B" or parsed_input[1] == "Bus":
            student_command_with_b(parsed_input[0])


def teacher_command(user_input):
    parsed_input = user_input.strip().split(" ")
    if len(parsed_input) != 1:
        return

    last_name = parsed_input[0]

    try:
        file = open("students.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if data[6] == last_name:
            print(data[0]+","+data[1])
    file.close()


def grade_command_with_gpa(input):
    student_list = []
    gpa = 0.0
    try:
        file = open("students.txt", 'r')
    except IOError:
        exit(1)

    grade = input[0]
    flag = input[1]

    if flag == "H" or flag == "High":
        gpa = 0.0
        for line in file:
            data = check_txt_file(line)
            if grade == data[2]:
                if float(data[5]) > gpa:
                    gpa = float(data[5])
                    student_list.clear()
                    student_list.append(data[0] + "," + data[1] + "," + data[5] + "," + data[6] + "," + data[7] + "," + data[4])
                elif float(data[5]) == gpa:
                    student_list.append(data[0] + "," + data[1] + "," + data[5] + "," + data[6] + "," + data[7] + "," + data[4])
        for student in student_list:
            print(student)

    if flag == "L" or flag == "Low":
        gpa = 10.0
        for line in file:
            data = check_txt_file(line)
            if grade == data[2]:
                if float(data[5]) < gpa:
                    gpa = float(data[5])
                    student_list.clear()
                    student_list.append(data[0] + "," + data[1] + "," + data[5] + "," + data[6] + "," + data[7] + "," + data[4])
                elif float(data[5]) == gpa:
                    student_list.append(data[0] + "," + data[1] + "," + data[5] + "," + data[6] + "," + data[7] + "," + data[4])
        for student in student_list:
            print(student)

    file.close()


def grade_command(user_input):
    parsed_input = user_input.strip().split(" ")

    if len(parsed_input) != 1 and len(parsed_input) != 2:
        return

    grade = parsed_input[0]

    if len(parsed_input) == 1:
        try:
            file = open("students.txt", 'r')
        except IOError:
            exit(1)

        for line in file:
            data = check_txt_file(line)
            if data[2] == grade:
                print(data[0] + "," + data[1])
        file.close()

    if len(parsed_input) == 2:
        grade_command_with_gpa(parsed_input)


def bus_command(user_input):
    parsed_input = user_input.strip().split(" ")
    if len(parsed_input) != 1:
        return

    bus = parsed_input[0]

    try:
        file = open("students.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if data[4] == bus:
            print(data[0]+", "+data[1] + "," + data[2] + "," + data[3])
    file.close()


def average_command(user_input):
    parsed_input = user_input.strip().split(" ")
    if len(parsed_input) != 1:
        return

    grade = parsed_input[0]

    total_gpa = 0
    num_students = 0

    try:
        file = open("students.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if data[2] == grade:
            total_gpa += float(data[5])
            num_students += 1
    file.close()

    if num_students != 0:
        print(grade + "," + str(round(total_gpa/num_students, 2)))


def info_command():
    info_dict = {}

    try:
        file = open("students.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if int(data[2]) not in info_dict:
            info_dict[int(data[2])] = 1
        else:
            info_dict[int(data[2])] += 1
    file.close()

    for key in sorted(info_dict.keys()):
        print(str(key) + ": " + str(info_dict[key]))

def parseinstruction(userinput):
    parsed_input = userinput.split(":")
   
    if parsed_input[0] == "I" or parsed_input[0] == "Info":
        if len(parsed_input) == 1:
           info_command()
           return
    elif parsed_input[0] == "Q" or parsed_input[0] == "Quit":
        if len(parsed_input) == 1:
           exit(0)
        return

    if len(parsed_input) != 2:
        return

    command = parsed_input[0]
    if command == "S" or command == "Student":
        student_command(parsed_input[1])
    elif command == "T" or command == "Teacher":
        teacher_command(parsed_input[1])
    elif command == "G" or command == "Grade":
        grade_command(parsed_input[1])
    elif command == "B" or command == "Bus":
        bus_command(parsed_input[1])
    elif command == "A" or command == "Average":
        average_command(parsed_input[1])
    else:
        return


def main():
    while (1):
       userinput = input("Input a search command: ")
       parseinstruction(userinput)
if __name__ == "__main__":
    main()

