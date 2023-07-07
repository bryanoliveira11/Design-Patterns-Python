"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""
from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass


class Control(IControl):
    def top(self) -> None:
        print('Movendo para cima')

    def right(self) -> None:
        print('Movendo para direita')

    def down(self) -> None:
        print('Movendo para baixo')

    def left(self) -> None:
        print('Movendo para esquerda')


class NewControl:
    def move_top(self) -> None:
        print('Movendo para cima')

    def move_right(self) -> None:
        print('Movendo para direita')

    def move_down(self) -> None:
        print('Movendo para baixo')

    def move_left(self) -> None:
        print('Movendo para esquerda')


class ControlAdapter:
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()

    def right(self) -> None:
        self.new_control.move_right()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()


class ControlAdapter2(Control, NewControl):
    def top(self) -> None:
        self.move_top()

    def right(self) -> None:
        self.move_right()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()


if __name__ == '__main__':
    new_control = NewControl()
    c1 = ControlAdapter(new_control)
    c1.top()

    c2 = ControlAdapter2()
    c2.top()
