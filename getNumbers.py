#getNumbers.py


def getNumbers():
    nums = [] # start with an empty list

    # sentinael loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = eval(xStr)
        nums.append(x) # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums