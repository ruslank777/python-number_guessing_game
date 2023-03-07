inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputLists = []


def group_same_indexes(arr):
    # Define the groups by getting the length of sub-arrays
    amount_of_groups = len(arr[0])

    # iterate over each group and feed it with appropriate values from the incoming array

    for i in range(amount_of_groups):
        # append new sub-array to output
        print("i: ", i)
        outputLists.append([])
        # iterate over the incoming array to detect and feed the sub-array with appropriate values
        for j in inputLists:
            outputLists[i].append(j[i])

    a, b, c = outputLists[0], outputLists[1], outputLists[2]
    print(a, b, c)


if __name__ == "__main__":
    groupSameIndeces(inputLists)


