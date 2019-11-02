import re

with open("students.txt") as file:
    for line in file:
        age = re.findall(r'\d{2}', line)
        for i in age:
            if int(i) < 30:
                z = line.split(',')
                print(z[0], z[1], z[4], end="")
