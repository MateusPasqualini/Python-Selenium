import random
import string


class Person:

    # Construtora da classe Person
    def __init__(self):
        self.nome = "Mad"
        self.last = "Max"
        self.senha = "123456"
        self.dia = "7"
        self.mes = "6"
        self.ano = "1995"
        self.endereco = "Rua de teste"
        self.cidade = "Cidade Teste"
        self.estado = "29"
        self.postal = "00000"
        self.email = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(13)) + "@automation.com"
        self.celular = "(51)982521227"


    #método get para testes
    def getname(self):
        return self.nome


    #método get para testes
    def getendereco(self):
        return self.endereco

#if para testes apenas no escopo deste programa
if __name__ == '__main__':
    P1 = Person()
    print(P1.nome)
    print(P1.last)
    print(P1.senha)
    print(P1.dia)
    print(P1.mes)
    print(P1.ano)
    print(P1.endereco)
    print(P1.cidade)
    print(P1.estado)
    print(P1.postal)
    print(P1.email)
    print(P1.celular)
