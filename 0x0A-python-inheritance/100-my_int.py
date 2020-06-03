#!/usr/bin/python3
"""
 module that creates a class named MyInt
"""


class MyInt(int):
    """
     class named MyInt
    """

    def __eq__(self, other):
        """Swaps the eq builtin"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Swaps the ne builtin"""
        return int.__eq__(self, other)
