from collections import deque
def Infix2Postfix(Infix):
    operators = {'~': 5, '&': 4, '|': 3, '>': 2, '=': 1} # Operators' precedence
    stack = []
    Postfix = ''
    InfixDeque = deque(Infix)
    while InfixDeque:
        char = InfixDeque.popleft() # Scan infix expression from left to right
        if char.isalpha():
            Postfix += char
        elif char in operators:
            if not stack or operators.get(char) > operators.get(stack[-1], 0): # get 0 if the last element is (
                stack.append(char)
            else:
                while stack and stack[-1] != '(':
                    if operators.get(stack[-1], 6) > operators.get(char): # get 6 if the last element is )
                        Postfix += stack.pop()
                    else:
                        stack.append(char)
                        break
                else:
                    stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            char = stack.pop()
            while stack and char != '(':
                Postfix += char
                char = stack.pop()
        else:
            # Invalid character encountered
            return None
    while stack:
        Postfix += stack.pop()
    return Postfix


from re import findall
from itertools import product

def postfix_to_infix(Postfix):
    stack = []
    PostfixDeque = deque(Postfix)
    while PostfixDeque:
        char = PostfixDeque.popleft()
        if char.isalpha():
            stack.append(char)
        elif char == '~':
            char = stack.pop()
            stack.append(f'~{char}')
        else:
            second = stack.pop()
            first = stack.pop()
            if PostfixDeque:
                stack.append(f'({first}{char}{second})')
            else: # For last operator
                stack.append(f'{first}{char}{second}')
    return stack[0]


def Postfix2TruthTable(Postfix):
    unique_propositional_variables = sorted(set(findall("[A-Z]", Postfix)))
    header_row = '||'.join(unique_propositional_variables) + '||' + postfix_to_infix(Postfix)
    num_prepositions = len(unique_propositional_variables)
    prespositions = product([True, False], repeat=num_prepositions)



    print(header_row)
    print('-'*len(header_row))
    for presposition in prespositions:
        dictionary = {}
        for i, var in enumerate(unique_propositional_variables):
            dictionary[var] = presposition[i] # Dictionary for corresponding key propositional variable and value truth value for each case

        # Evaluate each case's expression
        stack = []
        PostfixDeque = deque(Postfix)
        while PostfixDeque:
            char = PostfixDeque.popleft() # Scan the expression from left to right
            if char.isalpha():
                stack.append(dictionary.get(char))
            elif char == '~': # When char is an operator not
                stack.append(not dictionary.get(char))
            else: # When char is the other operator
                second_operand = stack.pop()
                first_operand = stack.pop()
                if char == '&':
                    stack.append(first_operand and second_operand)
                elif char == '|':
                    stack.append(first_operand or second_operand)
                elif char == '>':
                    stack.append(not first_operand or second_operand)
                elif char == '=':
                    stack.append(first_operand == second_operand)
                else: # Invalid operator encountered
                    return None
        for var in presposition:
            print(f"{var:<1}||", end="")
        print(f"{stack[0]:<1}")

# For explanation
# Postfix2TruthTable(Infix2Postfix("R|(P&Q)"))
# print()
# Postfix2TruthTable(Infix2Postfix("~P|(Q&R)>R"))

# For experimental results
experimental_expressions = ['R|(P&Q)', '~P|(Q&R)>R', 'P|(R&Q)', '(P>Q)&(Q>R)', '(P|~Q)>~P=(P|(~Q))>~P']
for e in experimental_expressions:
    Postfix2TruthTable(Infix2Postfix(e))
    print()