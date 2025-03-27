class Vector:
    # Lo primero que debemos definir es el constructor, o inicializador en python
    def __init__(self, iterable):
        self._vector = [item for item in iterable]
        return None
    
    def __repr__(self):
        return f"Vector({self._vector})"
    
    def __str__(self):
        cadena = "[" 
        for item in self._vector:
            cadena += f" {item}"
        cadena += f" ]"
        return cadena
    
    def __getitem__(self, index):
        return self._vector[index]
    
    def __setitem__(self, index, valor):
        self._vector[index] = valor
    
    def __len__(self):
        return len(self._vector)
    
    def __add__(self, other):
        if isinstance(other, (int, float, complex)):
            return Vector([item + other for item in self._vector])
        else:
            return Vector([num1 + num2 for num1, num2 in zip(self, other) ])
        
    __radd__ = __add__