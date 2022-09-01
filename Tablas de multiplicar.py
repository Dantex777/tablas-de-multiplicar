#contador = 1
#print(contador)
#while contador <1000:
#    contador += 1
#    print(contador)


#for contador in range(999, 1001):
#    print(contador)

#for i in range(10):
#    result= 11*i
#    print("11 por " + str(i) + " es igual a= " + str(result))

#TAREA: Hacer un programa que te devuelva las tablas que el USER Quiera:

def run():
                     
    for contador in range(11):
        resultado = int(tabla) * int(contador)
        print(str(tabla) + " multiplicado por " + str(contador) + " = " + str(resultado))
        


if __name__ == '__main__':
    tabla = input(
        """***********************************
Bienvenid@ al programa de Tablas!!!
Cual tabla quieres saber?
***********************************
Tu respuesta= """)
    run()
