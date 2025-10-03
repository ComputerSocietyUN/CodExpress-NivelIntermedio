class Contact():
    def __init__(self, name: str, phone: int, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}"


class ContactBook():
    def __init__(self):
        self.contacts = []

    def ADD(self, contact):
        # No permitir emails duplicados
        for c in self.contacts:
            if c.email.lower() == contact.email.lower():
                return "ERROR:DUP"
        self.contacts.append(contact)
        return f"Contacto {contact.name} agregado."

    def DEL(self, name: str):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                return f"Contacto {name} eliminado."
        return "Contact not found"

    def FIND(self, text: str):
        results = []
        for contact in self.contacts:
            if text.lower() in contact.name.lower() or text.lower() in contact.email.lower():
                results.append(str(contact))
        if results:
            return "\n".join(results)
        return "Contact not found"

    def LIST(self):
        sorted_contacts = sorted(self.contacts, key=lambda c: c.name)
        if not sorted_contacts:
            return "No hay contactos."
        return "\n".join(map(str, sorted_contacts))


# ---- Casos de prueba ----
Juan = Contact("Juan", 1151232528, "juan@gmail.com")
Ana = Contact("Ana", 1065498378, "ana@gmail.com")
Carlos = Contact("Carlos", 1156781234, "carlos@gmail.com")

book = ContactBook()
print(book.ADD(Juan))
print(book.ADD(Ana))
print(book.ADD(Carlos))
print(book.ADD(Contact("Pedro", 111222333, "juan@gmail.com")))  # Email duplicado

print("\n--- LISTA INICIAL ---")
print(book.LIST())

print("\n--- ELIMINANDO ---")
print(book.DEL("Ana"))
print(book.DEL("Maria"))

print("\n--- LISTA DESPUÉS ---")
print(book.LIST())

print("\n--- BUSQUEDA ---")
print(book.FIND("Carlos"))
print(book.FIND("gmail"))
print(book.FIND("Andrés"))
