# 💻 Coding Challenge Problems

This repository contains two distinct algorithmic problems: **Maximum Products Purchase** and **Maximum Throughput**.

---

## 1.  Maximum Products Purchase (`findMaximumValue`)

###  Problem Description

Alex is shopping where products are sold from $n$ cubicles. The prices are stored in a non-decreasing array, `prices`. For a given query, Alex starts at cubicle $pos$ (1-indexed) and visits all cubicles up to the last one. With a budget $amount$, the goal is to determine the **maximum number of products** Alex can purchase, buying at most **one product** from each visited cubicle, without exceeding the budget.

### ⚙️ Function Signature

```python
def findMaximumValue(prices: list[int], pos: list[int], amount: list[int]) -> list[int]:
    # prices: prices at each cubicle (sorted non-decreasingly)
    # pos: starting positions for each query (1-indexed)
    # amount: budgets for each query
    # Returns: an array of answers for each query
    pass
```
Input Data
* prices = [1, 2, 3, 4, 5]
* pos = [1, 3]
* amount = [4, 14]

Output
[2, 3]

## 2. ⚙️ Maximum Throughput (`getMaximumThroughput`)

### 📝 Problem Description

A data pipeline has $n$ services in series. The final throughput of the entire composite service is limited by the **minimum throughput** among all services.

A service **i** with initial throughput **throughput[i]** can be scaled **x** times at a cost of scalingCost[i] per scale-up. After scaling x times, its new throughput becomes **throughput[i]**.(1 + x).

Given a total **budget**, find the optimal scaling for all services to **maximize the final composite throughput**.

### ⚙️ Function Signature

```python
def getMaximumThroughput(throughput: list[int], scalingCost: list[int], budget: int) -> int:
    # throughput: initial throughput of each service
    # scalingCost: cost to scale each service once
    # budget: available money
    # Returns: the maximum possible final throughput
    pass
```

# Sample data 

* Input Data

*  throughput = [7, 3, 4, 6]

*  scalingCost = [2, 5, 4, 3]

*  budget = 25

# Output 

9


Service Index,   Initial Throughput,  Target Throughput,   Times Scaled (x),   Cost per Scaling,  Total Cost
0,                    7,                   14,                  1,                   2,               2
1,                    3,                    9,                  2,                   5,               10
2,                    4,                   12,                  2,                   4,                8
3,                    6,                   12,                  1,                   3,                3
Total                                                                                                 23


