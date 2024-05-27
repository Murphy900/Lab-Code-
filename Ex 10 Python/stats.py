from math import sqrt

class stats:
    
    summ = 0
    N = 0
    sample = []

    def __sub__ (self,other):
        return self.sample - self.other

    def __init__(self,sample):
        
        self.sample = sample
        self.summ = sum(self.sample)
        self.N = len(self.sample)

    def mean(self):
        return self.summ / self.N
    
    def variance(self, bessel = False ):
        var = sum([(x - self.mean())**2 for x in self.sample ])/self.N
        if bessel : var = sum([(x - self.mean())**2 for x in self.sample])/(self.N-1)
        return var
    
    def sigma(self,bessel = False):
        return sqrt(self.variance(bessel))
    
    def sigma_mean(self, bessel = False):
         return self.sigma(bessel)/sqrt(self.N)
    
    def skew(self,bessel = False):
        ske = sum(self.sample - self.mean())**3/(self.sigma()**3*self.N)
        if bessel: ske = sum(self.sample - self.mean())**3/(self.sigma(bessel)**3*(self.N-1))
        return ske
    
    def kurt(self, bessel = False):
        kur = sum(self.sample - self.mean())**4/(self.sigma(bessel)**4*self.N)-3
        if bessel : sum(self.sample - self.mean())**4/(self.sigma(bessel)**4*(self.N-1))-3
        return kur 
    
    def insert(self,x):
        self.sample.append(x)
        self.summ = self.summ + x
        self.N = self.N + 1
