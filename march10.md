# Announcements

- HW 5 out, single problem due Sunday
    - Extra credit problems will be out by tonight
- Most grades should be updated by tonight

# Analyzing Dijkstra's Algorithm

```python
# input:
# - V: list of nodes
# - E: list of edges
# start, goal: start and goal nodes
# cost(v,w): cost of edge between nodes v and w
graph = AdjacencyList(V, E)
dists = {v:inf for v in V}
dists[start] = 0
unvisited = MinPriorityQueue(V, dists)
while unvisited is not empty:
  current = unvisited.pop_min() # pop node with minimum distance
  if current == goal:
    return
  for n in current.neighbors:
    dist_from_here = current.dist + cost(current, n)
    if n.dist > dist_from_here:
      n.dist = dist_from_here
      unvisited.decrease_priority(n, n.dist)
  unvisited.update()
return
```

## remove root of heap

The `pop_min` routine removes the root node from a min-heap.

The method for doing this is to replace the root node with the "last" element at
the bottom of the heap, then swapping the "new" root node with its smallest
child until it's in the correct location.

This gives $O(log(M))$ time, where $M$ is the number of elements in the priority
queue.

## decrease priority of element in heap

Similarly, if we need to update the priority of a certain node, we first need to
find the node under consideration. This is O(1) if we have a dictionary associating
nodes in our graph with node IDs in the priority queue, O(M) otherwise.

Once we have found the element, we call `Heapify` and re-order the priority
queue in $O(log M)$ time, and update our secondary data structure if necessary.

## worst-case complexity in terms of V and E

Originally, all nodes are in the priority queue to start. Each node must be
processed in the while loop, and the complexity of operations inside the while
loop is $O((# of neighbors) \log M) < O((# of neighbors)\dot \log |V|)$.

Thus, the total complexity of the algorithm is bounded by

$$
\begin(align\*}
& O(N \dot (# of neighbors per node ) \dot \log |V|) \\
\leq & O(|E| \dot \log |V|) \\
\end{align\*}
$$
