# 2-terms, single operation fraction calculator
# Sample input: "1/2 + 2/3", "1 * 1/2", "2 - 1_1/2"
class FracCalc:
    def __init__(self):
        self.__num1 = 0
        self.__denom1 = 1
        self.__num2 = 0
        self.__denom2 = 1

    def parse_mixed(self, frac):
        container = frac.split("/")
        mixed_half = container[0]
        denom = int(container[1])

        mcontainer = mixed_half.split("_")
        mixed = int(mcontainer[0])
        num = int(mcontainer[1])

        if mixed < 0:
            num *= -1

        num += mixed * denom
        return num

    def parse_num(self, frac):
        container = frac.split("/")
        num = int(container[0])
        return num

    def parse_denom(self, frac):
        container = frac.split("/")
        denom = int(container[1])
        return denom

    # Lazy implementation since 2 vars per frac
    def frac_ops(self, frac_one, frac_two):
        if frac_one.find("/") >= 0:
            if frac_one.find("_") >= 0:
                container = frac_one.split("/")
                self.__num1 = self.parse_mixed(frac_one)
                self.__denom1 = int(container[1])
            else:
                self.__num1 = self.parse_num(frac_one)
                self.__denom1 = self.parse_denom(frac_one)
        else:
            self.__num1 = int(frac_one)
            self.__denom1 = 1

        if frac_two.find("/") >= 0:
            if frac_two.find("_") >= 0:
                container = frac_two.split("/")
                self.__num2 = self.parse_mixed(frac_two)
                self.__denom2 = int(container[1])
            else:
                self.__num2 = self.parse_num(frac_two)
                self.__denom2 = self.parse_denom(frac_two)
        else:
            self.__num2 = int(frac_two)
            self.__denom2 = 1

    def validate(self, operator):
        if ((self.__denom1 == 0) or (self.__denom2 == 0)) or ((operator == "/") and (self.__num2 == 0)):
            print("Divide by 0!")
            return False
        return True

    def gcf(self, num, denom):
        gcf = 1

        if abs(num) < abs(denom):
            smaller = abs(num)
        else:
            smaller = abs(denom)

        for x in range(smaller, 0, -1):
            if (num % x == 0) and (denom % x == 0):
                gcf = x
                break
        return gcf

    def simplify(self, num, denom):
        gcf = self.gcf(num, denom)
        num /= gcf
        denom /= gcf
        num = int(num)
        denom = int(denom)

        if (num == 0) or (denom == 1):
            return str(num)
        elif abs(num) > abs(denom):
            mixed = int(num / denom)
            num %= denom

            if mixed < 0:
                num *= -1
            return str(mixed) + "_" + str(num) + "/" + str(denom)
        else:
            return str(num) + "/" + str(denom)

    def add(self):
        num = (self.__num1 * self.__denom2) + (self.__num2 * self.__denom1)
        denom = self.__denom1 * self.__denom2
        return self.simplify(num, denom)

    def subtract(self):
        num = (self.__num1 * self.__denom2) - (self.__num2 * self.__denom1)
        denom = self.__denom1 * self.__denom2
        return self.simplify(num, denom)

    def multiply(self):
        num = self.__num1 * self.__num2
        denom = self.__denom1 * self.__denom2
        return self.simplify(num, denom)

    def divide(self):
        num = self.__num1 * self.__denom2
        denom = self.__num2 * self.__denom1

        if (denom < 0) and (num != 0):
            num *= -1
            denom *= -1
        return self.simplify(num, denom)

    def prompt(self):
        print("Welcome to the Fraction Calculator!")
        loop = True

        while loop:
            expression = input("Enter an expression (or \"quit\"): ")

            if expression.lower() == "quit":
                print("Goodbye!", end="")
                loop = False
            else:
                equation = expression.split()
                frac_one = equation[0]
                operator = equation[1]
                frac_two = equation[2]

                self.frac_ops(frac_one, frac_two)
                cont = self.validate(operator)

                if cont:
                    # print(self.__num1, "/", self.__denom1,operator, self.__num2, "/", self.__denom2)
                    if operator == "+":
                        print(self.add())
                    elif operator == "-":
                        print(self.subtract())
                    elif operator == "*":
                        print(self.multiply())
                    elif operator == "/":
                        print(self.divide())


def main():
    frac_calc = FracCalc()
    frac_calc.prompt()


if __name__ == "__main__":
    main()
