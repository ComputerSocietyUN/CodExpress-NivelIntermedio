class Node():
    def __init__(self,valor):
        self.valor=valor
        self.siguiente=None

class Stack():
    def __init__(self):
        self.top= None
        self.tamano=0
    def push(self,nodo):
        if(self.tamano==0):
            self.top=nodo
            self.tamano+=1
        else:
            nodo.siguiente=self.top
            self.top= nodo
            self.tamano+=1
        return
    def pop(self):
        if(self.tamano==0):
            print("ERROR:EMPTY")
        else:
            print(f"El valor {self.top.valor}  fue eliminado")
            self.top=self.top.siguiente
            self.tamano-=1
            
        return
    def peek(self):
        if(self.tamano==0):
            print("ERROR:EMPTY")
            return 
        else:
            print(self.top.valor)
            return 
    def size(self):
        print(self.tamano)
    

def main():
    Pila=Stack()
    datos=int(input("Ingresa el numero de operaciones a realizar: "))
    cuenta=0
    while (cuenta<datos):
        entrada=input()
        entrada=entrada.split()
        if(entrada[0]=="PUSH"):
            datos_a_utilizar= entrada[1]
            nuevo_nodo = Node(datos_a_utilizar)
            Pila.push(nuevo_nodo)
        elif(entrada[0]=="POP"):
            Pila.pop()
        elif(entrada[0]=="PEEK"):
           Pila.peek()
        elif(entrada[0]=="SIZE"):
            Pila.size()
        cuenta+=1
main()

"""TESTCASES

    TESTCASE#1
    Entradas:
    7
    PUSH Pera
    PUSH 45
    PUSH 377.34
    POP
    POP
    PEEK
    SIZE

    Salidas:
    El valor 377.34  fue eliminado
    El valor 45  fue eliminado
    Pera
    1

    TESTCASE#2
    Entradas:
    7
    POP
    PEEK
    PUSH Banano
    SIZE
    PUSH Rabano
    PUSH 7
    PEEK

    Salidas:
    ERROR:EMPTY
    ERROR:EMPTY
    1
    7

    TESTCASE#3
    Entradas:
    4
    PUSH 63673.3
    PUSH 323
    POP
    PEEK

    Salidas:
    El valor 323  fue eliminado
    63673.3

    Analisis de Complejidad:
    Todas las operaciones son O(1) ya que ninguna depende de la cantidad de datos entrantes, todas las operaciones se hacen en tiempo constante
"""


