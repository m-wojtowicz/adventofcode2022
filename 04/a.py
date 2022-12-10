input_file = open("input.txt", "r")
input = input_file.readlines()
count = 0
for line in input:
  first, second = line.split(',')
  first_range = first.split('-')
  second_range = second.split('-')

  first_set = set()
  second_set = set()
  for i in range(int(first_range[0]), int(first_range[1]) + 1):
    first_set.add(i)
  for i in range(int(second_range[0]), int(second_range[1]) + 1):
    second_set.add(i)

  first_in_second = True
  second_in_first = True
  for i in first_set:
    if i not in second_set:
      first_in_second = False
      break
  if not first_in_second:
    for i in second_set:
      if i not in first_set:
        second_in_first = False
        break
    
  if first_in_second or second_in_first:
    count += 1
  
print(count)