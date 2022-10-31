from math import sqrt

class ListVec(list):
    
    def vec_sum(self, vec):
        
        assert len(self) == len(vec)        
        for i in range(len(self)):
            self[i] += vec[i]
        return self
    
    def scalar_mul(self, scalar):        
        for i in range(len(self)):
            self[i] = self[i]*scalar
        return self
    
    def dot(self, vec):
        
        assert len(self) == len(vec)                  
        n = 0
        for i in range(len(self)):
            n += self[i] * vec[i]
        return n

    def norm(self):
        n = self.dot(self)
        print(n)
        return n**(1/2)
    
    def similarity(self, b):        

        assert len(self) == len(b)
        denominador = sqrt(self.dot(self))*sqrt(b.dot(b))
        return self.dot(b)/denominador