"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de Luxo Está Buscando Cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro Popular Está Buscando Cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto Luxo Está Buscando Cliente...')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto Popular Está Buscando Cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo: str) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # método que cria um objeto
        match tipo:
            case 'popular':
                return CarroPopular()
            case 'luxo':
                return CarroLuxo()
            case 'moto_luxo':
                return MotoLuxo()
            case 'moto_popular':
                return MotoPopular()
            case _:
                raise ValueError("Veículo Não Existe")


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # método que cria um objeto
        if tipo == 'popular':
            return CarroPopular()
        else:
            raise ValueError("Veículo Não Existe")


if __name__ == '__main__':
    from random import choice

    veiculos_disponiveis_zona_norte = [
        'luxo', 'popular', 'moto_luxo', 'moto_popular']

    veiculos_disponiveis_zona_sul = ['popular']

    print('ZONA NORTE')
    for i in range(10):
        carro_norte = ZonaNorteVeiculoFactory(
            choice(veiculos_disponiveis_zona_norte)
        )
        carro_norte.buscar_cliente()

    print()
    print('ZONA SUL')
    for i in range(10):
        carro_sul = ZonaSulVeiculoFactory(
            choice(veiculos_disponiveis_zona_sul)
        )
        carro_sul.buscar_cliente()
