def calculateDirSize(tree, path):
  sum = 0
  for file in tree[path]["files"]:
    sum += int(file["size"])
  for dir in tree[path]["dirs"]:
    sum += calculateDirSize(tree, dir)

  return sum

input_file = open("input.txt", "r")
input = input_file.readlines()
tree = {}
path = ""
for i in range(len(input)):
  cmd = input[i].strip().split(' ')
  if cmd[1] == "cd":
    if cmd[2] == "..":
      path = path[:path.rfind('/', 0, path.rfind('/'))]
      path = path + "/"
    elif cmd[2] == "/":
      path = "/"
    else:
      path = path + cmd[2] + "/"
    i += 1
  if cmd[1] == "ls":
    tree[path] = { "files": [], "dirs": [] }
    sum = 0
    while True:
      if i < len(input) - 1:
        i += 1
      else:
        break
      entry = input[i].strip().split(' ')
      if entry[0] == "$":
        i -= 1
        break
      elif entry[0] == "dir":
        tree[path]["dirs"].append(path + entry[1] + "/")
      else:
        tree[path]["files"].append({ "name": entry[1], "size": entry[0] })

total = 0
for entry in tree:
  sum = calculateDirSize(tree, entry)
  if sum < 100000:
    total += sum
print(total)