import math


class Ponto3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Ponto3({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, Vetor3):
            return Ponto3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Permitido somar apenas Ponto3 a Vetor3")

    def __sub__(self, other):
        if isinstance(other, Ponto3):
            return Vetor3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vetor3):
            return Ponto3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Permitido subtrair apenas Ponto3 de Ponto3 ou Vetor3 de Ponto3")

    def dist(self, other):
        if isinstance(other, Ponto3):
            dx = self.x - other.x
            dy = self.y - other.y
            dz = self.z - other.z
            return (dx**2 + dy**2 + dz**2)**(1/2)
        else:
            raise TypeError("Argumento deve ser outro ponto")

    def to(self, other):
        if isinstance(other, Point3):
            return Vector3(p.x - self.x, p.y - self.y, p.z - self.z)
        else:
            raise TypeError("Argumento deve ser outro ponto")


class Vetor3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vetor3):
            return Vetor3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Permitido somar apenas Vetor3 a Vetor3")

    def __sub__(self, other):
        if isinstance(other, Vetor3):
            return Vetor3(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Permitido subtrair apenas Vetor3 de Vetor3")

    def __mul__(self, escalar):
        if isinstance(escalar, (int, float)):
            return Vetor3(self.x * escalar, self.y * escalar, self.z * escalar)
        raise TypeError("Multiplicação apenas com um escalar")

    def __truediv__(self, escalar):
        if isinstance(escalar, (int, float)) and escalar != 0:
            return Vetor3(self.x / escalar, self.y / escalar, self.z / escalar)
        raise ValueError("Divisão apenas por um escalar não nulo")

    def dot(self, other):
        if isinstance(other, Vetor3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise TypeError("Produto escalar requer outro Vetor3")

    def cross(self, other):
        if isinstance(other, Vetor3):
            return Vetor3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        raise TypeError("Produto vetorial requer outro Vetor3")

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Não é possível normalizar um vetor nulo")
        return self / mag

    def __repr__(self):
        return f"Vetor3({self.x}, {self.y}, {self.z})"