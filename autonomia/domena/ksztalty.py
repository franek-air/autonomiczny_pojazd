"""Kształty szarych bloków w świecie robota."""
from autonomia.domena.bledy import BladScenariusza
from abc import ABC, abstractmethod


class Ksztalt(ABC):
    """Wspólny typ bazowy wszystkich kształtów szarych bloków w świecie.

    Klasa abstrakcyjna: nie tworzy się jej obiektów, tylko obiekty klas
    pochodnych (Prostokat, Okrag). Każdy kształt musi umieć odpowiedzieć,
    czy dany punkt w nim leży. Dzięki temu planista i siatka zajętości
    korzystają tylko z typu Ksztalt i nie muszą wiedzieć, z jakim konkretnie
    kształtem mają do czynienia.
    """

    @abstractmethod
    def zawiera_punkt(self, px, py):
        """Zwraca True, gdy punkt leży w kształcie (łącznie z brzegiem)."""

class Prostokat(Ksztalt):
    """Prostokątny blok o bokach równoległych do osi, np. regał lub ściana.
    Układ współrzędnych: (0, 0) to lewy górny róg świata, x rośnie w prawo,
    a y w dół. Wymiary podajemy w metrach. Punkt (x,y) to lewy górny róg
    prostokąta.
    
    Punkt leżący na krawędzi uznajemy za należący do prostokąta. Szerokość
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


class Okrag(Ksztalt):
    """Okrągły blok, np. słup w hali.

    Układ współrzędnych jest taki sam jak w Prostokat: (0, 0) to lewy górny
    róg świata, x rośnie w prawo, a y w dół. Wymiary podajemy w metrach.
    Punkt (x, y) to środek okręgu.

    Punkt leżący na brzegu uznajemy za należący do okręgu. Promień musi być
    dodatni, inaczej konstruktor zgłasza BladScenariusza. Obiekt jest
    niezmienny.
    """

    def __init__(self, x, y, promien):
        if not promien > 0:
            raise BladScenariusza(f"promien musi byc dodatni: {promien}")

        self._x = x
        self._y = y
        self._promien = promien


    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def promien(self):
        return self._promien


    def zawiera_punkt(self, px, py):
        dx = px - self.x
        dy = py - self.y

        return dx**2 + dy**2 <= self.promien**2