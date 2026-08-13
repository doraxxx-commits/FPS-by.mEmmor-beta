"""
Silnik czasu (punkt 52 Game Planu: "Świat musi żyć podczas symulacji").

W Etapie 1 czas jest reprezentowany jako sezon + numer kolejki —
to najprostsza jednostka, na której da się oprzeć terminarz i tabelę.
Prawdziwy kalendarz dzień-po-dniu (z konkretnymi datami meczów, oknami
transferowymi liczonymi w dniach itd. — punkty 18, 24) dojdzie w Etapie 4,
kiedy transfery będą potrzebowały realnych dat, a nie tylko numeru kolejki.
"""

from __future__ import annotations


class GameCalendar:
    """Śledzi bieżący sezon i kolejkę rozgrywek."""

    def __init__(self, start_season: str = "2026/27") -> None:
        self.season = start_season
        self.matchday = 1

    def advance_matchday(self) -> None:
        """Przechodzi do kolejnej kolejki w obrębie tego samego sezonu."""
        self.matchday += 1

    def advance_season(self) -> None:
        """Kończy bieżący sezon i przechodzi do następnego (np. 2026/27 -> 2027/28)."""
        start_year_str, _ = self.season.split("/")
        next_start = int(start_year_str) + 1
        self.season = f"{next_start}/{str(next_start + 1)[-2:]}"
        self.matchday = 1

    def __repr__(self) -> str:
        return f"<GameCalendar sezon={self.season}, kolejka={self.matchday}>"
