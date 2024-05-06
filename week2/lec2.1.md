# **Week 2**

**ANALYSIS OF ALGORITHMS**

Measuring performance:

Example of validating SIM cards against Aadhaar data.

Naive approach takes thousands of years

Smarter solution takes a few minutes.

Two main resources of interest

* Running time - how long the algorithm takes
* Space - memory management

Time depends on processing power

* Impossible to change for given hardware
* Enhancing hardware has only a limited impact at a practical level
* Storage is limited by available memory
* Easier to congure, augmen

Typically, we focus on time rather than space.

Analysis of time dependence:

Input Size: Running time depends on input size.Larger arrays will take longer to sort.

Measure time eciency as function of input size

1. Input size n
2. Running time t(n)

Different input of size n may take different amounts of time

Example 1: SIM cards v/s Aadhaar Cards


$$\ \frac{x_{1} +x_{2} +x_{3\ .................\ +\ x_{n}}}{n}$$

log2(n) = kn = ⇒2kExample 2: Video gameSeveral objects on screenBasic step: nd closest pair of objects.n objects - naive algorithm is For each pair of objects, compute their distanceReport minimum distance across all pairs.There is a clever algorithm that takes time nlog2nHigh resolution gaming console may have 4000x2000 pixels.8 x  points - 8 millionSuppose we have 100,000 = 1 x  objects.Naive algorithm takes  steps1000 seconds, or 16.7 minutes in Python.Unacceptable response time!log2100,000 is under 20, so nlog2n takes a fraction of a second.n21061051010Orders of magnitudeWhen comparing t(n), focus on orders of magnitudeIgnore constant factorsf(n) =  eventually grows faster than g(n) = 5000For small values of n, f(n) < g(n)After n = 5000, f(n) overtakes g(n)Asymptotic complexityWhat happens in the limit, as n becomes largeTypical growth functionsIs t(n) proportional to logn, ..., , , ..., ?Note: logn means log2n by defaultLogarithmic, polynomial, exponential...n3n2n2n32nThe red colour line is called the "feasibility line"

Measuring running timeAnalysis should be independent of the underlying hardwareDon't use actual timeMeasure in terms of basic operationsTypical basic operationsCompare two valuesAssign a value to a variableExchange a pair of values?(x,y) = (y,x)t = xx = yy = tIf we ignore constants, focus on orders of magnitude, both are within a factor of 3.Need not be very precise about dening basic operations.What is the input size?Typically a natural parameter

Size of a list/array that we want to search or sortNumber of objects we want to rearrangeNumber of vertices and number of edges in a graphSeparate parametersNumeric problems? Is n a prime?Magnitude of n is not the correct measure.Arithmetic operations are performed digit by digitAddition with carry, subtraction with borrow, multiplication, long division ...Number of digits is a natural measure of input sizeSame as logbn, when we write n in base bWhich inputs should we consider?Performance varies across input instancesBy luck, the value we are searching for is the rst element we examine in an arrayIdeally, want the "average" behaviorDicult to computeAverage over what? Are all inputs equally likely?Need a probability distribution over inputsInstead, worst case inputInput that forces algorithm to take longest possible timeSearch for a value that is not present in an unsorted listMust scan all elementsPessimistic - worst case may be rareUpper bound for worst case guarantees good performanceSummary:Two important parameters when measuring algorithm performanceRunning time, memory requirement (space)Mainly focus on timeRunning time t(n) is a function of input size nInterested in orders of magnitudeAsymptotic complexity, as n becomes largeFrom running time, we can estimate feasible input sizesWe focus on worst case inputs

Pessimistic, but easier to calculate than average caseUpper bound on worst case gives us an overall guarantee on performanceCOMPARING ORDERS OF MAGNITUDEUpper Boundsf(x) is said to be O(g(x)) if we can nd constants c and x0 such that c.g(x)is an upperbound for f(x) for x beyond x0f(x)cg(x) for every x x0≤≥

Examples:1. 100n + 5 is O()100n + 5  100n + n = 101n, for n 5101n 101Choose n0 = 5, c = 101 ∀nn0 (i.e 5) 100n 101Alternatively,100n + 5  100n + 5n = 105n for n1105n 105Choose n0 = 1, c = 105∀nn0 (i.e 1) 100n 105g(x) Choice of n0, c not unique. 2. 100 + 20n + 5 is O()100 + 20n + 5  100 + 20 + 5, for n  1100 + 20n + 5  125, for n  1Choose n0 = 1, c = 125What matters is the highest term20n + 5 is dominated by 100 is not O()No matter what c we choose, c will be dominated by  for ncn2≤≥≤n2⇒≥≤n2≤≥≤n2⇒≥≤n2n2n2≤n2n2n2≥n2≤n2≥n2n3n2n2n3≥Useful properties:If f1(n) is O(g1(n)) and f2(n) is O(g2(n)), then f1(n) + f2(n) is O(max(g1(n),g2(n)))Prooff1(n)  c1g1(n) for n > n1f2(n)  c2g2(n) for n > n2Let c3 = max(c1, c2) = max(n1, n2)For n  n3, f1(n) + f2(n)  c1g1(n) + c2g2(n)  c3(g1(n) + g2(n))  2c3(max(g1(n),g2(n)))Algorithm has two phases:Phase A takes time O(gA(n))Phase B takes time O(gB(n))Algorithm as a whole takes time max(O(gA(n), gB(n)))≤≤≥≤≤≤

Least ecient phase is the upper bound for the whole algorithmLower Boundsf(x) is said to be (g(x)) if we can nd constants c and x0 such that cg(x) is a lower boundfor f(x) for x beyond x0f(x)  cg(x) for every x  x0 is () >  for all n, so n0 = 1, c = 1Typically we establish lower bounds for a problem rather than an individual algorithmIf we sort a list by comparing elements and swapping them, we require (nlogn)comparisons.This is independent of the algorithm we use for sorting.Ω≥≥n3Ωn2n3n2ΩTight boundsF(x) is said to be (g(x))if it is both O(g(x)) and (g(x))Find constants c1, c2, x0 such that c1g(x)  f(x)  c2g(x) for every x x0n(n - 1)/2 is ()Upper bound:n(n-1)/2 =/2 - n/2 /2 for all n  0;  = Lower bound:n(n-1)/2 = /2 - n/2 /2 - (n/2 x n/2) /4 for all n  2;  = Choose n0 = 2, c1 = 1/4, c2 = 1/2ΘΩ≤≤≥Θn2n2≤n2≥c11/2n2≥n2≥n2≥c21/4Summaryf(n) is O(g(n)) means g(n) is an upper bound for f(n)Useful to describe asymptotic worst case running timef(n) is (g(n)) means g(n)is a lower bound for f(n)Typically used for a problem as a whole, rather than an individual algorithmf(n) is (g(n)): matching upper and lower boundsWe have found an optimal algorithm for a problemΩΘCALCULATING COMPEXITY - EXAMPLESCalculating complexity

Iterative programsRecursive programsIterative programsEXAMPLE 1: Find the maximum element in a listInput size is legth of the listSingle loop scans all elementsAlways takes n stepsOverall time is O(n)defmaxElement(L):  maxval = L[0]for i inrange(len(L)):if L[i] > maxval:      maxval = L[i]return maxvalEXAMPLE 2: Check whether a list contains duplicatesInput size is length of the listNested loop scans all pairs of elementsA duplicate may be found in the very rst iterationWorst case - no duplicates, both loops ran fullyTime is: (n - 1) + (n - 2) + ... + 1 = n(n - 1)/2Overall time is O()n2defnoDuplicates(L):for i inrange(len(L)):for j inrange(i + 1,len(L)):if L[i] == L[j]:returnFalsereturnTrueEXAMPLE 3:Matrix multiplicationMatrix is represented as list of lists[[1,2,3],[4,5,6]]Input matrices have size m x n, n x p()142536

Output matrix is m x pThree nested loopsOverall time is O(mnp) - O() if both are n x nn3defmatrixMultiply(A,B):  (m,n,p) = (len(A), len(B), len(B[0]))  c = [[0for i inrange(p) ]for j inrange(m) ]for i inrange(m):for j inrange(p):for k inrange(n):        c[i][j] = c[i][j] + A[i][k] * B[k][j]return cEXAMPLE 4Number of bits in binary representation of nlog n steps for n to reach 1For number theoretic problems, input size is number of digitsThis algorithm is linear in input sizedefnumberOfBits(n):  count = 1while n > 1:    count = count + 1    n = n // 2return countEXAMPLE 5 Towers of Hanoi Three pegs A, B, CMove n disks from A to B, use C as transit pegNever put a larger disk on a snaller one Recursive Solution:Move n - 1 disks from A to C, use B as transit pegMove larger disk from A to BMove n - 1 disks from C to B, use A as transit peg Recurrence:M(n) - number of moves to transfer n disksM(1) = 1M(n) = M(n - 1) + 1 + M(n - 1) = 2M(n - 1) + 1Unwind and solve:M(n) = 2M(n - 1) + 1 = 2(2M(n - 2) + 1) + 1 = M(n - 2) + (2 + 1) = (2M(n - 3) + 1) + (2 + 1) = M(n - 3) + (4 + 2 + 1) 222223

...= M(n - k) + ( - 1)) ... = M(1) + ( - 1) =  +  - 1 =  - 12k2k2n−12n−12n−12n−12nSummaryIterative programsFocus on loopsRecursive programsWrite and solve a recurrenceNeed to be clear about accounting for "basic" operationsSEARCHING IN A LISTSearch problemIs value v present in list l ?Naive solution scans the listInput size n, the length of the listWorst case is when v is not present in lWorst case complexity is O(n)defnaivesearch(v,l):for x in l:if v == x:returnTruereturnFalseSearching a sorted listWhat if l is sorted in ascending order?Compare v with the midpoint of lIf midpoint is v, the value is foundIf v less than midpoint, search the rst halfIf v greater than midpoint, search the second halfStop when the interval to search becomes emptydefbinarysearch(v,l):if l == []:
