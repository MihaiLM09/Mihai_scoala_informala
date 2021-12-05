

def cmmnc(a,b):
    if a == 0:
        return b
    else:
        return cmmnc(b%a, a)

class Fraction:

    def __init__(self, numarator, numitor):
        self.sus = numarator
        self.jos = numitor

    def __str__(self):
        return str(self.sus)+'/'+str(self.jos)

    def __add__(self, fractionA):
        newsus = self.sus*fractionA.jos + self.jos*fractionA.sus
        newjos = self.jos * fractionA.jos
        common = cmmnc (newsus, newjos)

        return Fraction(newsus//common, newjos//common)

    def __sub__(self, fractionA):
        newsus = self.sus * fractionA.jos - self.jos * fractionA.sus
        newjos = self.jos * fractionA.jos
        common = cmmnc(newsus, newjos)

        return Fraction(newsus // common, newjos // common)

    @classmethod
    def invert(cls, fraction):
        return cls(fraction.jos, fraction.sus)


myf = Fraction(4,3)
print(myf)

myof = Fraction(5,2)
mytf = myf + myof
print(mytf)

myof = Fraction(5,6)
mytf = myf - myof
print(mytf)

print(Fraction.invert(myf))





