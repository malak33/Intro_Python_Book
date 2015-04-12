#printfile.py
# Prints a fle to the screen

def main():
    fname = input("Enter filename")
    infile = open(fname,"r")
    data = infile.read()
    print(data)

main()