#In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.



def factorial(n):
    j = 1
    if n > 12 or n < 0:
        raise ValueError
    for i in range(1, n+ 1):
        j *= i
    return j