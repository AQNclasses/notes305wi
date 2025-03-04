# Announcements

- Quiz 2 grades posted, can return Quiz 1 and Quiz 2 after class today
- Quiz 3 will be back tomorrow
- HW1 and HW2 solutions are posted

# Review

## Requests for Topics?

## How to write a proof

1. Write down statement to prove (translate from word problem to logical
statement if needed).
2. Write down type of proof (direct proof, proof by contradiction, induction).
3. Write down what that type of proof needs
   a. direct proof: sequence of logical implications, starting from assumptions
      and definitions. State action in words if not very clear from math.
   b. proof by contradiction: state negation of statement you are trying to
      prove. then perform sequence of inferences until you reach a logical
      contradiction.
   c. induction: define inductive hypothesis $P(n)$. (function in terms of $n$). Prove
      base case(s). Prove $P(n)$ assuming $P(1)$ through $P(n-1)$ are true.
4. Optional: "QED", $\qed$

## How to find and solve recurrences

- *Recursive algorithm:* An algorithm that calls itself.
- *Recurrence relation:* A mathematical equation defining a sequence, where the
  $n$th term in the sequence is equal to some combination of previous terms.
  - not a *function*, because a function maps each element of a set $X$ to
    exactly one element of a set $Y$
- We use recurrences to describe the runtime of recursive algorithms, or to help
  us create a recursive algorithm.

### How to find

- Counting method, but use T(...) every time our algorithm references itself
- Subtleties in defining recursive calls can have large effect on estimated
runtime (Quiz 2 example)

### How to solve

- Review tricks in [Runtime and Asymptotics](topics/runtime_and_asymptotic.md).
- Review recursion trees

Examples:

$$
T(n) = 4T(n/2) + 1000
$$

$$
T(n) = 2T(n/2) + n^3
$$

$$
T(n) = 3T(n) + n^2
$$

## Amortization review

- From [here in the notes](topics/amortized.md).
