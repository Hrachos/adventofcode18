def found(res, curr):
    if curr in res:
        print("FOUND!")
        print(curr)
        return True
    return False


filename = "input.txt"
file = open(filename, "r")
results = {}
current = 0

while True:
    for line in file:
        current += int(line)
        if found(results, current):
            exit(0)
        results[current] = True
        # print(results)
    file.seek(0)
