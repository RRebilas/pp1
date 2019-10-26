tab = [15, 8, 31, 47, 2, 19]
arr_standard = ""
arr_reversed = ""
for i in tab:
    arr_standard += str(i) + " "
for j in reversed(tab):
    arr_reversed += str(j) + " "
print("tab: " + arr_standard)
print("tab in reverse: " + arr_reversed)