import numpy as np
import matplotlib.pyplot as plt

F = {}

def RecFib(n):
  if n==0:
    return 0, 1
  elif n==1:
    return 1, 1
  else:
    F1, c1 = RecFib(n-1)
    F2, c2 = RecFib(n-2)
    return F1+F2, c1+c2

def MemFib(n):
  rec = 1
  if n==0 or n==1:
    return n, 1
  else:
    if n not in F:
      F1, c1 = MemFib(n-1)
      F2, c2 = MemFib(n-2)
      F[n] = F1 + F2
      rec += c1+c2
    return F[n], rec

def measure(n):
    rec_counts = np.zeros(n)
    mem_counts = np.zeros(n)
    for i in range(n):
        Fi, ci = RecFib(i)
        rec_counts[i] = ci
        Fi, ci = MemFib(i)
        mem_counts[i] = ci
    fig, ax = plt.subplots()
    ax.plot(rec_counts, color='red')
    ax.plot(mem_counts, color='blue')
    plt.show()

if __name__ == '__main__':
    measure(15)
