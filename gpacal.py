# gpacal.py
# A program to find the student with the best gpa

from gpa import Student



def main():
        # open the input file for reading
        filename = input("Enter the name of the grade file: ")
        infile = open(filename, 'r')

        # set best to the record for the first student in the file
        best = makeStudent(infile.readline())

        # process subsequent lines of the file
        for line in infile:
            # turn the line into a student record
            s = makeStudent(line)
            # if this student is best so far, remember it.
            if s.gpa() > best.gpa():
                best = s
        infile.close()

        # print information about the best student
        print("The best student is:", best.getName())
        print("hours:", best.getHours())
        print("GPA:", best.gpa())

if __name__ == '__main__':
    main()
