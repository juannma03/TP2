def eliminar(lista):
    for i in lista:
        print(i)
File=open("CASA.txt","w")
File.write("Hola clase")
File.close()
File=open("CASA.txt","a")
File.write("\nsabores")
File.close()
File=open("CASA.txt","r")
lista=((File.readlines()))
print(lista)
eliminar(lista)

