import pytest

from autonomia.domena.bledy import BladScenariusza
from autonomia.domena.ksztalty import Prostokat


def test_punkt_w_srodku_nalezy_do_prostokata():
    p = Prostokat(x=10, y=5, szerokosc=3, wysokosc=12)
    assert p.zawiera_punkt(11.5, 11)


def test_punkt_poza_prostokatem_nie_nalezy():
    p = Prostokat(x=10, y=5, szerokosc=3, wysokosc=12)
    assert not p.zawiera_punkt(9, 6)


def test_punkt_w_rogu_nalezy_do_prostokata():
    p = Prostokat(x=1, y=2, szerokosc=5, wysokosc=6)
    assert p.zawiera_punkt(1, 2)


def test_punkt_na_krawedzi_nalezy_do_prostokata():
    p = Prostokat(x=0, y=0, szerokosc=2, wysokosc=5)
    assert p.zawiera_punkt(2, 3)


def test_szerokosc_zero_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Prostokat(x=0, y=0, szerokosc=0, wysokosc=5)


def test_szerokosc_ujemna_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Prostokat(x=0, y=0, szerokosc=-1, wysokosc=5)


def test_wysokosc_zero_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Prostokat(x=0, y=0, szerokosc=2, wysokosc=0)


def test_wysokosc_ujemna_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Prostokat(x=0, y=0, szerokosc=2, wysokosc=-2)


def test_punkt_blisko_dolnej_krawedzi_nalezy_do_prostokata():
    p = Prostokat(x=10, y=5, szerokosc=3, wysokosc=12)
    assert p.zawiera_punkt(11.5, 16)