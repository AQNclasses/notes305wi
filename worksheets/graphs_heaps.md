---
geometry: margin=1in
header-includes:
    - \usepackage{fancyhdr}
---

\pagestyle{fancy}
\fancyhead[CO]{CSCI 305 Winter 25}

1. There are n people at a party. Each person shakes hands with every other person. How many handshakes take place?

\vspace{6em}

2. Consider the graph with the following adjacency matrix.

\begin{table}[h]
\begin{tabular}{llllllll}
  & A & B  & C & D & E  & F & G  \\
A & 0 & 10 & 6 & 4 & 0  & 7 & 0  \\
B & 0 & 0  & 9 & 0 & 11 & 0 & 18 \\
C & 6 & 9  & 0 & 1 & 1  & 0 & 0  \\
D & 4 & 0  & 1 & 0 & 1  & 2 & 0  \\
E & 0 & 0  & 1 & 1 & 0  & 0 & 14 \\
F & 7 & 0  & 0 & 2 & 0  & 0 & 15 \\
G & 0 & 18 & 0 & 0 & 0  & 0 & 0 
\end{tabular}
\end{table}

a. Draw a picture of the graph represented by this adjacency matrix S without the weights.

\vspace{15em}

b. Is the graph directed or undirected? Explain.

\vspace{5em}

c. List the vertices in depth-first order beginning with Vertex A. When there is a choice, process the vertices and edges from left to right.

\newpage

3. A claim is made that a complete directed graph of n vertices has n(n-1) edges, while a complete undirected graph of n vertices has n(n-1)/2 edges. Is this claim true? If so outline a proof. If not, give a counter example.

\vspace{25em}

4. We have a max-heap where nodes are given IDs starting at 0 for the root node,
1 for the left child, and 2 for the right child. We increase node IDs as we move
from left to right across one level of the tree.

    Identify a pattern for moving from a node with label $j$ to its left child and
    right child. What labels would be found on the left and right children of node $j$?
