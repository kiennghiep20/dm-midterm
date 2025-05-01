# Project Explanation

## Task 1: Truth Table

1.  **Infix to Postfix Conversion:** It includes a function `Infix2Postfix` that converts logical expressions written in standard infix notation (e.g., `(P | ~Q) > R`) into postfix notation (Reverse Polish Notation, e.g., `PQ~|R>`). This conversion uses a stack-based algorithm considering operator precedence (`~`, `&`, `|`, `>`, `=`).
2.  **Truth Table Generation:** It includes a function `Postfix2TruthTable` that takes a postfix expression, identifies the unique propositional variables (like P, Q, R), and generates a complete truth table. The table shows all possible combinations of truth values (True/False) for the variables and the resulting truth value of the entire logical expression for each combination. It also uses an auxiliary function `postfix_to_infix` to display the original expression in the table header.

### Detailed Mechanism for Task 1

#### `Infix2Postfix(Infix)` Function:

*   **Purpose:** Converts standard infix logical expressions to postfix (RPN) for easier stack-based evaluation.
*   **Algorithm (Adapted Shunting-Yard):**
    *   **Initialization:**
        *   `operators`: Dictionary defining operator precedence (`~`:5, `&`:4, `|`:3, `>`:2, `=`:1).
        *   `stack`: List used as a temporary store for operators and parentheses.
        *   `Postfix`: String to build the output postfix expression.
        *   `InfixDeque`: Input string converted to a `deque` for efficient left-to-right processing.
    *   **Processing Loop (Character by Character):**
        *   **Operand (Letter):** Append directly to `Postfix`.
        *   **Operator:**
            *   If the stack is empty or the current operator has higher precedence than the stack top, push the current operator onto the `stack`.
            *   Otherwise, pop operators from the `stack` to `Postfix` as long as they have higher or equal precedence than the current operator (and are not `(`). Then, push the current operator onto the `stack`.
        *   **Opening Parenthesis `(`:** Push onto the `stack`.
        *   **Closing Parenthesis `)`:** Pop operators from `stack` to `Postfix` until `(` is found. Discard both parentheses.
    *   **Finalization:** Pop any remaining operators from `stack` to `Postfix`.
    *   **Output:** The final `Postfix` string.

#### `Postfix2TruthTable(Postfix)` Function:

*   **Purpose:** Generates a truth table for a given postfix logical expression which is obtained using the `Infix2Postfix` funciton.
*   **Steps:**
    *   **Variable Identification:** Finds unique variables (A-Z) using regex `findall("[A-Z]", Postfix)`.
    *   **Header Generation:**
        *   Creates the table header with variable names and the original infix expression (reconstructed using `postfix_to_infix`).
        *   `postfix_to_infix(Postfix)`: Helper function to convert postfix back to infix with necessary parentheses for display. Uses a stack to rebuild the expression.
    *   **Truth Value Combinations:** Generates all 2<sup>n</sup> possible True/False combinations for `n` variables using `itertools.product`.
    *   **Table Row Generation (Looping through combinations):**
        *   **Variable Mapping:** Creates a dictionary mapping variables to their current truth values for the row.
        *   **Postfix Evaluation (using a stack):**
            *   Scan the `Postfix` expression.
            *   **Operand:** Push its corresponding truth value (from the dictionary) onto the evaluation stack.
            *   **Operator `~`:** Pop one value, apply `not`, push the result.
            *   **Binary Operators (`&`, `|`, `>`, `=`):** Pop two values, apply the corresponding logical operation (`and`, `or`, `not op1 or op2`, `==`), push the result.
        *   **Printing Row:** Print the variable truth values and the final calculated result for the expression in that row.
    *   **Output:** Prints the formatted truth table to the console.

## Task 2: Quantified Reasoning over Real-World Data Using Predicate Logic

1.  **Data Loading:** It reads the CSV file and stores student records, creating a lookup structure for efficient access by StudentID or StudentName.
2.  **Predicate Functions:** It defines several functions that act as predicates to check conditions for a given student:
    *   `is_passing`: Checks if a student has scores >= 5 in all subjects.
    *   `is_high_math`: Checks if a student's Math score is >= 9.
    *   `is_struggling`: Checks if a student's Math and CS scores are both < 6.
    *   `improved_in_cs`: Checks if a student's CS score is greater than their Math score.
3.  **Quantified Statements:** It defines functions to evaluate quantified statements over the entire set of student records:
    *   **Universal Quantification (∀):** e.g., `all_passed()` checks if *all* students passed all subjects.
    *   **Existential Quantification (∃):** e.g., `any_math_gt9()` checks if *there exists* at least one student with a Math score > 9.
    *   **Combined/Nested Statements:** e.g., checking if all students with Math < 6 have at least one other score > 6.
4.  **Negation of Quantified Statements:** For each quantified statement, a corresponding function calculates its logical negation (e.g., the negation of "all passed" is "at least one student did not pass").

## Conclusion
*   **Task 1:** A robust truth table generator was developed. It parses logical expressions, identifies variables, evaluates the expression for all possible truth value combinations using postfix notation, and presents the results in a clear, formatted table.
*   **Task 2:** Functionality for analyzing and negating quantified statements was created. This involved processing statements to determine their truth values and deriving their logical negations, demonstrating an understanding of predicate logic principles.