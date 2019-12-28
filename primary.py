
  # a command-line program utilizing bisection-search to find a root of a polynomial function inputted by the user

import re
import math
import expression_parsing_func
import term_parsing_module_v1


def approx_root_finder(poly_expr, interval_lowerb, interval_upperb, error_tol, iter_max):
    """
    A function utilizing bisection-search to find a root of a polynomial.

    poly_expr is the polynomial being analyzed;
    interval_lowerb is the interval's lower endpoint;
    interval_upperb is the interval's upper endpoint;
    error_tol is the error tolerance of the approximation;
    iter_max is the time-limit creator of the program.

    interval_lowerb and interval_upperb must be floating-point type, or be converted to floating-point type.
    error_tol and iter_max must be integer type
    """

    interval_lowerb = float(interval_lowerb)  # a must be floating-point type
    interval_upperb = float(interval_upperb)  # b must be floating-point type

    n = 1
    while n <= iter_max:  # iteration limit to prevent infinite iteration
        mid = (interval_lowerb + interval_upperb) / 2  # mid-point
        max_error = (abs(interval_upperb - interval_lowerb))/2  # approximate maximum error
        if mid == 0 or max_error <= error_tol:  # either the root is found or the maximum error is tolerable
            print("Sufficient root found:", end = " ")
            print(mid)  # The value is printed to the display
            return mid  # The value is returned for further use

        if poly_expr(mid) * poly_expr(interval_lowerb) >= 0:
            interval_lowerb = mid
        else:
            interval_upperb = mid

        n = n + 1

    if n > iter_max:  # the condition of the iteration number reaching its maximum
        print("It appears that either no root exists within the given interval "
              "or the iteration limit was set too low and a root could not be found within the given time constraints."
              "\n"
              "\nIf you'd like to try again, please end this session and restart with a different time limit or another"
              "interval.")


try:  # Command-Line prompt and string-parser to interpret user-entered expressions
    print("Hello, and welcome to the Polynomial Root Finder."
            "\nYou will be asked to enter a polynomial expression, and then an interval you believe a root of the function is within," 
            "and this program will report an approximation of that root to you, if it exists in the given interval."
            "\n"
            "\nIf you'd like to, you can end this session by entering the word 'stop'.")

    while True:
        inputted_expression = input("Please, enter a polynomial expression: ")  # cmd-line prompt for the polynomial expression
        inputted_interval = input("Now, please, enter two x-values you believe the root exists between: ")  # cmd-line prompt for the closed-interval
        user_input = input("The approximate root is being computed...: ")

        if user_input == "stop":  # user-activated while-loop break
            raise KeyboardInterrupt

except KeyboardInterrupt:
    print("The session has ended.")
