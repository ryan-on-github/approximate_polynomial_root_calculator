
  # entire while-loop cmd-line prompt and input-parser

import re


try:  # Command-Line prompt and string-parser to interpret user-entered expressions
    print("Hello, and welcome to the Polynomial Approximate Root Finder."
            "\n You will be asked to enter the following: "
            "\n     A polynomial expression in standard-form, such like: 'ax^(n) + bx^(n-1) + cx^(n-2) + ... + (n-1)x^2 + nx';"
            "\n     the lower-bound of an interval you believe the root is in; a simple integer;"
            "\n     the upper-bound of that interval you believe the root is in; again, simply an integer;"
            "\n     the tolerable amount of error, or, the largest distance the approximate root can be from the true root; another integer"
            "\n     and finally, since this is an iteration-based search function, a maximum number of iterations to be computed, for to avoid infinite loops; another integer."
            "\n"
            "\nIf you'd like to, you can end this session by entering the word 'stop'.")


    while True:  # while-loop to enable cmd-line usage
        inputted_expression = input("Please, enter a polynomial expression >>>")  # cmd-line prompt for the polynomial expression

        list_of_terms = re.split(r"""\+\b  # a simple 'plus' sign with no space-characters on either of its sides
                                     |\s\+\s  # a 'plus' sign with a space-character on both of its sides
                                     |(?<!\()-  # a 'minus' sign, not preceded by a left-parenthesis, with no space-characters on either of its sides
                                     |(?<!\()\s-\s  # a 'minus' sign, not preceded by a left parenthesis, with space-characters on both of its sides""",
                                 inputted_expression, flags=re.VERBOSE)  # parsing of the user's input for to separate terms

        while True:
            for i in range(len(list_of_terms)):
                print(list_of_terms[i-1])
            user_confirm = input("Please confirm that these are the terms you wish to have entered; 'yes' or 'no' >>>")
            if user_confirm == "yes":
                break
            elif user_confirm == "no":
                inputted_expression = input("Please, enter another polynomial expression >>>")
                break
            else:
                continue

        inputted_lower_bound = input("Now, enter the lower-bound of your interval >>>")  # cmd-line prompt for the lower bound
        inputted_upper_bound = input("Alright, now, enter the upper-bound of your interval >>>")  # cmd-line prompt for the upper bound
        inputted_tol = input("Please, enter the tolerable amount of error >>>")  # cmd-line prompt for the error tolerance
        inputted_iter_max = input("And lastly, enter the iteration limit >>>")  # cmd-line prompt for the iteration maximum

        user_input = input("The approximate root is being computed... >>>")

        if re.match(r"\s*stop\b", user_input, re.IGNORECASE):  # user-activated while-loop break
            raise KeyboardInterrupt

except KeyboardInterrupt:
    print("The session has ended.")

finally:
    print("Thank you")
