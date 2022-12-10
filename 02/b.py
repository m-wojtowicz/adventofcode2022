input_file = open("input.txt", "r")
input = input_file.readlines()
r = 1
p = 2
s = 3
d = 3
w = 6
score = 0
for line in input:
  choices = line.split()
  if choices[0] == 'A': # Rock
    if choices[1] == 'X':
      score += s  # Lose + Scissors
    if choices[1] == 'Y':
      score += d + r  # Draw + Rock
    if choices[1] == 'Z':
      score += w + p  # Win + Paper
  if choices[0] == 'B': # Paper
    if choices[1] == 'X':
      score += r  # Lose + Rock
    if choices[1] == 'Y':
      score += d + p  # Draw + Paper
    if choices[1] == 'Z':
      score += w + s  # Win + Scissors
  if choices[0] == 'C': # Scissors
    if choices[1] == 'X':
      score += p  # Lose + Paper
    if choices[1] == 'Y':
      score += d + s  # Draw + Scissors
    if choices[1] == 'Z':
      score += w + r  # Win + Rock
print(score)