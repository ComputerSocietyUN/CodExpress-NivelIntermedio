from decimal import Decimal, ROUND_HALF_UP

class Course():
    def __init__(self, name: str, credits: int, grade: Decimal):
        self.name = name
        self.credits = int(credits)
        self.grade = Decimal(str(grade))

    def __str__(self):
        return f"{self.name}, {self.credits}, {self.grade:.2f}"


class Semester():
    def __init__(self):
        self.courses = {}   # usamos diccionario para evitar duplicados
    
    def ADD(self, name: str, credits: int, grade: Decimal):
        if name in self.courses:
            print("ERROR:DUP")
        else:
            self.courses[name] = Course(name, credits, grade)
    
    def LIST(self):
        sorted_courses = sorted(self.courses.values(), key=lambda c: (-c.credits, c.name))
        for course in sorted_courses:
            print(course)
        
    def AVG(self):
        total_credits = sum(c.credits for c in self.courses.values())
        if total_credits == 0:
            avg = Decimal("0.00")
        else:
            total = sum(c.credits * c.grade for c in self.courses.values())
            avg = (total / total_credits).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
        print(f"prom={avg}")

    def IMPORT(self, lines):
        valid, invalid = 0, 0
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) != 3:
                invalid += 1
                continue
            name, credits, grade = parts
            try:
                credits = int(credits)
                grade = Decimal(grade)
            except:
                invalid += 1
                continue
            if name in self.courses:
                invalid += 1
            else:
                self.courses[name] = Course(name, credits, grade)
                valid += 1
        print(f"Import: {valid} valid, {invalid} invalid")


# ---- Casos de prueba sencillos ----
sem = Semester()

# 1. Agregar cursos
sem.ADD("Matematicas", 4, Decimal("4.5"))
sem.ADD("Ingles", 2, Decimal("3.7"))
sem.ADD("Matematicas", 3, Decimal("5.0"))  # duplicado → ERROR:DUP

# 2. Listar cursos
print("\nLIST:")
sem.LIST()

# 3. Promedio actual
print("\nAVG:")
sem.AVG()

# 4. Importar desde lista CSV
lines = [
    "Fisica,3,5.0",
    "Matematicas,2,4.0",  # duplicado
    "Quimica,4,4.2",
    "Errorcito,xx,3.5"    # inválido
]
sem.IMPORT(lines)

# 5. Listar después de importar
print("\nLIST después de import:")
sem.LIST()

# 6. Nuevo promedio
print("\nAVG nuevo:")
sem.AVG()

