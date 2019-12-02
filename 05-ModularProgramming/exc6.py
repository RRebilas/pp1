import csv
import statistics
lp = 1
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    # print(f.readline())
    print("====================================================")
    age_sum = []
    for row in reader:
        print(f"{lp} {row[1]} {row[0]} {row[2]} {row[3]}")
        lp += 1
        age_sum.append(int(row[2]))
    print(f"Srednia arytmetyczna wieku pracowników: {statistics.mean(age_sum)}")