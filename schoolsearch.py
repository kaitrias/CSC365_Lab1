#Nadia Wohlfarth, Kai Trias, Karla Sunjara
#CSC 365. Fall 2019
#Lab 1-2 
def check_txt_file(line):
    data = line.strip().split(",")
    if len(data) != 6:
        exit(1)
    return data


def check_teachers_file(line):
    data = line.strip().split(",")
    if len(data) != 3:
        exit(1)
    return data


def find_teacher(classroom):
    try:
        file = open("teachers.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_teachers_file(line)
        if classroom == data[2].strip():
            return data

    print("Could not find teacher")
    exit(1)


def student_command_with_b(last_name):
    try:
        file = open("list.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if data[0] == last_name:
            print(data[0].strip()+","+data[1].strip()+","+data[4].strip())
    file.close()


def student_command_without_b(last_name):
    try:
        file = open("list.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if data[0].strip() == last_name:
            teacher = find_teacher(data[3].strip())
            print(data[0].strip()+","+data[1].strip()+","+data[2].strip()+","+data[3].strip()+","+teacher[0].strip()+","+teacher[1].strip())
    file.close()


def student_command(user_input):
    parsed_input = user_input.strip().split(" ")

    if len(parsed_input) == 1:
        student_command_without_b(parsed_input[0])

    if len(parsed_input) == 2:
        if parsed_input[1] == "B" or parsed_input[1] == "Bus":
            student_command_with_b(parsed_input[0])


def find_student(classroom):
    try:
        file = open("list.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if classroom == data[3].strip():
            print(data[0].strip() + "," + data[1].strip())


def teacher_command(user_input):
    parsed_input = user_input.strip().split(" ")
    if len(parsed_input) != 1:
        return

    last_name = parsed_input[0]

    try:
        file = open("teachers.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_teachers_file(line)
        if data[0].strip() == last_name:
            find_student(data[2].strip())
    file.close()

def grade_command_with_gpa(input):
    student_list = []
    gpa = 0.0
    try:
        file = open("list.txt", 'r')
    except IOError:
        exit(1)

    grade = input[0]
    flag = input[1]

    if flag == "H" or flag == "High":
        gpa = 0.0
        for line in file:
            data = check_txt_file(line)
            if grade == data[2].strip():
                if float(data[5]) > gpa:
                    gpa = float(data[5])
                    student_list.clear()
                    teacher = find_teacher(data[3].strip())
                    student_list.append(data[0].strip() + "," + data[1].strip() + "," + data[5].strip() + "," + teacher[0].strip() + "," + teacher[1].strip() + "," + data[4].strip())
                elif float(data[5]) == gpa:
                    teacher = find_teacher(data[3].strip())
                    student_list.append(data[0].strip() + "," + data[1].strip() + "," + data[5].strip() + "," + teacher[0].strip() + "," + teacher[1].strip() + "," + data[4].strip())
        for student in student_list:
            print(student)

    if flag == "L" or flag == "Low":
        gpa = 10.0
        for line in file:
            data = check_txt_file(line)
            if grade == data[2].strip():
                if float(data[5]) < gpa:
                    gpa = float(data[5])
                    student_list.clear()
                    teacher = find_teacher(data[3].strip())
                    student_list.append(data[0].strip() + "," + data[1].strip() + "," + data[5].strip() + "," + teacher[0].strip() + "," + teacher[1].strip() + "," + data[4].strip())
                elif float(data[5]) == gpa:
                    teacher = find_teacher(data[3].strip())
                    student_list.append(data[0].strip() + "," + data[1].strip() + "," + data[5].strip() + "," + teacher[0].strip() + "," + teacher[1].strip() + "," + data[4].strip())
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
            file = open("list.txt", 'r')
        except IOError:
            exit(1)

        for line in file:
            data = check_txt_file(line)
            if data[2].strip() == grade:
                print(data[0].strip() + "," + data[1].strip())
        file.close()

    if len(parsed_input) == 2:
        grade_command_with_gpa(parsed_input)


def bus_command(user_input):
    parsed_input = user_input.strip().split(" ")
    if len(parsed_input) != 1:
        return

    bus = parsed_input[0]

    try:
        file = open("list.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if data[4].strip() == bus:
            print(data[0].strip()+", "+data[1].strip() + "," + data[2].strip() + "," + data[3].strip())
    file.close()


def average_command(user_input):
    parsed_input = user_input.strip().split(" ")
    if len(parsed_input) != 1:
        return

    grade = parsed_input[0]

    total_gpa = 0
    num_students = 0

    try:
        file = open("list.txt", 'r')
    except IOError:
        exit(1)

    for line in file:
        data = check_txt_file(line)
        if data[2].strip() == grade:
            total_gpa += float(data[5])
            num_students += 1
    file.close()

    if num_students != 0:
        print(grade + "," + str(round(total_gpa/num_students, 2)))


def info_command():
    info_dict = {}

    try:
        file = open("list.txt", 'r')
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

def grade_analytics(analytics_dict):
   try:
      file = open("list.txt", 'r')
   except IOError:
      exit(1)
   for line in file:
      data = check_txt_file(line)
      if int(data[2]) not in analytics_dict:
         analytics_dict[int(data[2])] = [1, float(data[5])]
      else:
         total = 0.00
         analytics_dict[int(data[2])][0] += 1
         analytics_dict[int(data[2])][1] = float(analytics_dict[int(data[2])][1]) + float(data[5])
   file.close()
   return analytics_dict

def bus_analytics(analytics_dict):
   try:
      file = open("list.txt", 'r')
   except IOError:
      exit(1)
   for line in file:
      data = check_txt_file(line)
      if int(data[4]) not in analytics_dict:
         analytics_dict[int(data[4])] = [1, float(data[5])]
      else:
         total = 0.00
         analytics_dict[int(data[4])][0] += 1
         analytics_dict[int(data[4])][1] = float(analytics_dict[int(data[4])][1]) + float(data[5])
   file.close()
   return analytics_dict
def teacher_analytics(analytics_dict):
   try: 
      file = open("list.txt", 'r')
   except IOError:
      exit(1)
   for line in file:
      data = check_txt_file(line)
      if int(data[3]) not in analytics_dict:
         analytics_dict[int(data[3])] = [1, float(data[5])]
      else:   
         analytics_dict[int(data[3])][0] += 1
         analytics_dict[int(data[3])][1] = float(analytics_dict[int(data[3])][1]) + float(data[5])
   file.close()
   return analytics_dict
def find_teacher(key, analytics_dict):
   try:
      file = open("teachers.txt", 'r')
   except IOError:
      exit(1)
   for line in file:
      data = check_teachers_file(line)
      if key == int(data[2]):
         print(str(data[0]) + ": " + str(round(analytics_dict[key][1]/analytics_dict[key][0], 2)))
         return
   file.close()
def analytics(user_input):
   parsed_input = user_input.strip().split(" ")
   if len(parsed_input) != 1:
      return
   analytics_dict = {}
   if (parsed_input[0] == "G"):
      analytics_dict = grade_analytics(analytics_dict)
      for key in sorted(analytics_dict.keys()):
         print(str(key) + ": " + str(round(analytics_dict[key][1]/analytics_dict[key][0], 2)))
   elif (parsed_input[0] == "B"):
      analytics_dict = bus_analytics(analytics_dict)
      for key in sorted(analytics_dict.keys()):
         print(str(key) + ": " + str(round(analytics_dict[key][1]/analytics_dict[key][0], 2)))
   elif (parsed_input[0] == "T"):
      analytics_dict = teacher_analytics(analytics_dict)
      for key in sorted(analytics_dict.keys()):
         find_teacher(key, analytics_dict)
         #print(str(key) + ": " + str(round(analytics_dict[key][1]/analytics_dict[key][0], 2)))
   return
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
    elif command == "Analytics":
        analytics(parsed_input[1])
    else:
        return


def main():
    while (1):
       userinput = input("Input a search command: ")
       parseinstruction(userinput)
if __name__ == "__main__":
    main()

