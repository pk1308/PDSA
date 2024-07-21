# Lecture 8.3 - Divide and Conquer-Integer Multiplication.pdf (PDF file)
**Summary**
**Integer Multiplication**

**Introduction**

Multiplying two integers x and y, each with n bits, traditionally involves multiplying each digit of y by x and adding up the partial products, requiring O(n^2) time.

**Divide and Conquer Approach**

Karatsuba's algorithm uses divide and conquer to reduce the complexity of integer multiplication.

**Algorithm**

1. Split x and y into two groups of n/2 bits each:
    - x = x1x0
    - y = y1y0

2. Calculate:
    - p = x1y1
    - q = x0y0
    - r = (x1 - x0)(y1 - y0)

3. Return:
    - p * 2^n + (p + q - r) * 2^n/2 + q

**Analysis**

- T(1) = 1
- T(n) = 3T(n/2) + n
- T(n) = 3 * T(n/2) + n
    - = 3 * (3 * T(n/4) + n/2) + n
    - = 3^2 * T(n/2^2) + (3/2 + 1) * n
- T(n) = 3^log n * T(n/2^log n) + ((3/2)^(log n - 1) + ... + (3/2)^1 + 1) * n
- T(n) = 3^log n * T(1) + ((3/2)^(log n - 1) + ... + (3/2)^1 + 1) * n
- T(n) = 3^log n + ((3/2)^(log n - 1) + ... + (3/2)^1 + 1) * n
- T(n) = 3^log n + O(n)
- T(n) = O(n^(log 3)) ≈ O(n^1.59)

**Historical Note**

- Andrei Kolmogorov conjectured that integer multiplication in subquadratic time is impossible.
- Anatolii Karatsuba developed this divide and conquer algorithm in 1960, refuting Kolmogorov's conjecture.
- The algorithm can be used in any base, not just binary.
