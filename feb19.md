# Announcements

# Greedy Algorithms

- Scheduling Classes problem
- Recursive solution
- O($n^3$) time

```python
def GreedySchedule(S, F):
  sort arrays by ascending end time
  count = 1
  X[count] = 1
  for i=2 to n:
    if S[i] > F[X[count]]:
      count += 1
      X[count] = i
  return X
```

Finds maximum number of non-overlapping classes.

**Lemma:** At least one maximal conflict-free schedule includes the class that
finishes first.

**Proof:** Let $f$ be the class that finishes first. Suppose we have a maximal
conflict-free schedule $X$ that does not include $f$. Let $g$ be the the first
class in $X$ to finish. Since $f$ finishes before $g$, $f$ cannot conflict with
any class in the set $X$ without $g$. X with $f$ instead of $g$ is the same
size, so it is also a maximal solution.

**Theorem:** The greedy schedule is an optimal schedule.

**Proof:** Let $(g_1, g_2, g_{j-1}, \ldots , c_j, c_{j+1}, \ldots, c_m)$ by a maximal
conflict-free schedule, where classes $g_i$ are chosen by a greedy algorithm,
and $c_i$ chosen otherwise.

By construction, the $j$th greedy choice $g_j$ does not conflict with earlier
classes, and neither does $c_j$ since our schedule is conflict-free.

Additionally, $g_j$ has the earliest finish time among all classes that don't
conflict with earlier classes; it finishes before $c_j$. Thus, the following
schedule is also conflict-free:

$(g_1, g_2, g_{j-1}, \ldots , g_j, c_{j+1}, \ldots, c_m)$

We may repeat the same argument for all remaining classes that are not chosen
by the greedy algorithm.
