class BiDictionary:
    def __init__(self):
        self.es_to_en = {}
        self.en_to_es = {}

    def ADD(self, es: str, en: str):
        es = es.casefold()
        en = en.casefold()
        if es in self.es_to_en or en in self.en_to_es:
            print("ERROR:DUP")
            return
        self.es_to_en[es] = en
        self.en_to_es[en] = es

    def FIND(self, word: str):
        word = word.casefold()
        if word in self.es_to_en:
            print(f"es={word}, en={self.es_to_en[word]}")
        elif word in self.en_to_es:
            print(f"en={word}, es={self.en_to_es[word]}")
        else:
            print("NOTFOUND")

    def LIST(self):
        for es in sorted(self.es_to_en.keys()):
            print(f"{es} -> {self.es_to_en[es]}")

    def BULKADD(self, pairs):
        # Validar primero
        for es, en in pairs:
            es, en = es.casefold(), en.casefold()
            if es in self.es_to_en or en in self.en_to_es:
                print("ERROR:BULK")
                return
        # Si no hubo conflicto, agregar todos
        for es, en in pairs:
            es, en = es.casefold(), en.casefold()
            self.es_to_en[es] = en
            self.en_to_es[en] = es

    def EXPORT(self, filename="diccionario.txt"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for es in sorted(self.es_to_en.keys()):
                    f.write(f"{es} -> {self.es_to_en[es]}\n")
            print(f"Diccionario exportado a {filename}")
        except Exception as e:
            print("ERROR:EXPORT", e)


# ---- Casos de prueba ----
bd = BiDictionary()

bd.ADD("Casa", "House")
bd.ADD("Perro", "Dog")
bd.ADD("Gato", "Cat")

print("\nLIST:")
bd.LIST()

print("\nFIND:")
bd.FIND("casa")
bd.FIND("house")
bd.FIND("bird")

print("\nBULKADD:")
bd.BULKADD([("Sol", "Sun"), ("Luna", "Moon")])
bd.BULKADD([("Agua", "Water"), ("Perro", "Doggy")])  # ERROR:BULK

print("\nLIST después de BULKADD:")
bd.LIST()

print("\nEXPORT:")
bd.EXPORT("mi_diccionario.txt")
