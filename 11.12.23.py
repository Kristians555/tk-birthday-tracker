# fails= "noteiktiEksistejosFails.txt"

# try:
#     with open(fails) as fails:
#         print("atveras")

# except FileNotFoundError as e:
#     print("fails:", fails, "netika atrasts")

# print("nakamais")

# def Dalisana(sk1, sk2):
#     dalijums=0
#     try:
#         dalijums= sk1/sk2
#     except ZeroDivisionError as e1:
#         print("nevar dalit ar 0")
#     except Exception as e2:
#         print("nav vienadas vertibas")
#     return dalijums

# print(Dalisana(3,3))
# print(Dalisana(3,"3"))
# print(Dalisana(3,0))

# print("nakamais")

# def Dalisana(sk3, sk4):
#     return sk3/sk4

# try:
#     print(Dalisana(3,3))
#     print(Dalisana(3,"banans"))

# except Exception as e3:
#     print("nevar jo nav vienadas vinibas")

# print("nakamais")

# import math

# class NeatbalstitiNegativiCipari(Exception):
#     pass

# def saskaitiKvadratsaknes(sk5, sk6):
#     if sk5<0 or sk6<0:
#         msg = "Vismaz 1 skaitlis ir negativs"
#         raise NeatbalstitiNegativiCipari(msg)
    
#     return math.sqrt(sk5)+math.sqrt(sk6)

# print(saskaitiKvadratsaknes(1, -1))

print("nakamais")

