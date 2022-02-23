#You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
#Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    else:
        full_string = []
        spaces = n //2
        stars = 1
        while(stars < n):
            full_string.append(" " * spaces + '*' * stars + '\n')
            spaces -= 1
            stars += 2
        while(stars > 0):
            full_string.append(" " * spaces + "*" * stars + '\n')
            stars -= 2
            spaces += 1
        result = ''.join(full_string)
        return result
    