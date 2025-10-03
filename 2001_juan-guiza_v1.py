class Contact:
    def __init__(self,nombre,apellido,email,telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.telefono=telefono


class ContactBook:
    def __init__(self):
        self.contactos=list()
        self.numero_de_contactos=0
    def add(self,datos):
        nuevo_contacto= Contact(datos[0],datos[1],datos[2],datos[3])
        posicion=0
        for i in range(0,self.numero_de_contactos,1):
            if(self.contactos[i].apellido<nuevo_contacto.apellido):
                posicion+=1
            if(nuevo_contacto.email.lower()==self.contactos[i].email.lower()):
                print("ERROR:DUP")
                return
        self.contactos.insert(posicion,nuevo_contacto)
        self.numero_de_contactos+=1
        return
    def delete(self,dato):
        dato_encontrado=self.find(dato)
        if(dato_encontrado==-1):
            print("Usuario no encontrado; no puede ser eliminado")
        else:
            self.contactos.pop(dato_encontrado)
            print("Usuario eliminado con exito")
            self.numero_de_contactos-=1
        return
    def find(self,dato):
        dato=dato[0].lower()
        for i in range(0,self.numero_de_contactos,1):
            if((dato==self.contactos[i].email.lower())or((dato==self.contactos[i].nombre.lower()))):
                return i
        return -1
    def list(self):
        for i in range(0,self.numero_de_contactos,1):
            print(f"{self.contactos[i].apellido},{self.contactos[i].nombre} <{self.contactos[i].email}> {self.contactos[i].telefono}")
        return
    

def main():
    Directorio = ContactBook()
    datos=int(input("Ingresa el numero de operaciones a realizar: "))
    cuenta=0
    while (cuenta<datos):
        entrada=input()
        entrada=entrada.split()
        datos_a_utilizar= entrada[1:]
        if(entrada[0]=="ADD"):
            Directorio.add(datos_a_utilizar)
        elif(entrada[0]=="DEL"):
            Directorio.delete(datos_a_utilizar)
        elif(entrada[0]=="FIND"):
            busqueda=Directorio.find(datos_a_utilizar)
            if(busqueda==-1):
                print(f"El usuario identificado por {datos_a_utilizar[0]} NO se encuentra en el contact_book")
            else:
                print(f"El usuario identificado por {datos_a_utilizar[0]} se encuentra en el contact_book")
        elif(entrada[0]=="LIST"):
            Directorio.list()
        cuenta+=1


main()
"""
    TESTCASE #1:
    Entradas:

    6
    ADD Juan Florez aaa@gmail.com 328732
    ADD Juan Florez aaa@gmail.com 328732
    ADD Jhon Sanchez bbb@gmail.com 237423
    LIST
    DEL aaa@gmail.com
    LIST

    Salidas:
    ERROR:DUP

    Florez,Juan <aaa@gmail.com> 328732
    Sanchez,Jhon <bbb@gmail.com> 237423 

    Usuario eliminado con exito

    Sanchez,Jhon <bbb@gmail.com> 237423

    TESTCASE#2

    Entradas:

    6
    ADD Juan Florez aaa@gmail.com 328732
    ADD Valentina Giraldo hshs@gmail.com 739823
    LIST
    ADD Andres Fernandez jdhsu@gmail.com 32424
    LIST
    FIND Andres

    Salidas:
    Florez,Juan <aaa@gmail.com> 328732
    Giraldo,Valentina <hshs@gmail.com> 739823

    Fernandez,Andres <jdhsu@gmail.com> 32424
    Florez,Juan <aaa@gmail.com> 328732
    Giraldo,Valentina <hshs@gmail.com> 739823   

    El usuario identificado por Andres se encuentra en el contact_book

    TESTCASE#3:

    Entradas:
    7
    ADD Juan Florez aaa@gmail.com 328732
    ADD Valentina Giraldo hshs@gmail.com 739823
    ADD Andres Fernandez jdhsu@gmail.com 32424
    FIND jdhsu@gmail.com
    FIND Horacio
    DEL hshs@gmail.com
    LIST

    Salidas:

    El usuario identificado por jdhsu@gmail.com se encuentra en el contact_book

    El usuario identificado por Horacio NO se encuentra en el contact_book

    Usuario eliminado con Exito

    Fernandez,Andres <jdhsu@gmail.com> 32424
    Florez,Juan <aaa@gmail.com> 328732

"""