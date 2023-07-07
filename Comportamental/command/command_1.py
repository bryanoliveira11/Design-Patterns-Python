"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    # Receiver

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'Light "{self.name}" in "{self.room_name}" is now ON')

    def off(self) -> None:
        print(f'Light "{self.name}" in "{self.room_name}" is now OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'Light "{self.name}" in "{self.room_name}" is now {self.color}')


class ICommand(ABC):
    # Interface de Comando

    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    # Comando Concreto

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class ChangeLightColor(ICommand):
    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self):
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self):
        self.light.change_color(self._old_color)


class RemoteController:
    # Invoker

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_pressed(self, name: str) -> None:

        if name not in self._buttons:
            print('Invalid Button !')
            return

        self._buttons[name].execute()
        self._undos.append((name, 'execute'))

    def button_undo(self, name: str) -> None:

        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    def global_undo(self) -> None:
        if not self._undos:
            print('nothing to undo')
            return None

        button_name, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()


if __name__ == '__main__':
    light1 = Light('my light', 'my room')
    light2 = Light('the light', 'the room')

    light1_on = LightOnCommand(light1)
    light2_on = LightOnCommand(light2)

    remote = RemoteController()
    remote.button_add_command('btn1_ON', light1_on)
    remote.button_add_command('btn2_ON', light2_on)

    remote.button_pressed('btn1_ON')
    remote.button_pressed('btn2_ON')
    remote.button_undo('btn1_ON')

    print()

    light1_red = ChangeLightColor(light1, 'red')
    remote.button_add_command('red_color', light1_red)

    light1_blue = ChangeLightColor(light1, 'blue')
    remote.button_add_command('blue_color', light1_blue)

    remote.button_pressed('red_color')
    remote.button_pressed('blue_color')

    remote.button_undo('blue_color')

    print()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
