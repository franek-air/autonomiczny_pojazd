import pytest

from autonomia.domena.bledy import BladScenariusza
from autonomia.domena.ksztalty import Prostokat
from autonomia.domena.scenariusz import Scenariusz
from autonomia.domena.swiat import Swiat


def _swiat_z_regalem():
    swiat = Swiat(szerokosc=10, wysokosc=10)
    swiat.dodaj_blok(Prostokat(x=4, y=4, szerokosc=2, wysokosc=2))
    return swiat


def test_poprawny_scenariusz_zapamietuje_dane():
    swiat = _swiat_z_regalem()
    s = Scenariusz("test", swiat, start=(1, 1), cel=(8, 8))
    assert s.nazwa == "test"
    assert s.swiat is swiat
    assert s.start == (1, 1)
    assert s.cel == (8, 8)


def test_start_w_bloku_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Scenariusz("test", _swiat_z_regalem(), start=(5, 5), cel=(8, 8))


def test_cel_w_bloku_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Scenariusz("test", _swiat_z_regalem(), start=(1, 1), cel=(5, 5))


def test_start_poza_mapa_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Scenariusz("test", _swiat_z_regalem(), start=(-1, 1), cel=(8, 8))


def test_cel_poza_mapa_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Scenariusz("test", _swiat_z_regalem(), start=(1, 1), cel=(11, 8))