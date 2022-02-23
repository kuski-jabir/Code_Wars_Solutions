#Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

#Rules:

 #   You need to round the answer to 2 decimal places and return it as String.

  #  If the given value is 0 then it should return 0.00

   # You will only be given Natural Numbers as arguments.


def series_sum(n):
    new_list = [1]
    i = 1
    while (n > 1 and n != 0):
        i += 3
        new_list.append(1 / i)
        n = n - 1
    if n == 0:
        return str("%.2f" % 0)
    return str("%.2f" % (round(sum(new_list), 2)))