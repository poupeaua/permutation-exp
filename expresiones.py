"""
    Program to study the expressions in EXP of the following inductive
    contruction given a vocabulary V.
        - Base: if a in V => a in EXP
        - Induction: if (a,b) in EXP => (a*b) in EXP, (a+b) in EXP
            and (a==b) in EXP

    [*, (, ), =, +] is the list of symbol
"""


VOCABULARY = ["a", "b", "1", "2"]
SYMBOLS = ["*", "(", ")", "=", "+"]
VOCAB_SIZE = len(VOCABULARY)


def cantidad(n):
    """
        Argument:
            n (int) : index number

        Returns:
            a_n (int) : the number of different expressions of size n
    """
    if n == 0 or n == 2 or n == 3 or n == 4:
        return 0
    elif n == 1:
        return VOCAB_SIZE
    else:
        result = 0
        for i in range(0, n-VOCAB_SIZE):
            result += (2*cantidad(i+1) + cantidad(i))*cantidad(n-VOCAB_SIZE-i)
        return result



def getSepIndex(string):
    """
        Argument:
            string (str) : string that defines an expression

        Returns:
            idx (int) : index of the separation between two substrings
    """
    if string[1] == "(":
        count_parenthesis = 1
        idx = 2
        while count_parenthesis != 0:
            if string[idx] == "(":
                count_parenthesis += 1
            elif string[idx] == ")":
                count_parenthesis -= 1
            idx += 1
    else:
        idx = 2

    return idx



def getSepExp(string):
    """
        Argument:
            string (str) : string that defines a expression

        Returns:
            substring1 (str) : left substring
            substring2 (str) : right substring
    """
    # get the substring separation index
    # the while MUST stop since the nb of right / left parenthesis is the same
    idx = getSepIndex(string=string)

    # get the substrings
    substring1 = string[1:idx]
    if string[idx] == "*" or string[idx] == "+":
        substring2 = string[idx+1:-1]
    elif string[idx] == "=":
        substring2 = string[idx+2:-1]
        if string[idx+1] != "=":
            # case one = but not ==
            substring2 = "X"
    else:
        # it is not in the vocabulary -> putting something that will return False
        substring2 = "X"

    return substring1, substring2



def esExp(string):
    """
        Argument:
            string (str) : string that defines an expression

        Returns:
            is_exp (bool) : true if string in EXP, false if not.
    """
    if len(string) <= 4:
        # consider the case empty string and of size 2, 3 and 4 impossible
        if string in VOCABULARY:
            return True
        else:
            return False
    else:
        nb_right_parenthesis = len([0 for element in string if element == "("])
        nb_left_parenthesis = len([0 for element in string if element == ")"])
        if nb_right_parenthesis != nb_left_parenthesis:
            # easy case when the number of right / left parenthesis is not equal
            return False
        else:
            # the nb of right / left parenthesis is the same
            substring1, substring2 = getSepExp(string=string)
            return esExp(substring1) and esExp(substring2)



def main(string_input):
    """
        Argument:
            string_input (str) : expression

        Displays:
            a (int) : 1 if string_input in EXP, 0 if not
            b (int) : result of a_{len(string_input)}
    """
    # turn the boolean into int
    a = int(esExp(string=string_input))
    b = cantidad(n=len(string_input))
    print(str(a)+" "+str(b))


if __name__ == "__main__":
    string_input = input()
    main(string_input)
