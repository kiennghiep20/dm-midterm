# Task 1: Logical Expressions and Truth Tables

## Theory

### Reverse Polish Notation (RPN)

Reverse Polish Notation (RPN), also known as Postfix notation, is a mathematical notation in which operators follow their operands. For example, the infix expression `P & Q` becomes `PQ&` in RPN. RPN avoids the need for parentheses and operator precedence rules during evaluation, making it suitable for computer evaluation using a stack.

**Evaluation Process:**
1. Scan the RPN expression from left to right.
2. If an operand (variable like P, Q) is encountered, push it onto a stack.
3. If an operator is encountered:
    * Pop the required number of operands from the stack (usually one for unary operators like `~`, two for binary operators like `&`, `|`, `>`).
    * Perform the operation.
    * Push the result back onto the stack.
4. After scanning the entire expression, the final result remains on the stack.

**Conversion from Infix to RPN (Shunting-yard algorithm):**
The `Infix2Postfix` function implements a common algorithm:
1. Initialize an empty output queue (for the Postfix string) and an empty operator stack.
2. Define operator precedence (`~` highest, then `&`, `|`, `>`, `=`).
3. Scan the infix expression from left to right:
    * **Operand:** Add it directly to the output queue.
    * **Operator:**
        * While the operator stack is not empty, the top element is not `(` and has higher or equal precedence than the current operator, pop operators from the stack to the output queue.
        * Push the current operator onto the stack.
    * **Left Parenthesis `(`:** Push it onto the operator stack.
    * **Right Parenthesis `)`:** Pop operators from the stack to the output queue until a `(` is encountered. Discard both parentheses.
4. After scanning, pop any remaining operators from the stack to the output queue.

### Basic Logic for Truth Tables

*   **`~` (NOT):** Negation. `~P` is true if `P` is false, and false if `P` is true.
*   **`&` (AND):** Conjunction. `P & Q` is true only if both `P` and `Q` are true.
*   **`|` (OR):** Disjunction. `P | Q` is true if at least one of `P` or `Q` is true.
*   **`>` (IMPLIES):** Implication. `P > Q` is false only if `P` is true and `Q` is false. It's equivalent to `~P | Q`.
*   **`=` (EQUIVALENT):** Biconditional. `P = Q` is true if `P` and `Q` have the same truth value.

The `Postfix2TruthTable` function calculates the truth value of the expression for every possible combination of truth values (True/False) assigned to the propositional variables (P, Q, R, etc.).

## Program Explanation with Test Cases

The program uses two main functions: `Infix2Postfix` to convert the input expression to RPN, and `Postfix2TruthTable` to generate and print the truth table based on the RPN expression.

### Test Case 1: `R|(P&Q)`

**Step 1: Infix to Postfix Conversion (`Infix2Postfix("R|(P&Q)")`)**

1.  **Scan `R`:** Operand. Postfix: `R`. Stack: `[]`.
2.  **Scan `|`:** Operator. Stack is empty. Push `|`. Postfix: `R`. Stack: `[|]`.
3.  **Scan `(`:** Push `(`. Postfix: `R`. Stack: `[|, (]`.
4.  **Scan `P`:** Operand. Postfix: `RP`. Stack: `[|, (]`.
5.  **Scan `&`:** Operator. Top is `(`. Push `&`. Postfix: `RP`. Stack: `[|, (, &]`.
6.  **Scan `Q`:** Operand. Postfix: `RPQ`. Stack: `[|, (, &]`.
7.  **Scan `)`:** Pop `&` to Postfix. Pop `(`. Postfix: `RPQ&`. Stack: `[|]`.
8.  **End of Infix:** Pop remaining `|` to Postfix.
9.  **Final Postfix:** `RPQ&|`

**Step 2: Truth Table Generation (`Postfix2TruthTable("RPQ&|")`)**

1.  **Identify Variables:** The unique variables are `P`, `Q`, `R`.
2.  **Generate Truth Combinations:** Create all 2^3 = 8 combinations for (P, Q, R).
    *   (T, T, T), (T, T, F), (T, F, T), (T, F, F), (F, T, T), (F, T, F), (F, F, T), (F, F, F)
3.  **Print Header:** `P||Q||R||R|(P&Q)`
4.  **Evaluate for each combination (Example: P=T, Q=F, R=T):**
    *   Use the Postfix `RPQ&|`. Evaluation stack starts empty.
    *   **Scan `R`:** Push `T` (value of R). Stack: `[T]`.
    *   **Scan `P`:** Push `T` (value of P). Stack: `[T, T]`.
    *   **Scan `Q`:** Push `F` (value of Q). Stack: `[T, T, F]`.
    *   **Scan `&`:** Pop `F`, Pop `T`. Calculate `T & F = F`. Push `F`. Stack: `[T, F]`.
    *   **Scan `|`:** Pop `F`, Pop `T`. Calculate `T | F = T`. Push `T`. Stack: `[T]`.
    *   **Final Result for (T, F, T):** `T`.
5.  **Print Row:** Print the truth values for P, Q, R and the calculated result for this combination.
6.  **Repeat:** Repeat step 4 and 5 for all 8 combinations.

### Test Case 2: `~P|(Q&R)>R`

**Step 1: Infix to Postfix Conversion (`Infix2Postfix("~P|(Q&R)>R")`)**

*Operator Precedence: `~` (5), `&` (4), `|` (3), `>` (2)*

1.  **Scan `~`:** Operator. Push `~`. Postfix: ``. Stack: `[~]`.
2.  **Scan `P`:** Operand. Postfix: `P`. Stack: `[~]`.
3.  **Scan `|`:** Operator. Precedence(`|`) < Precedence(`~`). Pop `~`. Push `|`. Postfix: `P~`. Stack: `[|]`.
4.  **Scan `(`:** Push `(`. Postfix: `P~`. Stack: `[|, (]`.
5.  **Scan `Q`:** Operand. Postfix: `P~Q`. Stack: `[|, (]`.
6.  **Scan `&`:** Operator. Top is `(`. Push `&`. Postfix: `P~Q`. Stack: `[|, (, &]`.
7.  **Scan `R`:** Operand. Postfix: `P~QR`. Stack: `[|, (, &]`.
8.  **Scan `)`:** Pop `&` to Postfix. Pop `(`. Postfix: `P~QR&`. Stack: `[|]`.
9.  **Scan `>`:** Operator. Precedence(`>`) < Precedence(`|`). Pop `|`. Push `>`. Postfix: `P~QR&|`. Stack: `[>]`.
10. **Scan `R`:** Operand. Postfix: `P~QR&|R`. Stack: `[>]`.
11. **End of Infix:** Pop remaining `>`.
12. **Final Postfix:** `P~QR&|R>`

**Step 2: Truth Table Generation (`Postfix2TruthTable("P~QR&|R>")`)**

1.  **Identify Variables:** `P`, `Q`, `R`.
2.  **Generate Truth Combinations:** 8 combinations for (P, Q, R).
3.  **Print Header:** `P||Q||R||(~P|(Q&R))>R`
4.  **Evaluate for each combination (Example: P=F, Q=T, R=F):**
    *   Use Postfix `P~QR&|R>`. Evaluation stack starts empty.
    *   **Scan `P`:** Push `F` (value of P). Stack: `[F]`.
    *   **Scan `~`:** Pop `F`. Calculate `~F = T`. Push `T`. Stack: `[T]`.
    *   **Scan `Q`:** Push `T` (value of Q). Stack: `[T, T]`.
    *   **Scan `R`:** Push `F` (value of R). Stack: `[T, T, F]`.
    *   **Scan `&`:** Pop `F`, Pop `T`. Calculate `T & F = F`. Push `F`. Stack: `[T, F]`.
    *   **Scan `|`:** Pop `F`, Pop `T`. Calculate `T | F = T`. Push `T`. Stack: `[T]`.
    *   **Scan `R`:** Push `F` (value of R). Stack: `[T, F]`.
    *   **Scan `>`:** Pop `F` (second operand), Pop `T` (first operand). Calculate `T > F = F`. Push `F`. Stack: `[F]`.
    *   **Final Result for (F, T, F):** `F`.
5.  **Print Row:** Print the truth values for P, Q, R and the calculated result.
6.  **Repeat:** Repeat step 4 and 5 for all 8 combinations.

