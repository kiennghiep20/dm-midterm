from collections import deque
# Task 1
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

def to_python_operation(first, second, operator):
    if operator == '~':
        return
    
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

# Task 2
import csv

student_lookup = {} # Create an efficient lookup to quickly find student based on whether the input is id or name for quantified statement
with open('dataset.csv', 'r') as file:
    dataset = csv.DictReader(file)
    student_records = []
    for record in dataset:
        # Convert score from string to int for consistent checking
        record['Math'] = int(record.get('Math', 0)) # Default to 0 for safety
        record['CS'] = int(record.get('CS', 0))
        record['Eng'] = int(record.get('Eng', 0))
        student_records.append(record) # Normal list of student information for negated quatified statements since we have to check all students in the dataset
        # Assuming student refers to both id and name
        student_lookup[record['StudentID']] = record # Store student information based on id
        student_lookup[record['StudentName']] = record # Store student information based on name

num_students = int(len(student_lookup) / 2) # Have to divide by 2 because we stored both id and name and convert it to int for range() function usage

def is_passing(student, student_lookup):
    return all(score >= 5 for score in [student_lookup.get(student).get('Math'), student_lookup.get(student).get('CS'), student_lookup.get(student).get('Eng')])
        
def is_high_math(student, student_lookup):
    return student_lookup.get(student).get('Math') >= 9
        
def is_struggling(student, student_lookup):
    return all(score < 6 for score in [student_lookup.get(student).get('Math'), student_lookup.get(student).get('CS')])
        
def improved_in_cs(student, student_lookup):
    return student_lookup.get(student).get('CS') > student_lookup.get(student).get('Math')

# Six quantified statements needing to negated later
# Universal quantifications
def all_passed():
    return all(score >= 5 for student in student_records for score in [student.get('Math'), student.get('CS'), student.get('Eng')])

def all_math_gt3():
    return all(student.get('Math') for student in student_records)

# Existential quantifications
def any_math_gt9(): # Basically ten lol
    return any(student.get('Math') > 9 for student in student_records)
        
def any_cs_gt_math():
    return any(student.get('CS') > student.get('Math') for student in student_records)

# Combined/nested statements
def all_has_above6():
    return all(any(score > 6 for score in [student.get('Math'), student.get('CS'), student.get('Eng')]) for student in student_records)

def all_math_below6_has_other_above6():
    return all(any(score > 6 for score in [student.get('CS'), student.get('Eng')]) for student in student_records if student.get('Math') < 6)

# Negate the statments
# At least one student did not pass at least one subject
def negated_all_passed():
    return any(score >= 5 for student in student_records for score in [student.get('Math'), student.get('CS'), student.get('Eng')])

# At least one student does not have a math score higher than 3.
def negated_all_math_gt3():
    return any(not student.get('Math') > 3 for student in student_records)

# All students have a math score greater than 9
def negated_any_math_gt9():
    return all(not student.get('Math') > 9 for student in student_records)

# All students did not improve in CS over Math
def negated_any_cs_gt_math():
    return all(not student.get('CS') > student.get('Math') for student in student_records)

def negated_all_has_above6():
    return all(any(score > 6 for score in [student.get('Math'), student.get('CS'), student.get('Eng')]) for student in student_records)

# There exists a student having all subject scores not above 6
def negated_all_has_above6():
    return any(all(not score > 6 for score in [student.get('Math'), student.get('CS'), student.get('Eng')]) for student in student_records)

# There exists a student whose math score is below 6 and all other scores are not above 6 (Negation of implication)
def negated_all_math_below6_has_other_above6():
    return any(all(not score > 6 for score in [student.get('CS'), student.get('Eng')]) for student in student_records if student.get('Math') < 6)

# print(is_passing('Charlie Brown', student_lookup))
# print(is_passing('3', student_lookup))
# print(all_passed())
# print(all_math_gt3())
# print(any_math_gt9())
# print(any_cs_gt_math())
# print(all_has_above6())
# print(all_math_below6_has_other_above6())
# print(negated_all_passed())
# print(negated_all_math_gt3())
# print(negated_any_math_gt9())
# print(negated_any_cs_gt_math())
# print(negated_all_has_above6())
# print(negated_all_math_below6_has_other_above6())