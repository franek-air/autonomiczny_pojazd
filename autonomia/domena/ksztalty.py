"""Kształty szarych bloków w świecie robota."""
from autonomia.domena.bledy import BladScenariusza


class Prostokat:
    """Prostokątny blok o bokach równoległych do osi, np. regał lub ściana.
    Układ współrzędnych: (0, 0) to lewy górny róg świata, x rośnie w prawo,
    a y w dół. Wymiary podajemy w metrach. Punkt (x,y) to lewy górny róg
    prostokąta.
    
    Punkt leżący na krawędzi uznajemt za należący do prostokąta. Szerokość
    i wysokość muszą być dodatnie, inaczej konstruktor zgłasza
    BladScenariusza. Obiekt jest niezmienny."""

    def __init__(self, x, y, szerokosc, wysokosc):
        if not szerokosc > 0:
            raise BladScenariusza(f"szerokosc musi byc dodatnia: {szerokosc}")
        
        if not wysokosc > 0:
            raise BladScenariusza(f"wysokosc musi byc dodatnia: {wysokosc}")

        self._x = x
        self._y = y
        self._szerokosc = szerokosc
        self._wysokosc = wysokosc
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def szerokosc(self):
        return self._szerokosc

    @property
    def wysokosc(self):
        return self._wysokosc

    def zawiera_punkt(self, px, py):
        return self.x <= px <= self.x + self.szerokosc and self.y <= py <= self.y + self.wysokosc   