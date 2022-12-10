def check_cycles(cycles, x):
  if cycles <= 220 and cycles % 40 == 20:
    return cycles * x
  return 0

input_file = open("input.txt", "r")
input = input_file.readlines()
sum = 0
cycles = 0
x = 1
for line in input:
  operation = line.strip().split(' ')
  if operation[0] == "noop":
    cycles += 1
    sum += check_cycles(cycles, x)
  elif operation[0] == "addx":
    cycles += 1
    sum += check_cycles(cycles, x)
    cycles += 1
    sum += check_cycles(cycles, x)
    x += int(operation[1])
print(sum)