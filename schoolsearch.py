def student_command(user_input):
    parsed_input = user_input.strip().split(" ")
    if len(parsed_input) != 1:
        return

    last_name = parsed_input[0]

    file = open("students.txt", 'r')
    for line in file:
        data = line.strip().split(",")
        if data[0] == last_name:
            print(data[0]+", "+data[1]+", "+data[2]+", "+data[3]+", "+data[6]+", "+data[7])
    file.close()


def teacher_command(user_input):
    parsed_input = user_input.strip().split(" ")
    if len(parsed_input) != 1:
        return

    last_name = parsed_input[0]

    file = open("students.txt", 'r')
    for line in file:
        data = line.strip().split(",")
        if data[6] == last_name:
            print(data[0]+", "+data[1])
    file.close()


def grade_command(user_input):
    parsed_input = user_input.strip().split(" ")

    if len(parsed_input) != 1 and len(parsed_input) != 2:
        return

    grade = parsed_input[0]

    if len(parsed_input) == 1:
        file = open("students.txt", 'r')
        for line in file:
            data = line.split(",")
            if data[2] == grade:
                print(data[0] + ", " + data[1])
        file.close()

    if len(parsed_input) == 2:
        output = ""
        gpa = 0.0

        file = open("students.txt", 'r')
        data = file.readline().strip().split(",")
        file.readline()
        output = data[0] + ", " + data[1] + ", " + data[5] + ", " + data[6] + ", " + data[7] + ", " + data[4]
        gpa = float(data[5])

        if parsed_input[1] == "H" or parsed_input[1] == "High":
            for line in file:
                data = line.strip().split(",")
                if data[2] == grade:
                    if float(data[5]) > gpa:
                        output = data[0] + ", " + data[1] + ", " + data[5] + ", " + data[6] + ", " + data[7] + ", " + data[4]
                        gpa = float(data[5])
            print(output)

        if parsed_input[1] == "L" or parsed_input[1] == "Low":
            for line in file:
                data = line.strip().split(",")
                if data[2] == grade:
                    if float(data[5]) < gpa:
                        output = data[0] + ", " + data[1] + ", " + data[5] + ", " + data[6] + ", " + data[7] + ", " + data[4]
                        gpa = float(data[5])
            print(output)

        file.close()


def bus_command(user_input):
    parsed_input = user_input.strip().split(" ")
    if len(parsed_input) != 1:
        return

    bus = parsed_input[0]

    file = open("students.txt", 'r')
    for line in file:
        data = line.strip().split(",")
        if data[4] == bus:
            print(data[0]+", "+data[1] + ", " + data[2] + ", " + data[3])
    file.close()


# in-progress
def average_command(user_input):
    parsed_input = user_input.strip().split(" ")
    if len(parsed_input) != 1:
        return

    grade = parsed_input[0]

    total_gpa = 0
    num_students = 0

    file = open("students.txt", 'r')
    for line in file:
        data = line.strip().split(",")
        if data[2] == grade:
            total_gpa += float(data[5])
            num_students += 1
    file.close()

    if num_students != 0:
        print(grade + ", " + str(round(total_gpa/num_students, 2)))


def info_command():
    return


def quit_command():
    return


def parseinstruction(userinput):
    parsed_input = userinput.split(":")

    if parsed_input[0] == "I":
        info_command()
        return
    elif parsed_input[0] == "Info":
        info_command()
        return
    elif parsed_input[0] == "Q":
        quit_command()
        return
    elif parsed_input[0] == "Quit":
        quit_command()
        return

    if len(parsed_input) != 2:
        return

    command = parsed_input[0]
    if command == "S":
        student_command(parsed_input[1])
    elif command == "Student":
        student_command(parsed_input[1])
    elif command == "T":
        teacher_command(parsed_input[1])
    elif command == "Teacher":
        teacher_command(parsed_input[1])
    elif command == "G":
        grade_command(parsed_input[1])
    elif command == "Grade":
        grade_command(parsed_input[1])
    elif command == "B":
        bus_command(parsed_input[1])
    elif command == "Bus":
        bus_command(parsed_input[1])
    elif command == "A":
        average_command(parsed_input[1])
    elif command == "Average":
        average_command(parsed_input[1])
    else:
        return


def main():
    while 1:
        userinput = input()
        parseinstruction(userinput)



if __name__ == "__main__":
    main()

