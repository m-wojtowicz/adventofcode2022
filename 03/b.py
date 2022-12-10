input_file = open("input.txt", "r")
input = input_file.readlines()
sum = 0
i = 0
while i in range(len(input)):
  set_1 = set(input[i])
  i += 1
  set_2 = set(input[i])
  i += 1
  set_3 = set(input[i])
  i += 1

  set_1.remove('\n')

  for char in set_1:
    if char in set_2 and char in set_3:
      if char <= 'Z':
        sum += ord(char) - ord('A') + 27
      else:
        sum += ord(char) - ord('a') + 1
print(sum)