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