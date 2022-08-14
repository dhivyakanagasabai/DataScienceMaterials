class Practice:
    def find_prime_factors(self, n):
        prime_factors_list = []
        for i in range(1,n+1):
            prime = solution.isPrime(i)            
            if prime and n%i==0:
                prime_factors_list.append(i)
        return prime_factors_list
    
    def isPrime(self, n):
        flag = True
        for i in range(2,n):
                if n%i == 0:
                    flag = False
                    break
        return flag
        
    def find_factors(self, n):
        factors_list = []
        for i in range(1,n+1):                      
            if n%i==0:
                factors_list.append(i)
        return factors_list

solution = Practice()
print("Prime factors: ", solution.find_prime_factors(20))
print("Factors: ", solution.find_factors(20))