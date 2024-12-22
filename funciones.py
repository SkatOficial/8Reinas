from os import system
from random import randint
from time import sleep

def Jugar_8():
    system("cls")
    tablero=[[None for columna in range(8)] for fila in range(8)]
    palabra=""
    while True:
        Ingresa_reina(tablero)
        comprueba=Verifica_juego(tablero)
        if(comprueba==False):
            Dibuja_matriz(tablero)
            palabra="[PERDISTE]"
            break
        elif(comprueba==True):
            Dibuja_matriz(tablero)
            palabra="[GANASTE]"
            break
    for letra in palabra:
        print(letra,end="")
        sleep(0.1)
    
def Dibuja_matriz(matriz,exculye=None):#Funcion que dibuja una matriz sin importar tamaño o tipo de dato   
    #-----------------|BUSCA EL ELEMENTO MAS GRANDE DE LA MATRIZ|-----------------
    larg_num=0
    fila_max=0

    for fila in matriz:
        fila_max+=1
        for columna in fila:
            if len(str(columna))>len(str(larg_num)):
                larg_num=columna
    larg_num=len(str(larg_num))

    #------|CREA ESPACIOS INICIALES|------
    sep=" +"
    linea_c="  "
    for n in range(len(str(fila_max))):
        sep=" "+sep
        linea_c+=" "

    #------|CREA SEPARADOR|------
    for n in range(len(matriz[0])):
        sep+="-"*(larg_num+1)+"+"

    #------|CREA LINEA DE NUMEROS DE LA COLUMNA|------
    for n in range(ord('A'),ord('A')+len(matriz[0])):
        linea_c+=str(chr(n)).center(larg_num+2)

    #------|DIBUJA SEPARADOR|-----
    print(linea_c)
    print(sep)
    indice_f=0
    for fila in matriz:
        
        indice_f+=1
        print(str(indice_f).center(len(str(fila_max))),end=" ")
        for columna in fila:
            sleep(0.02)
            if str(columna)== str(exculye):
                print("|"+"".center(larg_num+1) , end="")
            else:
                print("|"+str(columna).center(larg_num+1) , end="")
        print("|",)
        print(sep)
def Ingresa_reina(matriz):

    letras=['A','B','C','D','E','F','G','H']
    numeros=['1','2','3','4','5','6','7','8']
   
    #Variables que serviran para guardar las caracteristicas de la posicion
    contiene_letra = False;
    contiene_num = False;
    son_tipos_iguales = False;

    #-----------------|Ingresa Opcion|-----------------
    while True:
        Dibuja_matriz(matriz)
        print("+======================================+")
        posicion=input("|Ingrese una posicion: ").upper()
        
        #Comprueba las caracteristicas de la posicion (si contiene los numeros validos, las letras validas o si son igual tipo)
        if(len(posicion)==2 and posicion[0].isalnum() and posicion[1].isalnum()):
            contiene_letra=any(posicion[0]==letra or posicion[1]==letra for letra in letras)
            contiene_num=any(posicion[0]==numero or posicion[1]==numero for numero in numeros)
            son_tipos_iguales=(posicion[0].isdigit() and posicion[1].isdigit()) or (posicion[0].isalpha() and posicion[1].isalpha())
        else:
            system("cls")
            print("|[ERROR][LO INGRESADO NO ES UNA POSICION]")
            continue

        #Valida las caracteristicas de la posicion
        if((contiene_letra==False and contiene_num==False) or son_tipos_iguales==True):
            system("cls")
            print("|[ERROR][LO INGRESADO NO ES UNA POSICION]")
            continue
        else:
            fila=0
            columna=0

            #Transforma la posicion ingresada a una posicion que pueda leer la matriz
            if posicion[0].isdigit():
                fila=int(posicion[0])-1
                columna=ord(posicion[1])-ord('A')
            else:
                fila=int(posicion[1])-1
                columna=ord(posicion[0])-ord('A')
        
        if(matriz[fila][columna]!=None):
           system("cls")
           print("|[ERROR][POSICION YA OCUPADA]") 
           continue

        matriz[fila][columna]="♛"
        system("cls")
        print("|[REINA INGRESADA]") 
        break
def Verifica_juego(matriz):
    pos_reinas=[list([fila,columna]) for fila in range(8) for columna in range(8) if matriz[fila][columna]!=None]
    
    for pos in range(len(pos_reinas)-1):
        fila=pos_reinas[pos][0]
        columna=pos_reinas[pos][1]
 
        #print(f"posicion reina = {fila}|{columna}")
        
        for pos_sgnt in range(pos+1,len(pos_reinas)):
            fila_sgnt=pos_reinas[pos_sgnt][0]
            columna_sgnt=pos_reinas[pos_sgnt][1]
            diagonal_p=columna+(fila_sgnt-fila)
            diagonal_i=columna-(fila_sgnt-fila)
            if(fila_sgnt==fila or columna_sgnt==columna):# Verifica si las demas reinas estan en misma fila y columna
                return False
            elif(columna_sgnt==diagonal_p or columna_sgnt==diagonal_i):# lo mismo pero con la diagonales
                return False
        
    if len(pos_reinas)==8:
        return True    
    return None             