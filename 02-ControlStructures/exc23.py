mark = int(input("Podaj ocene: "))
marks_array = ['niedostateczny', 'mierny', 'dostateczny', 'dobry', 'bardzo dobry', 'celujacy']
if 1 <= mark <= 6:
    print(marks_array[mark - 1])
else:
    print("Enter proper mark")
