class Practice:
    def isPalindrome(self, my_string):
        reversed_string = my_string[::-1]
        if my_string.lower() == reversed_string.lower():
            return "The string is palindrome"
        else:
            return "The string is not palindrome"
    
find = Practice()
print(find.isPalindrome(input("Enter the text to find whether it is palindrome or not: ")))