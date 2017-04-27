""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
import pickle


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.p',True)
    1
    >>> update_counter('blah.p')
    2
    >>> update_counter('blah2.p',True)
    1
    >>> update_counter('blah.p')
    3
    >>> update_counter('blah2.p')
    2
    """
    if not reset:
        try:
            counter = int(pickle.load(open(file_name, "rb")))
            counter += 1
            print(counter)
            pickle.dump(str(counter), open(file_name, "wb"))
        except FileNotFoundError:
            open(file_name, 'a').close()
            pickle.dump(str(1), open(file_name, "wb"))
            print(1)
    else:
        open(file_name, 'a').close()
        pickle.dump(str(1), open(file_name, "wb"))
        print(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
