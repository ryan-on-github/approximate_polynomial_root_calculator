

import re


def expression_parser(expression):
    """
    An expression parsing function; to parse the entire user-entered expression and return a list of individual terms.

    If a term is subtracted within the expression, the minus sign must be included in the subtracted term's list item.
    If a term is added within the expression, the plus sign ought to be excluded from the added term's list item.
    """

    def range_len(a_list):  # to more easily utilize the ranges of the lengths of lists.
        return range(len(a_list))

    def post_sub_split_at_add(a_list, list_index):  # create lists of terms from parsing split_at_sub.
        """
        post_sub_split_at_add is intended for parsing added terms after parsing subtracted terms, if subtracted terms
        were present in the user-entered expression.

        There will be a separate process for parsing added terms if subtracted terms are absent from the expression,
        or, in other words, if no terms are subtracted in the user-entered expression.
        """
        return re.split(r"\s?\+\s?", a_list[list_index])

    print("The entered expression: " + expression)

    split_at_sub = re.split(r"\s?-\s?", expression)  # create lists of terms from parsing user-entered expression.

    mapped_split_at_sub = map(lambda x: "minus_" + x, split_at_sub)  # marking strings adjacent to a minus sign.

    intermediate_terms = list(mapped_split_at_sub)

    if re.search(r"\s*-\s*", expression):
        if split_at_sub:  # True if subtraction signs were present in the user-entered expression.
            for i in range_len(intermediate_terms):
                minus_match = re.match(r"minus_(\w+)", intermediate_terms[i])
                if minus_match:
                    if i == 0:  # the first string of the split expression.
                        first_term_match = re.match(r"minus_(((\w*(\*\*)*(\^)*\w*\s*)\+*-*)*)", intermediate_terms[i])
                        if first_term_match:
                            intermediate_terms[i] = first_term_match.group(1)
                    if i != 0:  # THIS SECTION OUGHT TO BE FURTHER CONTEMPLATED ABOUT.
                        pre_minus_match = re.match(r"minus_(\w*(\*\*)*(\^)*\w*)", intermediate_terms[i - 1])
                        # if a term is subtracted, commonly, it is the term written to the right of the minus sign that
                        # is subtracted;
                        # the term to the left of the minus sign is not necessarily subtracted, though it can be too.
                        if not pre_minus_match:
                            #  intermediate_terms[i] = minus_match.group()
                            pass

            split_at_add_terms = []
            for index in range_len(intermediate_terms):
                split_at_add_terms.extend(post_sub_split_at_add(intermediate_terms, index))

            for i in range_len(split_at_add_terms):
                split_at_add_terms[i] = "&" + split_at_add_terms[i]  # to mark the beginnings of each term; to mark separation between terms

            print("The parsed terms: ", end="")
            print(split_at_add_terms)

            return split_at_add_terms  # The final list of parsed terms, if the required conditions are satisfied.

    else:  # Executes if no subtractions signs are present in the user-entered expression.
        split_at_addition_sign = re.split(r"\s*\+\s*", expression)

        for i in range_len(split_at_addition_sign):
            split_at_addition_sign[i] = "&" + split_at_addition_sign[i]  # to mark the beginnings of each term; to mark separation between terms

        print("Terms after expression parsing: ", end="")
        print(split_at_addition_sign)

        return split_at_addition_sign  # The final list of parsed terms, if the required conditions are satisfied.
