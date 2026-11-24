
file = open("input.txt", "r")

lines = file.readlines()

count = len(lines)
print("Total number of lines:", count)

first_two_lines = lines[:2]

print("\nFirst two lines:")
for line in first_two_lines:
    print(line, end="")

file.close()

output = open("output.txt", "w")

output.writelines(first_two_lines)

output.close()

print("\n\nData successfully written into output.txt")
