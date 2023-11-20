#Funcion "pedir_letra"
def pedir_letra(letras_usadas):
    while True:
    
        letra_nueva = input('Ingrese una letra no repetida: ')
        letra_nueva = letra_nueva.lower()
        letra = None
        if letra_nueva  in letras_usadas:
            letra_nueva = input('Ingrese una letra no repetida: ')
        else:
             letra = letra_nueva
        
        return letra
     


       # elif letra_ingresada in letra:
           # letra_ingresada = input('Ingrese una letra no repetida: ')
        #elif len(letra_ingresada)  > 1 :
            #letra_ingresada = input('Ingresa una letra no  repetida: ')
        
            #letra.append(letra_ingresada)
            #return letra_usada

if __name__ == "__main__":
    letra_usada = ['a', 'b','c']
    pedir_letra(letra_usada)