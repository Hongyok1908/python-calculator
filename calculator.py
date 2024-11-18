class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        sign = -1 if (a < 0) ^ (b < 0) else 1
        result = 0
        for i in range(abs(b)):
            result = self.add(result, abs(a))
            
        return sign * result

    def divide(self, a, b):
        if b == 0:
            return None
        
        sign = -1 if (a < 0) ^ (b < 0) else 1
        a = abs(a)
        b = abs(b)
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        
        return sign * result
    
    def modulo(self, a, b):
        if b == 0:
            return None

        sign = 1 if a >= 0 else -1
        a = abs(a)
        b = abs(b)
        while a >= b:
            a = self.subtract(a, b)
        return sign * a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))