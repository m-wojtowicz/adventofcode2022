def moveFromTo(stack1, stack2, count):
  payload = []
  for i in range(count):
    crate = stack1.pop(0)
    payload.insert(0, crate)
  for i in range(len(payload)):
    stack2.insert(0, payload.pop(0))

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
  moveFromTo(stacks[int(command[3]) - 1], stacks[int(command[5]) - 1], int(command[1]))

result = ""
for stack in stacks:
  result += stack[0]
print(result)