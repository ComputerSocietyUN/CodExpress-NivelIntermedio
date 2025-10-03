from collections import deque

class QueueEmptyError(Exception):
    pass


class Queue:
    def __init__(self):
        self.q = deque()              # cola principal
        self.total_wait = 0           # suma de tiempos de espera
        self.served = 0               # elementos atendidos
        self.K = None                 # límite de operaciones
        self.ops = deque()            # timestamps de operaciones (para control de rate limit)

    def setK(self, k):
        self.K = k

    def _check_limit(self, timestamp):
        if self.K is None:
            return
        # limpiar timestamps más viejos de 60s
        while self.ops and timestamp - self.ops[0] >= 60:
            self.ops.popleft()
        if len(self.ops) >= self.K:
            print("ERROR:RATE_LIMIT")
            return False
        self.ops.append(timestamp)
        return True

    def ENQUEUE(self, id, timestamp):
        if not self._check_limit(timestamp):
            return
        self.q.append((id, timestamp))

    def DEQUEUE(self, timestamp):
        if not self._check_limit(timestamp):
            return
        if not self.q:
            raise QueueEmptyError("ERROR:EMPTY")
        id, enq_time = self.q.popleft()
        wait = timestamp - enq_time
        self.total_wait += wait
        self.served += 1
        return id

    def STATS(self):
        L = len(self.q)
        avg = (self.total_wait // self.served) if self.served > 0 else 0
        print(f"len={L} wait_avg={avg}")


# ---- Casos de prueba ----
q = Queue()

# Encolamos
q.ENQUEUE("A", 0)
q.ENQUEUE("B", 10)
q.ENQUEUE("C", 15)

# Sacamos
print("DEQUEUE:", q.DEQUEUE(20))  # A, esperó 20s
print("DEQUEUE:", q.DEQUEUE(25))  # B, esperó 15s

# Stats
q.STATS()  # len=1, wait_avg=(20+15)/2 = 17

# Rate limit
q.setK(2)
q.ENQUEUE("D", 30)
q.ENQUEUE("E", 35)
q.ENQUEUE("F", 40)  # debería dar ERROR:RATE_LIMIT
