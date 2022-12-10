def check_tail(head, tail):
  if head[0] > tail[0] + 1:
    tail[0] = head[0] - 1
    tail[1] = head[1]
  if head[0] < tail[0] - 1:
    tail[0] = head[0] + 1
    tail[1] = head[1]
  if head[1] > tail[1] + 1:
    tail[0] = head[0]
    tail[1] = head[1] - 1
  if head[1] < tail[1] - 1:
    tail[0] = head[0]
    tail[1] = head[1] + 1

input_file = open("input.txt", "r")
input = input_file.readlines()
visited = set()
head_pos = [0, 0]
tail_pos = [0, 0]

for line in input:
  direction, length = line.strip().split(' ')
  for i in range(int(length)):
    match direction:
      case "L":
        head_pos = [head_pos[0] - 1, head_pos[1]]
      case "R":
        head_pos = [head_pos[0] + 1, head_pos[1]]
      case "D":
        head_pos = [head_pos[0], head_pos[1] - 1]
      case "U":
        head_pos = [head_pos[0], head_pos[1] + 1]
    check_tail(head_pos, tail_pos)
    visited.add(tuple(tail_pos))
print(len(visited))