"""
Club — reprezentuje klub w świecie gry.

W Etapie 1 klub ma tylko to, co potrzebne do symulacji sezonu:
tożsamość, siłę drużyny (do symulacji meczów) oraz statystyki tabelowe.
Skład zawodników, trener, finanse itd. dojdą w kolejnych etapach
(patrz Game Plan: punkty 5-16, 28-29, 58-59) — celowo NIE dodajemy
tu jeszcze tych pól, żeby klasa nie stała się przedwcześnie wielkim
workiem na wszystko.
"""

from __future__ import annotations

import uuid


class Club:
    """Pojedynczy klub piłkarski."""

    def __init__(self, name: str, country: str, strength: int) -> None:
        """
        Args:
            name: nazwa klubu, np. "Legia Warszawa".
            country: kraj klubu, np. "Polska".
            strength: siła drużyny w skali 1-100, używana do symulacji
                meczów w Etapie 1 (odpowiednik "przeciętnego OVR kadry").
                W kolejnych etapach strength będzie WYLICZANA ze składu
                zawodników, a nie ustawiana ręcznie.
        """
        if not (1 <= strength <= 100):
            raise ValueError("strength musi być w zakresie 1-100")

        self.id: str = str(uuid.uuid4())
        self.name = name
        self.country = country
        self.strength = strength

        # Reset na początku każdego sezonu przez SeasonEngine.
        self.reset_season_stats()

    def reset_season_stats(self) -> None:
        """Zeruje statystyki tabelowe — wywoływane na starcie nowego sezonu."""
        self.played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0

    @property
    def goal_difference(self) -> int:
        return self.goals_for - self.goals_against

    @property
    def points(self) -> int:
        return self.wins * 3 + self.draws

    def register_result(self, goals_for: int, goals_against: int) -> None:
        """Aktualizuje statystyki klubu po rozegranym meczu."""
        self.played += 1
        self.goals_for += goals_for
        self.goals_against += goals_against

        if goals_for > goals_against:
            self.wins += 1
        elif goals_for == goals_against:
            self.draws += 1
        else:
            self.losses += 1

    def __repr__(self) -> str:
        return f"<Club {self.name} ({self.country}), siła={self.strength}>"
