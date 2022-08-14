class Practice:
    def isPrime(self, n):
        counter = 0
        for i in range(2, n):
            if n%i==0:
                counter+=1
                break
        if counter==0:
            return "The number is prime"
        else:
            return "The number is not prime"

solve = Practice()
print(solve.isPrime(int(input("Enter a number to check whether it is prime or not: "))))
