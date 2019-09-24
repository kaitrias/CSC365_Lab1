class student:
    stLastName = ""
    stFirstName = ""
    grade = 0
    classroom = 0
    bus = 0
    gpa = 0.0
    tLastName = ""
    tFirstName = ""

    def __init__(self, line):
        data = line.split(",")
        self.stLastName = data[0]
        self.stFirstName = data[1]
        self.grade = int(data[2])
        self.classroom = int(data[3])
        self.bus = int(data[4])
        self.gpa = float(data[5])
        self.tLastName = data[6]
        self.tFirstName = data[7]


students = []


def parseFile():
    file = open("students.txt", 'r')
    for line in file:
        students.append(student(line))



def main():
    parseFile()


if __name__ == "__main__":
    main()