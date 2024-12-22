#8 REINAS 
from funciones import *
system("cls")
while True:
    print("""
                        ♛
    +===============/8 REINAS\===============+
    |1.-JUGAR                                |
    |2.-SALIR                                |
    +========================================+
    """)
    opcion=input("|Eligue tu opcion :")
    system("cls")
    if(opcion=="1"):
        Jugar_8()
    elif(opcion=="2"):
        print("[SALIENDO...]")
        break
    else:
        print("[ERROR][OPCION INVALIDA]")
        

    
