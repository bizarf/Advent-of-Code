# reading the file and then putting them into a list. numpy doesn't like data with different lengths
with open("./puzzle_data.txt", "r") as f:
    lines = f.readlines()

# create a list of lists to store the sequences
data: list = []
for line in lines:
    sequence = [int(num) for num in line.strip().split()]
    data.append(sequence)

# part 1. trying to find out which reports are safe


# the first step is to check the lists to see which are safe. safe lists are either ascending or descending. no duplicate values either.
def checkAscending(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def checkDescending(arr):
    return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))


# create a list to store the results
report_results: list = []
num_of_safe_reports: int = 0

# loop through each list and check if they are within the safe distance of either 1, 2, or 3
for num in data:
    if checkAscending(num) or checkDescending(num):
        total = []
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                diff = num[i] - num[i + 1]
                total.append(diff == 1 or diff == 2 or diff == 3)
            else:
                diff = num[i + 1] - num[i]
                total.append(diff == 1 or diff == 2 or diff == 3)
        report_results.append(total)


# need to now check the report_results lists to see if they are all true. if a list is true, then increase the number of safe reports
def checkSame(list):
    return all(i == list[0] for i in list)


for result in report_results:
    if checkSame(result):
        num_of_safe_reports = num_of_safe_reports + 1


print(num_of_safe_reports)
