# Announcements

- Quiz make-up policy: take on Canvas until the following Wednesday for partial
credit; email me if you need it re-opened.
- Resubmissions for HW1 due 2/13
- Grading HW2 without double penalties for things corrected in HW1
  - comment on your submission ASAP about who you worked with to avoid points lost
- Mid-term Friday: about 2x length of quizzes, will have entire class period
  - One 8.5"x11" single sided sheet of notes allowed (physical copy)
  - Paper preferred, computer OK
  - No other resources allowed (automatic zero and possibly fail the course).
  - Book in DAC reminder!
    - DAC exam will be taken on computer by default: remember to show your work!
    - No drawing of recursion trees is explicitly required, but may be one
      method you use to find a bound

# Last new content: Theorem for finding tight bounds

Imagine we have a recurrence of form:

$$
T(n) = a T(\frac{n}{b}) + f(n)
$$

with a base case $T(n) \in \Theta(1)$.

What are some examples?

- Merge sort: $T(n) = 2T(n/2) + n$
- Binary search: $T(n) = T(n/2)$
- Max sub-array: $T(n) = 2T(n/2) + \Theta(n)$

First, we define a *critical exponent* $c_{crit} = \log_b(a)$.

Three cases:

1. Work is dominated by subproblems.

   a. **Condition:** $f(n) = O(n^c)$ where $c < c_{crit}$.

   b. **Bound:** $T(n) = \Theta(n^{c_{crit}})$

2a.

   a. **Condition:** $f(n) = \Theta(n^{c_{crit}} \log^k(n)$ for $k > -1$.

   b. **Bound:** $T(n) = \Theta(n^{c_{crit}} \log^{k+1}(n))$

2b.

   a. **Condition:** $f(n) = \Theta(n^{c_{crit}} \log^k(n)$ for $k = -1$.

   b. **Bound:** $T(n) = \Theta(n^{c_{crit}} \log(\log(n)))$

2c.

   a. **Condition:** $f(n) = \Theta(n^{c_{crit}} \log^k(n)$ for $k < -1$.

   b. **Bound:** $T(n) = \Theta(n^{c_{crit}})$

3. Work to split/recombine dominates the subproblems.

   a. **Condition:** $f(n) = \Omega(n^{c_{crit}}$ where $c > c_{crit}$
   **and** $af(\frac{n}{b}) \leq k f(n)$ for $k < 1$ and sufficiently large $n$. Second
   condition is called the *regularity condition*.

   b. **Bound:** $T(n) = \Theta(f(n))$


