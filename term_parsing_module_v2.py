

import re


class TermElements:
    """
    This class is intended to be the super-class of all term-element classes
    """

    def __init__(self, term, var_input_value):
        self.term = term
        self.var_input_value = float(var_input_value)
        self.post_parse_sub = self.ElementSubtraction()
        self.post_parse_coef = self.ElementCoefficient()
        self.post_parse_var = self.ElementVariable()
        self.post_parse_exp = self.ElementExponent()

    class ElementSubtraction:
        """
        This class is intended to correspond to the "minus_" prefixes present in the elements of subtracted terms
        """

        def __init__(self, boolean=None):
            self._minus_prefix = None
            self.boolean = boolean  # for checking if the element is present in the term

        @property
        def minus_prefix(self):
            return self._minus_prefix

        @minus_prefix.setter
        def minus_prefix(self, value):
            if self.boolean:
                self._minus_prefix = value

        @minus_prefix.deleter
        def minus_prefix(self):
            del self._minus_prefix

    class ElementCoefficient:

        def __init__(self, boolean=None):
            self._coefficient_value = 1
            self.boolean = boolean  # For checking if the element is present in the term

        @property
        def coefficient_value(self):
            return self._coefficient_value

        @coefficient_value.setter
        def coefficient_value(self, value):
            if self.boolean:
                self._coefficient_value = float(value)

        @coefficient_value.deleter
        def coefficient_value(self):
            del self._coefficient_value

        def __truediv__(self, a):
            return self.coefficient_value / a

        def __mul__(self, a):
            return self.coefficient_value * a

        def __pow__(self, a):
            return self.coefficient_value ** a

    class ElementVariable:

        def __init__(self, boolean=None):
            self._variable_value = 1
            self.boolean = boolean  # to check if the element is present in the term.

        @property
        def variable_value(self):
            return self._variable_value

        @variable_value.setter
        def variable_value(self, value):
            if self.boolean:
                self._variable_value = float(value)

        @variable_value.deleter
        def variable_value(self):
            del self._variable_value

        def __truediv__(self, a):
            return self.variable_value / a

        def __mul__(self, a):
            return self.variable_value * a

        def __pow__(self, a):
            return self.variable_value ** a

    class ElementExponent:

        def __init__(self, notation_boolean=None, value_boolean=None):
            self._exponent_value = 1
            self.notation_boolean = notation_boolean  # To check if exponent notation is present in the term.
            self.value_boolean = value_boolean  # To check if an exponent value if present in the term.

        @property
        def exponent_value(self):
            return self._exponent_value

        @exponent_value.setter
        def exponent_value(self, value):
            if self.notation_boolean and self.value_boolean:
                self._exponent_value = float(value)

        @exponent_value.deleter
        def exponent_value(self):
            del self._exponent_value

            
    def term_parser(self, term):
        """
        A function to convert terms, extracted from the user-entered polynomial, into lists of elements of terms.
        The function will return a list of 'term elements' extrapolated from the argument to the function.

        The argument corresponding to the "term" parameter is intended to be the "term" data attribute of the class
        instance that the method is being invoked from.
        """

        term_items = []  # list intended to contain term elements after parsing

        # compilation of patterns to match various parts of terms
        separator_pattern = re.compile(r"(?P<separator>&)")  # a prefix to mark the beginning of a new term, to separate terms
        subtraction_pattern = re.compile(r"(?P<subtraction>(?<=&)minus_)")  # the prefix of terms that were originally subtracted in the user-entered expression
        coefficient_pattern = re.compile(r"(?P<coefficient>(?<=&)(?:minus_)*(\d*))")
        variable_pattern = re.compile(r"(?P<variable>(?<=&)(?:minus_)*(?:\d*)([abcdefghjklopqrtuvwxyz]))")  # variable_pattern often matches with charactes of 'minus_'
        exponent_notation_pattern = re.compile(r"(?P<exp_notation>\*{2}|\^|\^{2})")
        exponent_pattern_one = re.compile(r"(?P<exp_one>(?<=\*{2}|\^{2})(\d*))")  # a digit character preceded by two repetitions of either an asterisk or a caret
        exponent_pattern_two = re.compile(r"(?P<exp_two>(?<=\^)(\d*))")  # a digit character preceded by a single caret

        # try:
        for i in range(1):  # single iteration of parsing the term, to search for 4 character types: coefficients, variables, exponent notations, and exponent values.

            extra_minus_search = re.search(r"^&minus_$", term)  # for the case of the expression beginning with a negative term
            if extra_minus_search:
                continue

            separator_search = separator_pattern.search(term)  # for if certain implementations would, for example, append all elements of an expression into one list
            if separator_search:
                term_items.append(separator_search.group("separator"))  # to indicate the beginning of a new term, or, the separation of terms

            subtraction_search = subtraction_pattern.search(term)
            if subtraction_search:
                term_items.append(subtraction_search.group("subtraction"))  # to indicate the term is being subtracted from the expression
                # this will be utilized in the evaluation portion of the program
                self.post_parse_sub.boolean = True
                self.post_parse_sub.minus_prefix.setter()

            coefficient_search = coefficient_pattern.search(term)
            if coefficient_search:
                term_items.append(coefficient_search.group(2))  # appending coefficients, if they are present
                self.post_parse_coef.boolean = True
                self.post_parse_coef.coefficient_value.setter(coefficient_search.group(2))

            variable_search = variable_pattern.search(term)
            if variable_search:
                term_items.append(variable_search.group(2))  # appending variables, if they are present
                self.post_parse_var.boolean = True
                self.post_parse_var.variable_value.setter(self.var_input_value)

            exp_notation_search = exponent_notation_pattern.search(term)
            if exp_notation_search:
                term_items.append(exp_notation_search.group('exp_notation'))  # appending exponent notations, if they are present
                self.post_parse_exp.notation_boolean = True

            exponent_search_one = exponent_pattern_one.search(term)
            if exponent_search_one:
                term_items.append(exponent_search_one.group('exp_one'))  # appending exponent values, if they are present
                self.post_parse_exp.value_boolean = True
                self.post_parse_exp.exponent_value.setter(exponent_search_one.group('exp_one'))

            exponent_search_two = exponent_pattern_two.search(term)
            if not exponent_search_one:  # contingency for alternative exponent notation
                if exponent_search_two:
                    term_items.append(exponent_search_two.group('exp_two'))  # appending exponent values, if they are present.
                    self.post_parse_exp.value_boolean = True
                    self.post_parse_exp.exponent_value.setter(exponent_search_two.group('exp_two'))

        print("\n")
        print("The term parsed: " + self.term)
        print("Number of character elements in the term: " + str(len(term_items)))
        print(term_items)

        return term_items

    def evaluate_term(self):
        """
        This function is intended to return the final value of the entire term after it's parsing.
        """

        if self.post_parse_exp.notation_boolean and self.post_parse_exp.value_boolean:  # presence of exponent notation and an exponent value
            if self.post_parse_var.boolean:  # presence of a variable
                var_to_the_exp = self.post_parse_var.__pow__(self.post_parse_exp)
            else:
                var_to_the_exp = self.post_parse_var

            if self.post_parse_coef.boolean:  # presence of coefficient after presence of an exponent
                var_times_coef = var_to_the_exp.__mul__(self.post_parse_coef)
            else:  # absence of a coefficient
                var_times_coef = var_to_the_exp

            if self.post_parse_sub.boolean:  # presence of subtraction signifier
                minus_var_times_coef = var_times_coef.__mul__(self.post_parse_sub)
                return minus_var_times_coef
            else:  # absence of subtraction signifier
                return var_times_coef

        elif not self.post_parse_exp.notation_boolean and self.post_parse_exp.value_boolean:  # absence of exponent notation or exponent value
            if self.post_parse_var.boolean:  # presence of a variable
                if self.post_parse_coef.boolean:  # presence of a coefficient
                    var_times_coef = self.post_parse_var.__mul__(self.post_parse_coef)
                else:  # absence of a coefficient
                    var_times_coef = self.post_parse_var

            if self.post_parse_sub.boolean:  # presence of subtraction signifier
                minus_var_times_coef = var_times_coef.__mul__(self.post_parse_sub)
                return minus_var_times_coef
            else:
                return var_times_coef
