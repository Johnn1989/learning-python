'''
Scrip description:
Calculadora que reciba 2 numeros y
realice la operacion aritmetica que el usuario desee.
Puede escoger entre sumar, restar, multiplicar o dividir
'''
import os

os.system("clear")

def calculator(x,y,z):
    if z == '1' :
        return x + y
    elif z == '2' :
        return x - y
    elif z == '3' :
        return x * y
    elif z == '4' 
    if y == 0

        return x / y
    else :
        print("::: Faild, invalid option:::") 
        return 0
n1 = float(Input("Ingrese el primer valor: "))
n2 = float(Input("Ingrese el segundo valor: "))

input(":::MENU CALCULADORA:::")
input("[1]. Sumar")
input("[2]. Restar")
input("[3]. Multiplicar")
input("[4]. Dividir")
opc = input("Digite una opcion del menu: ")
#Formato de salid 1:
if opc >= 1 and opc <= 4:
    ans = calculator (n1, n2, opc)
    print("Suma:", ans[0])
    print("Resta:", ans[0])
    print("Multiplicación:", ans[0])
    print("División:", ans[0])
ans = calculator(n1, n2, opc)
print("resultado: ", ans)

#Formato de salida 2:
#print("Resultado")


