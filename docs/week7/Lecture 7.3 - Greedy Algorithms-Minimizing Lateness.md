# Lecture 7.3 - Greedy Algorithms-Minimizing Lateness.pdf (PDF file)
**Summary**
**Introduction**

Greedy algorithms are a type of algorithm that iteratively make locally optimal choices with the hope of finding a globally optimal solution. They are often used in situations where finding the globally optimal solution is computationally infeasible.

**Minimizing Lateness**

In the context of scheduling, lateness is defined as the amount of time by which a task finishes after its deadline. The goal of minimizing lateness is to find a schedule that minimizes the maximum lateness of any task.

**Greedy Strategies**

There are several different greedy strategies that can be used to minimize lateness. The most common strategies are:

* **Schedule tasks in increasing order of length (T(i))**
* **Give priority to tasks with smaller slack time (D(i) - T(i))**
* **Schedule tasks in increasing order of deadlines (D(i))**

**Correctness Proof**

The correctness of the greedy algorithm can be proven using the following steps:

1. Renumber the jobs so that they are sorted by deadline (D(1) ≤ D(2) ≤ · · · ≤ D(n)).
2. The final schedule is simply 1, 2, . . . , n.
3. No idle time is present in the schedule.
4. Shifting jobs earlier can only reduce lateness.

**Exchange Argument**

The exchange argument is a technique used to prove the correctness of greedy algorithms. It involves showing that any two schedules with no inversions and no idle time have the same maximum lateness.

**Optimal Schedule**

The claim is that there is an optimal schedule with no inversions and no idle time. This claim can be proven by repeatedly removing adjacent inversions from the schedule.

**Summary**

The greedy algorithm for minimizing lateness is a simple and efficient algorithm that produces an optimal solution in O(n log n) time. The correctness of the algorithm follows from an exchange argument and the claim that there is an optimal schedule with no inversions and no idle time.
