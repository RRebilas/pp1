universities = []
with open('universities.txt', 'r+') as file:
    universities = [line.strip() for line in file]
universities.sort()
print(universities)
with open('universities.txt', 'w') as file:
    for line in universities:
        file.write(f"{line}\n")
