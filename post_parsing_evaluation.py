
  # classes to create term objects; this is intended to aid in evaluating individual terms

  # the user-entered polynomial is intended to be evaluated at the lower bound, a, the upper bound, b, and the midpoint, c.

import re
import expression_parsing_func
from term_parsing_module_v1 import *


class PolyTerm:
    """
    The values of interval_lower_bound and interval_upper_bound ought to be capable of changing, or updating,
    in order to re-evaluate terms multiple times with their variables representing new values in each new iteration.
    """

    def __init__(self, term_elements_list, interval_lower_bound, interval_upper_bound):
        self.term_elements_list = term_elements_list
        self.max_index = len(term_elements_list)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.max_index:
            raise StopIteration
        self.index = self.index + 1
        return self.term_elements_list[self.index]

    def evaluate(self, variable_value):
        """
        Values of coefficients and exponents can be created by concatenating strings of number-characters
        and converting the string into integer type or floating-point type, using int() or float().

        Evaluation of terms ought to be in accordance with the order of operations, P.E.M.D.A.S..
        """
