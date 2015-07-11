# selsort.py

def selSort(nums):
    # sort nums into ascending order

    n = len(nums)

    # for each position in the list (except the very last
    for bottom in range(n-1):
        # find the smallest item in nums[bottom] .. nums [n-1]

        mp = bottom # bottom is smallest at first
        for i in range(bottom+1,n):     # look at each position
            if nums[i] < nums[mp]:      # this one is smaller
                mp = i                  # remeber the index

        # swap smallest item to the bottom
        nums[bottom], nums[mp] = nums[mp], nums[bottom]