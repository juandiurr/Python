

class Coordenates:
    def __init__(self):
        self.coordenadas = []  # almacena toda la lista
    def __len__(self):
        return len(self.coordenadas)
    def __str__(self):
        return f"{self.coordenadas}"
    def ret(self):
        return self.coordenadas
    def clear(self):
        self.coordenadas.clear()
    def append_cs(self,coords):
        if not isinstance(coords, list):
            raise ValueError("Se esperaba una lista de coordenadas")
        
        for coord in coords:
            if not isinstance(coord, list):
                raise ValueError(f"Cada coordenada debe ser una lista, se recibió: {type(coord).__name__}")
            if len(coord) != 2:
                
                raise ValueError(f"Cada coordenada debe tener exactamente 2 elementos: {len(coord)} elementos del tipo: {type(coord).__name__}")
            if not all(isinstance(x, int) for x in coord):
                raise ValueError(f"Cada valor de coordenada debe ser entero: {type(coord)}")
        if not isinstance(coords, list):
            raise ValueError(f"Error en el tipo de variable al usar append: {type(coord)}")
        
        for i in coords:
            self.coordenadas.append(i)
    def append_c(self,name):
        if not isinstance(name, list):
            raise ValueError(f"Error en el tipo de variable al usar append: {type(name)}")
        if len(name) != 2:
            raise ValueError("La lista al agregar debe de ser 2 elementos int")
        if not all(isinstance(x, int) for x in name):
                raise ValueError(f"Cada valor de coordenada debe ser entero: {name}")
        self.coordenadas.append(name)
    def vertical(self):
        from collections import defaultdict
        verticales = defaultdict(list)
        puntos_por_x = defaultdict(list)
        for x, y in self.coordenadas:
            puntos_por_x[x].append(y)
        for x in puntos_por_x:
            ys = sorted(puntos_por_x[x])
            for i in range(len(ys)-1):
                if ys[i] != ys[i+1]:
                    verticales[x].append([ys[i], ys[i+1]])
        return dict(verticales)
    def horizontal(self):
        from collections import defaultdict
        horizontales = defaultdict(list)
        puntos_por_y = defaultdict(list)
        for x, y in self.coordenadas:
            puntos_por_y[y].append(x)
        for y in puntos_por_y:
            xs = sorted(puntos_por_y[y])
            for i in range(len(xs)-1):
                if xs[i] != xs[i+1]:
                    horizontales[y].append([xs[i], xs[i+1]])

        return dict(horizontales)
    def keep_last(self):
        if len(self.coordenadas) > 2:
            self.coordenadas = self.coordenadas[-2:]

def hht(n):
    if n == 2:
        return 1
    else:
        return 0   
def colision(n1, n2, m):
    N1 = max(n1,n2)
    N2 = min(n1,n2)
    if m >= N2 and m <= N1:
        return True
    else:
        return False
    
def main():
    c1 = [
        [640, 20], [640, 29], [542, 20], [551, 29], [542, 73], [551, 82], [477, 73], [486, 82], [477, 138], [486, 147], [412, 138], [421, 147], [412, 209], [421, 218], [299, 209], [308, 218], [299, 406], [308, 415], [180, 415], [189, 406]
    ]
    
    c = Coordenates()
    c.append_cs(c1)
    print("Verticales: ")
    print(c.vertical())
    print(list(c.vertical().keys()))
    print(c.vertical()[640])
    print("Horizontales: ")
    print(c.horizontal())

    
if __name__ == "__main__":
    main()