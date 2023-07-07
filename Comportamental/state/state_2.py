"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class Sound:
    def __init__(self) -> None:
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self, mode: PlayMode) -> None:
        self.playing = 0
        self.mode = mode
        print(f'Mudando Para Mode : {mode.__class__.__name__}')

    def press_next(self) -> None:
        self.mode.press_next()
        print(self)

    def press_prev(self) -> None:
        self.mode.press_prev()
        print(self)

    def __str__(self) -> str:
        return str(self.playing)


class PlayMode(ABC):
    def __init__(self, sound: Sound) -> None:
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None: pass

    @abstractmethod
    def press_prev(self) -> None: pass


class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1000

    def press_prev(self) -> None:
        self.sound.playing -= 1000 if self.sound.playing > 0 else 0


class MusicMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1

    def press_prev(self) -> None:
        self.sound.playing -= 1 if self.sound.playing > 0 else 0


if __name__ == "__main__":
    sound = Sound()
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    print()
    sound.change_mode(MusicMode(sound))
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.change_mode(RadioMode(sound))
