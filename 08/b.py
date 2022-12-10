input_file = open("input.txt", "r")
input = input_file.readlines()
size = 3
grid = [[0 for i in range(len(input[0]) - 1)] for i in range(len(input))]

for i in range(len(input)):
  for j in range(len(input[i]) - 1):
    sum = 1
    count = 0
    for k in range(j + 1, len(input[i]) - 1):
      if int(input[i][k]) >= int(input[i][j]):
        count += 1
        break
      count += 1
    if count == 0:
      count = 1
    sum *= count
    count = 0
    for k in range(j - 1, -1, -1):
      if int(input[i][k]) >= int(input[i][j]):
        count += 1
        break
      count += 1
    if count == 0:
      count = 1
    sum *= count
    count = 0
    for k in range(i + 1, len(input)):
      if int(input[k][j]) >= int(input[i][j]):
        count += 1
        break
      count += 1
    if count == 0:
      count = 1
    sum *= count
    count = 0
    for k in range(i - 1, -1, -1):
      if int(input[k][j]) >= int(input[i][j]):
        count += 1
        break
      count += 1
    if count == 0:
      count = 1
    sum *= count
    grid[i][j] = sum

max = 0
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] > max:
      max = grid[i][j]
print(max)