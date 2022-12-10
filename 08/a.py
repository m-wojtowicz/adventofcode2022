input_file = open("input.txt", "r")
input = input_file.readlines()
size = 3
grid = [[False for i in range(len(input[0]) - 1)] for i in range(len(input))]

for i in range(len(input)):
  min = -1
  for j in range(len(input[i]) - 1):
    if int(input[i][j]) > min:
      min = int(input[i][j])
      grid[i][j] = True
  min = -1
  for j in range(len(input[i]) - 2, 0, -1):
    if int(input[i][j]) > min:
      min = int(input[i][j])
      grid[i][j] = True

for i in range(len(input[0]) - 2, 0, -1):
  min = -1
  for j in range(len(input)):
    if int(input[j][i]) > min:
      min = int(input[j][i])
      grid[j][i] = True
  min = -1
  for j in range(len(input) - 1, 0, -1):
    if int(input[j][i]) > min:
      min = int(input[j][i])
      grid[j][i] = True

count = 0
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j]:
      count += 1
print(count)