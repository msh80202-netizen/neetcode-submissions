import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width = None) -> float:
        self.length = length
        self.width = width

        if width == None:
            pi = math.pi * self.length ** 2
            return round(pi, 2)
        else:
            rec = self.length * self.width
            return rec
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
