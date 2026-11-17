from pathlib import Path

import pytest

from autonomia.domena.bledy import BladScenariusza
from autonomia.wczytywanie import wczytaj_scenariusz

PRZYKLAD = Path(__file__).parent.parent / "scenarios" / "magazyn_01.yaml"


def _zapisz(tmp_path, tresc):
    sciezka = tmp_path / "scenariusz.yaml"
    sciezka.write_text(tresc, encoding="utf-8")
    return sciezka


def _tresc(bloki="  []", start="{x: 1, y: 1}", cel="{x: 8, y: 8}"):
    return f"""
nazwa: test
swiat: {{szerokosc: 10, wysokosc: 10}}
szare_bloki:
{bloki}
robot:
  start: {start}
  cel: {cel}
"""


def test_przykladowy_scenariusz_wczytuje_sie_poprawnie():
    s = wczytaj_scenariusz(PRZYKLAD)
    assert s.nazwa == "magazyn_01"
    assert s.swiat.szerokosc == 40
    assert s.swiat.wysokosc == 25
    assert len(s.swiat.bloki) == 4
    assert s.start == (2, 12)
    assert s.cel == (37, 20)


def test_brak_pliku_zglasza_blad_scenariusza(tmp_path):
    with pytest.raises(BladScenariusza):
        wczytaj_scenariusz(tmp_path / "nie_ma_takiego.yaml")


def test_niepoprawny_yaml_zglasza_blad_scenariusza(tmp_path):
    with pytest.raises(BladScenariusza):
        wczytaj_scenariusz(_zapisz(tmp_path, "swiat: ["))


def test_brak_sekcji_swiat_zglasza_blad_scenariusza(tmp_path):
    tresc = "nazwa: test\nrobot:\n  start: {x: 1, y: 1}\n  cel: {x: 2, y: 2}\n"
    with pytest.raises(BladScenariusza):
        wczytaj_scenariusz(_zapisz(tmp_path, tresc))


def test_nieznany_typ_bloku_zglasza_blad_scenariusza(tmp_path):
    bloki = "  - {typ: trojkat, x: 3, y: 3}"
    with pytest.raises(BladScenariusza):
        wczytaj_scenariusz(_zapisz(tmp_path, _tresc(bloki=bloki)))


def test_brak_pola_w_bloku_zglasza_blad_scenariusza(tmp_path):
    bloki = "  - {typ: prostokat, x: 3, y: 3, szerokosc: 2}"
    with pytest.raises(BladScenariusza):
        wczytaj_scenariusz(_zapisz(tmp_path, _tresc(bloki=bloki)))


def test_blok_poza_mapa_zglasza_blad_scenariusza(tmp_path):
    bloki = "  - {typ: prostokat, x: 9, y: 3, szerokosc: 5, wysokosc: 2}"
    with pytest.raises(BladScenariusza):
        wczytaj_scenariusz(_zapisz(tmp_path, _tresc(bloki=bloki)))