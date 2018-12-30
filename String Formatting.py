# Python 3

def print_formatted(number):
    # your code goes here
    bin_number = "{0:b}".format(number)
    l = len(bin_number)
    for i in range(number):
        print(("{0:d}".format(i+1)).rjust(l),("{0:o}".format(i+1)).rjust(l),("{0:X}".format(i+1)).rjust(l),("{0:b}".format(i+1)).rjust(l))