def findMissed(arr):
    numbers = set(arr)  # convert to set to remove duplicates as it is a collection of unique elements
    length = len(arr)
    out = []
    # arr[-1] - last element
    for i in range(1, arr[-1]):
        if i not in numbers:
            out.append(i)

    return out


if __name__ == '__main__':
    listOfNum = [1, 2, 4, 6, 7, 8, 10, 13]
    print(findMissed(listOfNum))
