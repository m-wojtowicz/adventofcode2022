input_file = open("input.txt", "r")
input = input_file.readlines()
sum = 0
for line in input:
  first, second = line[:len(line)//2], line[len(line)//2:]
  first_set = set(first)
  for char_first in first_set:
    if char_first in second:
      print(char_first)
      if char_first <= 'Z':
        sum += ord(char_first) - ord('A') + 27
      else:
        sum += ord(char_first) - ord('a') + 1
print(sum)