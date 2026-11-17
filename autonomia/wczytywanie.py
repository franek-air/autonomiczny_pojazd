"""Wczytywanie scenariusza z pliku YAML."""
import yaml

from autonomia.domena.bledy import BladScenariusza
from autonomia.domena.ksztalty import Okrag, Prostokat
from autonomia.domena.scenariusz import Scenariusz
from autonomia.domena.swiat import Swiat

# Typ bloku z pliku -> funkcja, która buduje odpowiedni kształt.
_FABRYKI_KSZTALTOW = {
    "prostokat": lambda o: Prostokat(o["x"], o["y"], o["szerokosc"], o["wysokosc"]),
    "okrag": lambda o: Okrag(o["x"], o["y"], o["promien"]),
}


def _wczytaj_yaml(sciezka):
    try:
        with open(sciezka, encoding="utf-8") as plik:
            dane = yaml.safe_load(plik)
    except FileNotFoundError:
        raise BladScenariusza(f"nie znaleziono pliku: {sciezka}") from None
    except yaml.YAMLError as blad:
        raise BladScenariusza(f"niepoprawny YAML w {sciezka}: {blad}") from None
    if not isinstance(dane, dict):
        raise BladScenariusza(f"plik {sciezka} nie opisuje scenariusza")
    return dane


def _zbuduj_ksztalt(opis):
    if not isinstance(opis, dict) or opis.get("typ") not in _FABRYKI_KSZTALTOW:
        raise BladScenariusza(f"nieznany lub brakujacy typ bloku: {opis}")
    try:
        return _FABRYKI_KSZTALTOW[opis["typ"]](opis)
    except KeyError as blad:
        raise BladScenariusza(
            f"w bloku '{opis['typ']}' brakuje pola {blad}"
        ) from None


def wczytaj_scenariusz(sciezka):
    """Wczytuje scenariusz z pliku YAML. Błędy zgłasza jako BladScenariusza."""
    dane = _wczytaj_yaml(sciezka)
    try:
        opis_swiata = dane["swiat"]
        swiat = Swiat(opis_swiata["szerokosc"], opis_swiata["wysokosc"])
        for opis in dane.get("szare_bloki") or []:
            swiat.dodaj_blok(_zbuduj_ksztalt(opis))
        robot = dane["robot"]
        start = (robot["start"]["x"], robot["start"]["y"])
        cel = (robot["cel"]["x"], robot["cel"]["y"])
    except KeyError as blad:
        raise BladScenariusza(f"w scenariuszu brakuje pola {blad}") from None
    return Scenariusz(dane.get("nazwa", "bez_nazwy"), swiat, start, cel)