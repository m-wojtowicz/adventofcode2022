input_file = open("input.txt", "r")
input = input_file.readlines()
sums = []
sum = 0
for line in input:
  if line == "\n":
    sums.append(sum)
    sum = 0
  else:
    sum += int(line)

print(max(sums))