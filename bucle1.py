'''
Bucle: Ciclo, Loop, repetir una acción N veces, iteraciones (cantidad de ejecuciones).
Contadores (Cuenta o incrementa)
Acumuladores (Acomulación de valores. Peje. Sumar valores)
Contar valores es diferente de sumar valores

num
1
2
3

Contador => c = c + K => K es una constante
Incremento consecutivo y variable
Cuantos datos hay? cont = cont + 1 // cont+= 1

Acumulador => a = a + V => V es una variable (num, salario, edad, temperaturas, etc.)
Incremento aleatorio y variable.
Acumular valores? acum = acum + num //acum+=num
'''

#Funciön Bucle para imprimir los nümeros del 1 al 10 en pantalla 
def list_numbers1():
    #Bucle que imprime lista de números por pantalla
    i = 1
    while i <= 101:
        print(i)
        i+=1 #i = i + 1

    print("i: ", i) #101

def list_numbers2():
    #Bucle que imprime lista de números por pantalla
    i = 1
    status = True
    while status: #While status == True
        if i == 11:
            break #El break rompe el bucle
        print(i)
        i+=1 #i = i + 1
        if i > 10: #i == 11 

    print("i: ", i) #11

def list_numbers3():
    #Bucle que imprime lista de números por pantalla
    i = 1
    status = True
    while status: #While status == True
        if i == 11:
            break #El break rompe el bucle
        print(i)
        i+=1 #i = i + 1
        if i > 10: #i == 11
            status False 

    print("i: ", i) #101

def list_numbers4():
    #Bucle que imprime lista de números por pantalla
    i = 1
    status = True
    while not status: #While status != False
        print(i)
        i+=1 #i = i + 1
        if i > 10: #i == 11
            status True 

    print("i: ", i) #101
    
#list_numbers1() 
#list_numbers2() 
#list_numbers3()   
list_numbers4()    
