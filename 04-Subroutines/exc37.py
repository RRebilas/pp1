def natural_numbers(array):
    non_repeatable = []
    array.sort()
    for i in range(len(array)):
        if i == len(array) - 1:
            if array[i] != array[i - 1]:
                non_repeatable.append(array[i])
        elif array[i] != array[i + 1] and array[i] != array[i - 1]:
            non_repeatable.append(array[i])
    return non_repeatable


print(f'Unikalne liczby w tablicy: {natural_numbers([0, 0, 1, 3, 6, 3, 5, 5, 7, 5, 4])}')
