#printfile2.py
# Prints the first 5 lines of a file

def main():
    fname = input("Enter a filename: ")
    infile = open(fname, "r")
    for i in range(5):
        line = infile.readline()
        print(line[:-1])

main()