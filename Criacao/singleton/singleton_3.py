# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('call é executado')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('new é executado')
#         return super().__new__(cls)

#     def __init__(self, nome) -> None:
#         print('init é executado')
#         self.nome = nome

#     def __call__(self, x, y):
#         print('call chamado', self.nome, x + y)


# p1 = Pessoa('pessoa')
# p1(2, 2)
# print(p1.nome)

from typing import Dict


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.tema = 'Tema escuro'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Tema claro'
    print(as1.tema)
    as2 = AppSettings()
    print(as1.tema)
    print(as2.tema)
