def twoSum(arr, target):
    for i in arr:
        for j in arr:
            if(i+j == target):
                print(i, j)


twoSum([1, 2, 3, 4], 7)
