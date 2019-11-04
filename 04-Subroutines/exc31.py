def reverse(tab):
    reversed_tab = []
    for i in range(len(tab)-1, -1, -1):
        reversed_tab.append(tab[i])
    return reversed_tab

print(reverse([2, 5, 4, 1, 8, 7, 4, 0, 9]))
