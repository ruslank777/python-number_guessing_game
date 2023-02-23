# Mean
list1 = [12, 16, 18, 18, 12, 30, 25, 20, 23, 26, 20]
mean = sum(list1)/len(list1)
print("Mean: ", mean)

# Median
list2 = [12, 16, 18, 18, 12, 30, 25, 20, 23, 26, 20, 13]
list2.sort()
print(list2)

if len(list2) % 2 == 0:
    m1 = list2[len(list2)//2]
    print(m1)
    m2 = list2[len(list2)//2 - 1]
    print(m2)
    median = (m1+m2)/2
else:
    median = list2[len(list2)//2]
print("Median: ", median)

# Mode
list3 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list3:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print("Mode: ", mode)
