filename = "input.txt"
file = open(filename, "r")
res = 0
for line in file:
    res += int(line)
print(res)
