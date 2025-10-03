class Course:
    def __init__(self,nombre,creditos,nota):
        self.nombre=nombre
        self.creditos=creditos
        self.nota=nota

class Semester:
    def __init__(self):
        self.cursos=list()
        self.No_cursos=0
        self.suma_total=0
    def add(self,datos):
        nuevo_curso= Course(datos[0],int(datos[1]),float(datos[2]))
        for i in range(0,self.No_cursos,1):
            if(nuevo_curso.nombre.lower()==self.cursos[i].nombre.lower()):
                print("ERROR:DUP")
                return
        self.suma_total+=nuevo_curso.nota
        self.cursos.append(nuevo_curso)
        self.No_cursos+=1
        return
    def avg(self):
        promedio = self.suma_total/self.No_cursos
        promedio=round(promedio,2)
        return promedio
    def list(self):
        for i in range(0,self.No_cursos,1):
            print(f"Creditos: {self.cursos[i].creditos}, Nombre: {self.cursos[i].nombre}")
        return
    
def main():
    Semestre = Semester()
    datos=int(input("Ingresa el numero de operaciones a realizar: "))
    cuenta=0
    while (cuenta<datos):
        entrada=input()
        entrada=entrada.split()
        datos_a_utilizar= entrada[1:]
        if(entrada[0]=="ADD"):
            Semestre.add(datos_a_utilizar)
        elif(entrada[0]=="AVG"):
            print(f"Prom={Semestre.avg()}")
        elif(entrada[0]=="LIST"):
            Semestre.list()
        cuenta+=1
main()

"""
    TESTCASES

    TESTCASE#1
    Entradas:
    4
    ADD Probabilidad 4 5
    ADD Estructuras_de_datos 3 4.7
    AVG
    LIST

    Salidas:

    prom=4.85
    Creditos: 4, Nombre: Probabilidad
    Creditos: 3, Nombre: Estructuras_de_datos

    TESTCASE#2
    Entradas:
    5
    ADD Calculo_Vectorial 4 4.2
    ADD Calculo_Integral 4 3.2
    ADD Algebra_Matricial 3 2.8
    LIST 
    AVG

    Salidas:
    Creditos: 4, Nombre: Calculo_Vectorial
    Creditos: 4, Nombre: Calculo_Integral
    Creditos: 3, Nombre: Algebra_Matricial
    Prom=3.37

    TESTCASE#3
    Entradas:
    10
    ADD Probabilidad 4 5
    ADD Estructuras_de_datos 3 4.7
    ADD Probabilidad 4 5
    ADD Estructuras_de_datos 3 4.7
    ADD Calculo_Vectorial 4 4.2
    AVG
    ADD Calculo_Integral 4 3.2
    ADD Algebra_Matricial 3 2.8
    LIST
    AVG

    Salidas:
    ERROR:DUP
    ERROR:DUP

    Prom=4.63

    Creditos: 4, Nombre: Probabilidad
    Creditos: 3, Nombre: Estructuras_de_datos
    Creditos: 4, Nombre: Calculo_Vectorial
    Creditos: 4, Nombre: Calculo_Integral
    Creditos: 3, Nombre: Algebra_Matricial

    Prom=3.98


"""
    