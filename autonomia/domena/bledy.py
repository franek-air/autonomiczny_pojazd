"""Własne wyjątki programu.

Wszystkie dziedziczą po BladAutonomii, więc kod wywołujący może złapać
dowolny błąd domenowy jednym `except BladAutonomii`.
"""


class BladAutonomii(Exception):
    """Bazowy wyjątek dla wszystkich błędów zgłaszanych przez program."""


class BladSterowania(BladAutonomii):
    """Niepoprawne sygnały sterujące (np. gaz i hamulec naraz)."""