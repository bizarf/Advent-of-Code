import re

# with open("./example_data.txt", "r") as f:
#     lines = f.read()
#     lines = lines.replace("\n", "")

# the puzzle data has newlines in it. use replace to remove the newlines or else the output will be in multiple lists
with open("./puzzle_data.txt", "r") as f:
    lines = f.read()
    lines = lines.replace("\n", "")


# part 1
def mul(a, b):
    return a * b


string_search_result = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", lines)

total: int = 0

# loop through the list to go through each function individually. remove mul and the rounds brackets. add up the total by sending the numbers to the mul function above
for func in string_search_result:
    nums_only: str = func.replace("mul(", "").replace(")", "").replace(",", " ").split()
    total = total + mul(int(nums_only[0]), int(nums_only[1]))

print(total)
