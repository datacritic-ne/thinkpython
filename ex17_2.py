#! python3

from __future__ import print_function

class Kangaroo:
    """
    Represents a kangaroo with a pouch.

    Attributes: contents of the pouch.
    """

    def __init__(self, pouch_contents):
        """
        Initializes a kangaroo object.

        The kangaroo's pouch is empty
        """

        self.pouch_contents = pouch_contents
        self.pouch_contents = []

    def put_in_pouch(self, item):

        self.pouch_contents.append(item)

    def __str__(self):
        print(self)
        print(self.pouch_contents)

def main():

    kanga = Kangaroo()
    roo = Kangaroo()

    kanga.put_in_pouch(roo)

    print(kanga)

if __name__ == '__main__':
    main()