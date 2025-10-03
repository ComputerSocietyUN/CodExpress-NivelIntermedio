class StackEmptyError(Exception):
    pass


class MinStack:
    """
    Implementación de una pila con:
    - push(x): O(1)
    - pop(): O(1)
    - peek(): O(1)
    - size(): O(1)
    - min(): O(1) → devuelve el mínimo actual de la pila
    """
    def __init__(self):
        self.stack = []       # pila normal
        self.min_stack = []   # pila auxiliar para mínimos

    def push(self, x):
        self.stack.append(x)
        # Si min_stack está vacío o x es menor/igual al actual mínimo
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            raise StackEmptyError("ERROR:EMPTY")
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def peek(self):
        if not self.stack:
            raise StackEmptyError("ERROR:EMPTY")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def get_min(self):
        if not self.min_stack:
            raise StackEmptyError("ERROR:EMPTY")
        return self.min_stack[-1]


# ---- Casos de prueba ----
s = MinStack()

# PUSH
s.push(5)
s.push(3)
s.push(7)
s.push(2)

print("SIZE:", s.size())      # 4
print("PEEK:", s.peek())      # 2
print("MIN:", s.get_min())    # 2

# POP
print("POP:", s.pop())        # 2
print("MIN después de pop:", s.get_min())  # 3

print("POP:", s.pop())        # 7
print("MIN:", s.get_min())    # 3

print("POP:", s.pop())        # 3
print("MIN:", s.get_min())    # 5

print("POP:", s.pop())        # 5
# Intentar MIN o POP aquí lanzaría ERROR:EMPTY
