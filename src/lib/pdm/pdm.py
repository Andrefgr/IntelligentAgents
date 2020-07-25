class PDM:
    
    def __init__(self, gama, delta_max):
        
        self._gama = gama
        self._delta_max = delta_max
        
        
    def gama(self):
        
        return self._gama
        
        
    def delta_max(self):
        
        return self._delta_max
        
        
    def utilidade(self, modelo):
        
        S, A = modelo.S, modelo.A
        
        U = {s : 0 for s in S()}
        
        while True:
            
            Uant = U.copy() # Backup de U
            delta = 0
            for s in S():
                U[s] = max(self.util_accao(s, a, Uant, modelo) for a in A(s))
                delta = max(delta, abs(U[s] - Uant[s]))
                
            if delta < self._delta_max:
                break
        
        return U # Utilidade
        
        
    def util_accao(self, s, a, U, modelo):
        
        T, R, gama = modelo.T, modelo.R, self._gama
        return sum(p * (R(s, a, sn) + gama * U[sn]) for (p, sn) in T(s, a)) # double
        
        
    def politica(self, U, modelo):
          
        A, S = modelo.A, modelo.S
        
        pia = {s : max(A(s), key = lambda a : self.util_accao(s, a, U, modelo)) for s in S()}

        return pia # Politica
    
    
    def resolver(self, modelo):
        U = self.utilidade(modelo)
        P = self.politica(U, modelo)
        return U, P # Tuple<E1 -> Utilidade, E2 -> Politica>