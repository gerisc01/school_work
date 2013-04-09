class Fraction:
    def __init__(self,inum,iden):
        self.num = inum
        self.den = iden

    def __str__(self):
        s = str(self.num) + "/" + str(self.den)
        return s

    def simplify(self):
        m = self.num
        n = self.den
        while n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
        self.num = self.num//m
        self.den = self.den//m

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.getDen() + self.den * otherfraction.getNum()
        newden = self.den * otherfraction.getDen()
        newf = Fraction(newnum, newden)
        newf.simplify()
        return newf

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.getDen() - self.den * otherfraction.getNum()
        newden = self.den * otherfraction.getDen()
        newf = Fraction(newnum, newden)
        newf.simplify()
        return newf

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.getNum()
        newden = self.den * otherfraction.getDen()
        newf = Fraction(newnum, newden)
        newf.simplify()
        return newf
    
    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.getDen()
        newden = self.den * otherfraction.getNum()
        newf = Fraction(newnum, newden)
        newf.simplify()
        return newf
    
