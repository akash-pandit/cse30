class EvalExpression:
    def evaluate(self, s: str) -> int:
        """Calculates the result of a standard infix notation string math expression using stacks with input bounds
        [0, 2^31-1] and floor division and returns the resulting integer."""

        """===== Convert s to list of terms stored as list "infix" =================================================="""
        s = s.replace(' ', '') + ';'  # remove any whitespace, add terminating character ;
        operators, nums, num = [], [], ''
        # init list of ops, list of nums, and a variable that holds concatenated digits that form a final number (num)
        for i in range(len(s)):
            if s[i] in ['+', '-', '*', '/', ';']:
                # semicolon added as an 'operator' as numbers are only added to the list in the presence of an operator
                operators.append(s[i])
                nums.append(num)
                num = ''  # reset num variable to start collecting the next number's digits
            else:
                num = num + s[i]  # concatenates num strings together until an operator is reached
                # (the input string is in infix format so all numbers must be separated by 1 operator)
        infix = []
        for i in range(len(nums)):  # stitch the nums and operators together in a final expression
            infix.append(nums[i])
            infix.append(operators[i])

        del infix[-1]  # remove terminating character (semicolon)
        """==== Convert infix list to postfix list stored as list "postfix" ========================================="""
        opstack, postfix = [], []
        precedence = {'/': 4, '*': 3, '+': 2, '-': 1}  # order of precedence of operators, high-low : first-last
        for i in infix:
            if i.isnumeric():  # nums are immediately added to postfix when ran across
                postfix.append(i)
            else:
                while (len(opstack) != 0) and (precedence[opstack[len(opstack) - 1]] >= precedence[i]):
                    # 'while opstack isn't empty and top of stack has equal or higher precedence:'
                    postfix.append(opstack.pop())
                opstack.append(i)  # the top op of opstack will be added to postfix THEN the next op is added to opstack

        while len(opstack) > 0:
            postfix.append(opstack.pop())  # any leftover operators get added (appended) on postfix

        """==== Actually calculate the result of the postfix expression ============================================="""
        def execute_operator_on_postfix(op: str) -> list:
            # create a nested func that given an operator, will run that operator for every occurrence in postfix
            oper = {'+': lambda x, y: x + y,  # the actual math, where an op is associated with a mathematical expr.
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x // y}  # / is floor division according to HW instructions
            for j in range(2, len(postfix)):  # an operator needs 2 values before it in postfix
                if postfix[j] == op: # checks if the value is an operator
                    postfix[j-2] = oper[op](int(postfix[j-2]), int(postfix[j-1]))  # AB+ -> op[+](A, B) -> result
                    # if so, reassigns first value (A) to the result of the operation with the previous 2 nums
                    del postfix[j-1], postfix[j-1]  # clears 2nd and 3rd values (op and B)
                    postfix.extend(['', ''])  # adds empty values so that list size remains constant for each iteration
            return postfix

        # run the operator execution based on order of precedence, division first, down all the way to subtraction
        execute_operator_on_postfix('/')
        execute_operator_on_postfix('*')
        execute_operator_on_postfix('+')
        execute_operator_on_postfix('-')
        # does not operate like in math, for the scope of this assignment / > * > + > -, not / or * > + or -
        # this assignment only deals with positive integers, its pos - pos not pos + neg like in math

        return postfix[0]


calc = EvalExpression()
# test cases given below
assert calc.evaluate('3+2*2') == 7
assert calc.evaluate(' 3/2 ') == 1
assert calc.evaluate(' 3+5 / 2 ') == 5
assert calc.evaluate(' 23 + 4 / 2 ') == 25
