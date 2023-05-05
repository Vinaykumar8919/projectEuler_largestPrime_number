
# import sys
# --------program1----------------
# def isPalindrome(n):
#     n = str(n)
#     rev = n[len(n)::-1]
#     if n==rev:
#         return 1
#     return 0
        
    
# def isThreeDigitProduct(n):
#     for i in range(100 ,999):
#         if n%i==0:
#             temp = str(n//i)
#             if len(temp)==3:
#                 return True
#     return False

# def solution(n):
#     sol=0
#     for i in range(n,10001,-1):
#         if isPalindrome(i):
#             if isThreeDigitProduct(i):
#                 return i
#     return 0     
                
# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     print(solution(n))
# ---------------program 2--------------
# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     palindromes = []
#     for i in range(999,99,-1):
#         for j in range(i,99,-1):
#             ele = i*j
#             if ele not in palindromes and str(ele)==str(ele)[::-1]:
#                 palindromes.append(ele)
#     palindromes.sort()
#     length = len(palindromes)
#     for i in range(length-1,-1,-1):
#         if palindromes[i]<n:
#             print(palindromes[i])
#             break

# ------------program3---------------

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    largest_palindrome = 0
    
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            num = i*j
            
            if (num <= largest_palindrome):
                break
            else:
                if ((num < n) and (str(num) == str(num)[::-1])):
                    largest_palindrome = num
                    break
            
    print(largest_palindrome)

