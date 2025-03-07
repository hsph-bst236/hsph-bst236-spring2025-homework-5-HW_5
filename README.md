# Homework 5: Numerical Linear Algebra

The due date is March 13 at midnight. Please follow the [code squad rules](https://junwei-lu.github.io/bst236/chapter_syllabus/syllabus/#code-squad). If you are using the late days, please note in the head of README.md that “We used XX late days this time, and we have XX days remaining”. 

This homework will help you to get familiar with the following topics:

- Solve a large linear system
- Compute eigenvalues of a large matrix
- Numerical computation of matrix functions
- Improve the computation efficiency of linear algebra operations

In `Readme.md#Report`, you need to explain the idea of your algorithm. Report the best answer you can get in the report. If you can get an answer beyond of the precision of IEEE 754 double-precision, you can report as many accurate digits as you can.


You can only choose the initial values, searching interval, hyperparameters, stopping criteria, etc., without utilizing any prior knowledge of the answer. 



Add all the packages you need in the `requirements.txt` file. The problems may only need `numpy` and `scipy`.

## Problem 1: Marching Towards Infinity

We have an infinitely large matrix $M$ with entries

$$
M_{jk} = \frac{1}{(j + k - 1)(j + k)/2 - (k - 1)}
$$

for $j, k = 1, 2, \ldots$. 

Find the maximum singular value of $M$:

$$
\sigma_{\max}(M) = \lim_{n \to \infty} \sigma_{\max}(M_n),
$$

where $M_n$ is the $n \times n$ principal submatrix of $M$. (It can be shown that the limitation above exists.)

Write you code in `sig1_M()` defined in `problem1.py` to return the answer. You code need to pass the Github Action test to return the answer within **2 minutes** under the setup used by the [GitHub Actions](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners#standard-github-hosted-runners-for--private-repositories).





### **Bit Battle** 🎮

Problem 1 is a bit battle event. We will rank your code based on the absolute error to the true value. If the answer has achieved the absolute error less than $1\times10^{-15}$, we will then rank the code based on its running time.

## Problem 2: Airemun's Journey

In the enchanted realm of Numeria, a lively sprite named Airemun embarks on an adventure from her home at the origin $(0,0)$ on an endless grid of magic. With each bound, she leaps one unit in one of four cardinal directions. The rules of her journey are as follows:

- A jump directly upward or downward occurs with probability $\frac{1}{4}$ each.
- A leap eastward is slightly favored, occurring with probability $\frac{1}{4} + \delta$.
- A hop to the west happens with a diminished chance of $\frac{1}{4} - \delta$.

It is foretold that the probability of Airemun eventually returning to her starting point is exactly $\frac{1}{2}$. What, then, must the bias parameter $\delta$ be?

![Airemun's journey](problem2.png)

You can find the linear algebra translation to the problem in `Hint.pdf`.

Write your code in `Numeria_delta()` defined in `problem2.py` to return the answer. If you are applying some root finding algorithm (e.g. `scipy.optimize.brute` or `scipy.optimize.bisect`), to be fair, your searching interval need to use the trivial one $[0, 1/4]$.
You code need to pass the Github Action test to return the answer within **2 minutes** under the setup used by the [GitHub Actions](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners#standard-github-hosted-runners-for--private-repositories). 







