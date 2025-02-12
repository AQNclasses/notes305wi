---
geometry: margin=1in
---

\begin{center}
{\Large{Master Theorem \\ CSCI 305}}
\end{center}

\vspace{1em}

For recurrences in the form $T(n) = a T(\frac{n}{b}) + f(n)$, with a base case $T(n) \in \Theta(1)$.

Three cases:

1 . Work is dominated by subproblems.

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

3 . Work to split/recombine dominates the subproblems.

   a. **Condition:** $f(n) = \Omega(n^c)$ where $c > c_{crit}$
   **and** $af(\frac{n}{b}) \leq k f(n)$ for $k < 1$ and sufficiently large $n$. Second
   condition is called the *regularity condition*.

   b. **Bound:** $T(n) = \Theta(f(n))$

Examples:

1. $T(n) = 8T(\frac{n}{2}) + 1000n^2$

\vspace{8em}

2. $T(n) = 2T(n/2) + 10n$

\vspace{8em}

3. $T(n) = 2T(n/2) + n^2$
