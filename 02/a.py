input_file = open("input.txt", "r")
input = input_file.readlines()
score = 0
for line in input:
  choices = line.split()
  if choices[0] == 'A': # Rock
    if choices[1] == 'X':
      score += 4  # Rock + Draw
    if choices[1] == 'Y':
      score += 8  # Paper + Win
    if choices[1] == 'Z':
      score += 3  # Scissors + Loss
  if choices[0] == 'B': # Paper
    if choices[1] == 'X':
      score += 1  # Rock + Loss
    if choices[1] == 'Y':
      score += 5  # Paper + Draw
    if choices[1] == 'Z':
      score += 9  # Scissors + Win
  if choices[0] == 'C': # Scissors
    if choices[1] == 'X':
      score += 7  # Rock + Win
    if choices[1] == 'Y':
      score += 2  # Paper + Loss
    if choices[1] == 'Z':
      score += 6  # Scissors + Draw
print(score)