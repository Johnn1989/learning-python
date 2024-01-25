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
    elif z == '4' :
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

ans = calculator(n1, n2, opc)
print("resultado: ", ans)


