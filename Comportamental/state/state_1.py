"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class Order:
    # Context
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        print('Tentando executar pending()')
        self.state.pending()
        print(f'Estado Atual : {self.state}')
        print()

    def approved(self):
        print('Tentando executar approved()')
        self.state.approve()
        print(f'Estado Atual : {self.state}')
        print()

    def reject(self):
        print('Tentando executar reject()')
        self.state.reject()
        print(f'Estado Atual : {self.state}')
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento já Pendente, nada será feito')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento Aprovado !')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento Rejeitado !')


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento Pendente !')

    def approve(self) -> None:
        print('Pagamento já está Aprovado, nada será feito')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento Rejeitado !')


class PaymentRejected(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento Pendente !')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento Aprovado !')

    def reject(self) -> None:
        print('Pagamento já está Rejeitado, nada será feito')


if __name__ == '__main__':
    order1 = Order()
    order1.pending()
    order1.approved()
    order1.approved()
    order1.reject()
