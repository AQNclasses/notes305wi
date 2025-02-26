# Quicksort Review

(see slides/quicksort.py)

# Intuition of Randomized Quicksort Average Case


# Exact Expected Runtime

## Comparisons

**Lemma 1:** The running time of Quicksort on an $n$-element array is $O(n+X)$, where
$X$ is the number of element comparisons performed.

**Proof:** Each time partition is called, the selected pivot is never included
in any future calls to quicksort or partition. Thus, there will be at most $n$
calls to Partition over the entire execution.

Partition takes $O(1)$ time plus an amount of time proportional to the number of
iterations of the for loop. Each iteration performs one element comparison.
There are at most $n$ calls to Partition.

Thus, the total time for quicksort is $O(n+X)$.

**Lemma 2:** During the execution of Randomized-Quicksort on an array of $n$
distinct elements $z_1 < z_2 < \ldots, z_j$, an element $z_i$ is compared with
an element $z_j$, where $i<j$, if and only if one of them is chosen as a pivot
before any other element in the set $Z_{ij}$. No two elements are ever compared
twice.

**Proof:** Consider the case where it is the first time an element $x \in
Z_{ij}$ is chosen as a pivot. There are three cases to consider:

- If $x$ is neither $z_i$ nor $z_j$, then $z_i$ and $z_j$ are not compared at
any subsequent time, because they will be partitioned by $x$.
- If $x=z_i$, then Partition compares $z_i$ with every other item in $Z_{ij}$.
Similarly, if $x=z_j$, then Partition compares $z_j$ with every other item in
$Z_{ij}$. Thus, $z_i$ and $z_j$ are compared if and only if one of them is the
first to be chosen as a pivot out of $Z_{ij}$. Since
the pivot is removed from future comparisons, it is never compared again with
any other element, thus each pairwise comparison of elements only occurs at
most once.

**Lemma 3:** Consider an execution of Randomized-Quicksort on an array of $n$
distinct elements $z_1 < z_2 < \ldots < z_n$. Given two arbitrary elements $z_i$
and $z_j$ where $i<j$, the probability that they are compared is $2/(j-i+1)$.

**Proof:** Consider the tree of recursive calls made by Randomized-Quicksort,
and the set of elements provided as input to each call. Initially, the root set
contains all elements of $Z_{ij}$. These elements stay together (and are not
compared to each other) until Partition chooses some $x \in Z_{ij}$ as the
pivot. From that point on, the pivot $x$ appears in no subsequent input and is
not compared.

The first time that we choose a pivot $x \in Z_{ij}$, each element is equally
likely. Since $|Z_{ij}| = j-i+1$, the probability is $1/(j-i+1)$ that any given
element is chosen as the pivot. Thus, by Lemma 2, we have:

$$
\begin{align\*}
Pr(z_i \text{  is compared to  } z_j) = & Pr(z_i \text{or} z_j \text{first pivot}) \\
= & Pr(z_i \text{first pivot}) + Pr(z_j \text{first pivot}) \\
= & \frac{2}{j-i+1}
\end{align\*}
$$

where the second line follows from the first because the two events are mutually
exclusive.

**Theorem:** The expected running time of Randomized-Quicksort on $n$ distinct
elements is $O(n \lg{n})$.

**Proof:** Let the elements be $z_1 < z_2 < \ldots < z_n$. Define an indicator
variable $X_{ij} = [z_i \text{ is compared to } z_j\]$. From Lemma 2, each pair is
compared at most once, so we can express $X$ as

$$
X = \sum_{i=1}^{n-1} \sum_{j=i+1}^n X_{ij}
$$

By taking expectations of both sides, and by linearity of expectation, we
obtain:

$$
\begin{align\*}
E\[X\] = & E \large[ \sum_{i=1}^{n-1} \sum_{j=i+1}^n X_{ij} \large] \\
= & \sum_{i=1}^{n-1} \sum_{j=i+1}^n E\[ X_{ij} ] \\
= & \sum_{i=1}^{n-1} \sum_{j=i+1}^n Pr(z_i \text{compared to} z_j) \\
= & \sum_{i=1}^{n-1} \sum_{j=i+1}^n \frac{2}{j-i+1}
\end{align\*}
$$

Change of variables:

$$
\begin{align\*}
E\[X\] = & \sum_{i=1}^{n-1} \sum_{k=1}^{n-i} \frac{2}{k+1} \\
< & \sum_{i=1}^{n-1} \sum_{k=1}^{n} \frac{2}{k} \\
= & \sum_{i=1}^{n-1} O(\lg{n}) \\
= & O(n\lg{n})
\end{align\*}
$$
