input_file = open("input.txt", "r")
input = input_file.read().strip()
for i in range(len(input)):
  chars = set()
  for j in range(i, i+14):
    chars.add(input[j])
  if len(chars) == 14:
    print(i+14)
    break
  