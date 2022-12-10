def check_cycles(cycles, x):
  if x - 1 <= cycles % 40 and x + 1 >= cycles % 40:
    return "#"
  return "."

input_file = open("input.txt", "r")
input = input_file.readlines()
cycles = 0
x = 1
display = ""
for line in input:
  operation = line.strip().split(' ')
  if operation[0] == "noop":
    display += check_cycles(cycles, x)
    cycles += 1
  elif operation[0] == "addx":
    display += check_cycles(cycles, x)
    cycles += 1
    display += check_cycles(cycles, x)
    cycles += 1
    x += int(operation[1])

for i in range(len(display)):
  if i > 0 and i % 40 == 0:
    print("")
  print(display[i], end="")