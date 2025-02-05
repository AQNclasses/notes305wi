
# Divide and Conquer

A general strategy for algorithm design.

## Maximum subarray problem

Suppose we are given a bunch of stock data, and we want to find the maximum gain
possible each day to use as training data for our day-trading neural network
(buy and sell only, no margin).

So given an array $A[1..n]$ of prices over one day, we want to find the time
(index) of when we should buy and sell our stock to maximize profit. Assume
we're only allowed to do one buy and one sell per day, in that order.

Just finding the max and min won't work, as we need to buy before we can sell.

### Naive strategy

Try all pairs of (buy, sell) times, where buy must be before sell.

What is runtime of this strategy?

(worksheet - write line by line in the code)

Ends up being $O(n^2)$: think of the table that would need to be filled out to
store all possible values.

### Divide and Conquer

Instead of raw prices, let's consider the daily change in price, and store these
values in a new array $B$. Now, our problem is to find the subarray that
maximizes the sum of the numbers in the subarray.

(Check how to transform solutions)

If we divide this array in two, we have three possible cases:

1. max subarray is in first half
2. max subarray is in second half
3. max subarray spans the two halves

In the first two cases, the recursive solution should be clear. But what about
the third?

To maximize the sum of the two spanning sub-arrays, we must maximize the sum of
each part.

Can write helper function to search for maximum sum that are adjacent to
midpoint of array: what is runtime?

(fill out psuedocode on worksheet)

What is the overall runtime?

- Base case: constant time
- First two recursions are $T(n/2)$
- Our helper function is $\Theta(n)$
- Overall asymptotic recurrence is $T(n) = 2T(n/2) + \Theta(n)$.

(draw recursion tree)

What other algorithm does this recursion tree remind us of?
