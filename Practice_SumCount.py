class Practice:
    def solution(self, a, b):
        count = 0
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i]+a[j] == b:
                    count = count+1
                
        return count

solve = Practice()
print(solve.solution([1,2,3,2,1],5))

