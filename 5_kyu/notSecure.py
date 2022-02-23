#The string has the following conditions to be alphanumeric:

#    At least one character ("" is not valid)
 #   Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
  #  No whitespaces / underscore


def alphanumeric(password):
    return password.isalnum()