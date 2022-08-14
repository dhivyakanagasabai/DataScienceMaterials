class Practice:
    def solution(self, ar, b):
        print(ar.count(b))
        print([ar.count(i)//2 for i in set(ar)])
        return sum([ar.count(i)//2 for i in set(ar)])

solve = Practice()
print(solve.solution([10, 20, 20, 10, 10, 30, 50, 10, 20],10)) 

