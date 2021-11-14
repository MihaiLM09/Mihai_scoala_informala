
# ### Suma total ###
# n = None
# while n == None or type(n) is not int:
#     n = input('Alege un numar: \n')
#     try:
#         n = int(n)
#     except ValueError as x:
#         print('Am spus sa alegi un numar! Hai sa incercam iar ...')
#
# def suma(n):
#     if n == 0:
#         return 0
#     return n + suma(n - 1)
# print(suma(n))



# ### Suma impar ###
# n = None
# while n == None or type(n) is not int:
#     n = input('Alege un numar: \n')
#     try:
#         n = int(n)
#     except ValueError as x:
#         print('Am spus sa alegi un numar! Hai sa incercam iar ...')
# def suma_impar(n):
#     if n == 0:
#          return 0
#     return ((n+1)//2)**2
# print(suma_impar(n))



# ### Suma impar_2 ###
# n = int(input('Alege un numar: \n'))
# def suma_impar_2(n):
#     if n == 0:
#         return 0
#     return sum(range(1,n+1,2))
# print(suma_impar_2(n))


# ### Suma par ###
# n = int(input('Alege un numar: \n'))
# def suma_par(n):
#     if n == 0:
#         return 0
#     return sum(range(0,n+1,2))
# print(suma_par(n))

# ### Calculator complet ###
# def calculator():
#
#     continuare = True
#     n = int(input('Alege un numar: \n'))
#     x = input('Alege T: total, P: par sau I: impar pentru tipul de suma dorita: \n').lower()
#
#     while continuare:
#
#         def suma_impar(n):
#             if n == 0:
#                 return 0
#             return sum(range(1, n + 1, 2))
#
#
#         def suma_par(n):
#             if n == 0:
#                 return 0
#             return sum(range(0, n + 1, 2))
#
#
#         def suma(n):
#             if n == 0:
#                 return 0
#             return n + suma(n - 1)
#
#
#         if x == 'p':
#             print(suma_par(n))
#         elif x == 'i':
#             print(suma_impar(n))
#         elif x == 't':
#             print(suma(n))
#         else:
#             print('Nu ai respectat regulile jocului.')
#
#         restart = input('Tasteaza Y daca continuam sau N daca incheiem. \n').lower()
#         if restart == "n":
#             continuare = False
#             print('Ne mai vedem. Ciao !')
#         elif restart == "y":
#             continuare = True
#             calculator()
#         else:
#             print('Iar nu ai respectat regulile jocului :).')
#
#
# calculator()

# ### Returnare valoarea 0 ###
# def valoarea_0():
#
#     n = None
#     while n == None:
#         n = input('Alege un numar: \n')
#         try:
#             n = int(n)
#             print(n)
#         except ValueError as x:
#             print(0)
#
# valoarea_0()

# ### Calculator real ###
# def nedefinit():
#
#     nedefinit = input('Scrie valori necunoscute, de orice tip, despartite doar de spatiu: \n').split()
#     my_list = []
#     for n in nedefinit:
#         try:
#             my_list.append(int(n))
#         except ValueError:
#             continue
#     print(sum(my_list))
#
# nedefinit()




