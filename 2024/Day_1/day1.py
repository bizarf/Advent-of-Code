# going to use numpy to create the lists
import numpy as np

# data = np.loadtxt("./example_data.txt")
data = np.loadtxt("./puzzle_data.txt")

first_col: list = []
second_col: list = []
total: list = []
similarity: list = []

# part 1
# sort the numbers into separate lists
for numbers in data:
    first_col.append(int(numbers[0]))
    second_col.append(int(numbers[1]))

first_col.sort()
second_col.sort()


# loop based on the length of the data. values have to result in a positive difference.
for i in range(len(data)):
    if first_col[i] > second_col[i]:
        total.append(first_col[i] - second_col[i])
    else:
        total.append(second_col[i] - first_col[i])

print(sum(total))

# part 2
for i in first_col:
    for j in second_col:
        if i == j:
            similarity.append(i)

print(sum(similarity))
