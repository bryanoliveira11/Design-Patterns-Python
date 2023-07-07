"""
Iterator é um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""
from collections.abc import Iterable, Iterator
from typing import Any, List


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self) -> Any:
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def __next__(self) -> Any:
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def __iter__(self) -> Iterator:
        return MyIterator(self._items)

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__} : {self._items}'

    def add(self, item: Any) -> None:
        self._items.append(item)


if __name__ == '__main__':
    mylist = MyList()
    mylist.add('Teste')
    mylist.add('oi')
    mylist.add('2323232')
    print(mylist)

    for value in mylist:
        print(value)

    for value in mylist.reverse_iterator():
        print(value)
