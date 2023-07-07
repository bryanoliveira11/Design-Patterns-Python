"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    # classe abstrata
    def prepare(self):
        # template method
        self.hook_before_add_ingredients()  # hook
        self.add_ingredients()  # Abstract
        self.hook_after_add_ingredients()  # hook
        self.cook()  # Abstract
        self.cut()  # Concretos
        self.serve()  # Concretos

    def hook_before_add_ingredients(self): pass
    def hook_after_add_ingredients(self): pass

    def cut(self):
        print(f' {self.__class__.__name__}: Cortando Pizza')

    def serve(self):
        print(f' {self.__class__.__name__}: Servindo Pizza')

    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class CheesePizza(Pizza):
    def hook_before_add_ingredients(self):
        print('Doing something before adding ingredients')

    def add_ingredients(self):
        print('Cheese Pizza: Adding Cheese')

    def cook(self):
        print('Cheese: Cooking for 45 minutes')


if __name__ == '__main__':
    p1 = CheesePizza()
    p1.prepare()
