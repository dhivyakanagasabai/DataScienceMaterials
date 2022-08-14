class Practice:
    def isArmstrong(self, num):
        x = str(num)
        sum = 0
        for i in range(len(x)):
            cube = int(x[i])**3
            sum = sum + cube
        if num == sum:
            return "The given number is armstrong number"
        else:
            return "The given number is not an armstrong number"

solution = Practice()
print(solution.isArmstrong(371))