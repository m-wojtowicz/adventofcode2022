input_file = open("input.txt", "r")
input = input_file.readlines()
sums = []
sum = 0
total = 0
for line in input:
  if line == "\n":
    sums.append(sum)
    sum = 0
  else:
    sum += int(line)

for i in range(0, 3):
  total += max(sums)
  sums.remove(max(sums))
print(total)