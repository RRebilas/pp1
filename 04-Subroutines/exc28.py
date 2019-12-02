def graph(jezyki, wartosci):
    for jezyk in jezyki:
        print('{:>10}'.format(jezyk), end=': ')
        for i in range(wartosci[jezyki.index(jezyk)]):
            print("#", end="")
        print()


jezyki = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
wartosci = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]
graph(jezyki, wartosci)
