# Filename : e_tothe_nth_digit.py

# find e to the nth digit.
# enter a number and generate e up that many decimal places

from math import e


def e_with_precision(n):
    """Return euler's number to the n-th decimal place
    :param n: number of decimal places to return
    :type n: int
    :return: euler's number with n decimal places
    :rtype: str
    """
    return '%.*f' % (n, e)

if __name__ == '__main__':
    # there is no do while loop in python, so we need to improvise
    correct_input = False
    while not correct_input:
        # ask until you get correct input
        print('Precision must be between 1 and 51')
        precision = int(raw_input('Number of decimal places: '))
        if 51 >= precision > 0:
            correct_input = True
    print(e_with_precision(precision))
