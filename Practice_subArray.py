class Practice:
    def subArray(self, a):
        res = 0
        for i in range(len(a)):
            for j in range(len(a)):                
                if a[i]+a[j] == 0:
                    res = 1
                else:                  
                    break
        return res

solve = Practice()
print(solve.subArray([2,-3,4,5,1,3]))