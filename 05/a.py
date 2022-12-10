def moveFromTo(stack1, stack2):
  crate = stack1.pop(0)
  stack2.insert(0, crate)

input_file = open("input.txt", "r")
input = input_file.readlines()

max = 0
for line in input:
  nums = line.strip().split("   ")
  if max < len(nums):
    max = len(nums)
  if "move" in nums[0]:
    break
stacks = [[] for i in range(max)]

for line in input:
  row = line.replace("    ", ",").strip().replace("[", "").replace("]", "").replace(" ", "")
  if "1" in row[0]:
    break
  for i in range(len(row)):
    if row[i] != ',':
      stacks[i].append(row[i])

for line in input:
  if "move" not in line:
    continue
  command = line.strip().split(' ')
  for i in range(int(command[1])):
    moveFromTo(stacks[int(command[3]) - 1], stacks[int(command[5]) - 1])

result = ""
for stack in stacks:
  result += stack[0]
print(result)