class Fraction:
    def __init__(self, numer = 0, denom = 1):
        self.num = numer
        if denom == 0: denom = 1
        self.den = denom

    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den

    def __str__(self):
        return str(self.getNum()) + '/' + str(self.getDen())

    def reduzir(self):
        menor = self.getNum()
        if self.getDen() < self.getNum():
            menor = self.getDen()

        for i in range(menor, 1, -1):
            if self.getNum() % i == 0 and self.getDen() % i == 0:
                self.num //= i
                self.den //= i

    def __add__(self, f2):
        f3 = Fraction()
        f3.num = (self.getNum() * f2.getDen()) + (f2.getNum() * self.getDen())
        f3.den = self.getDen() * f2.getDen()
        f3.reduzir()
        return f3
    
    def __sub__(self, f2):
        f3 = Fraction()
        f3.num = (self.getNum() * f2.getDen()) - (f2.getNum() * self.getDen())
        f3.den = self.getDen() * f2.getDen()
        f3.reduzir()
        return f3
    
    def __mul__(self, f2):
        f3 = Fraction()
        f3.num = self.getNum() * f2.getNum()
        f3.den = self.getDen() * f2.getDen()
        f3.reduzir()
        return f3
    
    def __truediv__(self, f2):
        f3 = Fraction()
        f3.num = self.getNum() * f2.getDen()
        f3.den = self.getDen() * f2.getNum()
        f3.reduzir()
        return f3

    def __gt__(self, f2):
        if self.getNum()/self.getDen() > f2.getNum()/f2.getDen():
            return True
        else:
            return False
        
    def __ge__(self, f2):
        if self.getNum()/self.getDen() >= f2.getNum()/f2.getDen():
            return True
        else:
            return False
        
    def __lt__(self, f2):
        if self.getNum()/self.getDen() < f2.getNum()/f2.getDen():
            return True
        else:
            return False
        
    def __le__(self, f2):
        if self.getNum()/self.getDen() <= f2.getNum()/f2.getDen():
            return True
        else:
            return False
        
    def __eq__(self, f2):
        if self.getNum()/self.getDen() == f2.getNum()/f2.getDen():
            return True
        else:
            return False
        
    def __ne__(self, f2):
        if self.getNum()/self.getDen() != f2.getNum()/f2.getDen():
            return True
        else:
            return False
        
if __name__ == "__main__":
    menu = "1 - Criar Frações\n2 - Reduzir frações\n3 - Mostrar Frações\n4 - Resultado das operações matemáticas\n5 - Resultado das operações relacionais\n0 - Sair"
    opcao = "ç"
    fracoes_criadas = False
    
    while opcao != "0":
        opcao = "ç"
        print(menu)
        while opcao not in ["1", "2", "3", "4","5","0"]:
            opcao = input("Escolha uma opção: ")
            if opcao not in ["1", "2", "3", "4","5","0"]:
                print("Opcao inválida")

        if opcao == "0": break
        elif opcao == "1":
            num1 = int(input("Numerador da fracao 1: "))
            den1 = 0
            while den1 == 0:
                den1 = int(input("Denominador da fracao 1: "))
                if den1 == 0:
                    print("Denominador não pode ser 0")

            num2 = int(input("Numerador da fracao 2: "))
            den2 = 0
            while den2 == 0:
                den2 = int(input("Denominador da fracao 1: "))
                if den2 == 0:
                    print("Denominador não pode ser 0")
            f1 = Fraction(num1, den1)
            f2 = Fraction(num2, den2)
            print("Fracoes criadas")
            fracoes_criadas = True
        if fracoes_criadas:
            if opcao == "2":
                f1.reduzir()
                f2.reduzir()
            elif opcao == "3":
                print(f"Fracao 1: {f1}")
                print(f"Fracao 2: {f2}")
            elif opcao == "4":
                print(f"Soma = {f1 + f2}")
                print(f"Subtracao = {f1 - f2}")
                print(f"Multiplicacao = {f1 * f2}")
                print(f"Divisao = {f1 / f2}")
            elif opcao == "5":
                print(f"f1 < f2 = {f1 < f2}")
                print(f"f1 <= f2 = {f1 <= f2}")
                print(f"f1 > f2 = {f1 > f2}")
                print(f"f1 >= f2 = {f1 >= f2}")
                print(f"f1 == f2 = {f1 == f2}")
                print(f"f1 != f2 = {f1 != f2}")
            
        else:
            print("Fracoes ainda nao foram criadas")

        print()

    