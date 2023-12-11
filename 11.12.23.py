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

# print("nakamais")


# try:
#     sk7 = int(input("ievadi simbolu rindu: "))
#     print("skaitlis ir:", sk7)
# except Exception as e5:
#     print("nav ievadits vesels skaitlis")

# print("nakamais")

# skaitli = [1, 2, 3, 4, 5]

# try:
#     print(skaitli[5])
# except IndexError as e6:
#     print(e6)
# finally:
#     print("sis joprojam notiek")

# print("nakamais")

# x= int(input("ievadi pozitivu skaitli: "))

# try:
#     x= x-10
#     assert x>=0, "atlauti tikai pozitivi skaitli"
# except AssertionError as e7:
#     print("notikusi kluda:", str(e7))

# print("notiek")

print("nakamais")

def Dalisana(sk8, sk9):
    try:
        rezultats= sk8/sk9
    except ZeroDivisionError as e8:
        print(e8)
    else:
        return rezultats
    
print(Dalisana(1,1))
