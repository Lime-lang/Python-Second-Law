class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_tipo(self):
        return self.tipo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_tipo(self, tipo):
        self.tipo = tipo

    def __eq__(self, other):
        return self.nombre == other.nombre and self.tipo == other.tipo

    def __str__(self):
        return f"{self.tipo} llamado {self.nombre}, {self.edad} años"

class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        if self.cabeza is None:
            self.cabeza = Nodo(animal)
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                if actual.animal == animal:
                    print("El animal ya está en la lista.")
                    return
                actual = actual.siguiente
            if actual.animal == animal:
                print("El animal ya está en la lista.")
                return
            actual.siguiente = Nodo(animal)

    def mostrar_animales_iterativo(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.animal)
            actual = actual.siguiente

    def mostrar_animales_recursivo(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo is not None:
            print(nodo.animal)
            self.mostrar_animales_recursivo(nodo.siguiente)

if __name__ == "__main__":
    zoologico = ListaEnlazada()

    animal1 = Animal("Águila", 5, "Ave")
    animal2 = Animal("Pantera", 3, "Felino")
    animal3 = Animal("Vaca", 2, "Mamífero")
    animal4 = Animal("Águila", 5, "Ave")  # Animal repetido

    zoologico.agregar_animal(animal1)
    zoologico.agregar_animal(animal2)
    zoologico.agregar_animal(animal3)
    zoologico.agregar_animal(animal4)  # No se debería agregar

    print("Animales en el zoológico (iterativo):")
    zoologico.mostrar_animales_iterativo()

    print("\nAnimales en el zoológico (recursivo):")
    zoologico.mostrar_animales_recursivo()