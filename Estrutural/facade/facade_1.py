"""
Façade (Fachada) é um padrão de projeto estrutural
que tem a intenção de fornecer uma interface
unificada para um conjunto de interfaces em um
subsistema. Façade define uma interface de nível
mais alto que torna o subsistema mais fácil de ser
usado.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class IObservable(ABC):
    # Observable

    @property
    @abstractmethod
    def state(self) -> None: pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass


class WeatherStation(IObservable):
    # Observable

    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return

        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name}. O objeto {observable_name} '
              f'acabou de ser atualizado => {self.observable.state}\n')


class WeatherStationFacade:
    def __init__(self) -> None:
        self.weather_station = WeatherStation()
        self.smartphone = Smartphone("samsung", self.weather_station)
        self.outro_smartphone = Smartphone(
            "outro_smartphone", self.weather_station)
        self.weather_station.add_observer(self.smartphone)
        self.weather_station.add_observer(self.outro_smartphone)
        self.weather_station.remove_observer(self.smartphone)
        self.weather_station.reset_state()

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self.weather_station.remove_observer(observer)

    def change_state(self, state: Dict) -> None:
        self.weather_station.state = state

    def remove_smartphone(self):
        self.weather_station.remove_observer(self.smartphone)

    def reset_state(self):
        self.weather_station.reset_state()


if __name__ == '__main__':
    weather_station = WeatherStationFacade()
    weather_station.change_state({'temperature': '30'})
