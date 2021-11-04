
mihai_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

ml_asc = sorted(mihai_list)
mihai_list.sort()
print(ml_asc)
# am incercat prima data ml_asc=mihai_list.sort() iar rezultatul e None
# nu am inteles de ce nu pot asigna aceasta operatie unei variabile ca la metoda sorted

ml_desc = sorted(mihai_list, reverse = True)
mihai_list.sort(reverse = True)
print(ml_desc)

mihai_list_par = ml_asc[1::2]
print(mihai_list_par)

mihai_list_par_1 = ml_desc[8::-2]
print(mihai_list_par_1)

mihai_list_impar = ml_asc[::2]
print(mihai_list_impar)

mihai_list_impar_1 = ml_desc[1::2]
print(mihai_list_impar_1)

mihai_list_3 = ml_asc[2::3]
print(mihai_list_3)
