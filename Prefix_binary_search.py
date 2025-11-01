# Example
#
# n=5
# prices = [3, 4, 5, 5, 7]
#     pos   1  2  3  4  5
#     index 0  1  2  3  4

#
# queries = [[2, 10], [1, 24], [5, 5]]
#
# Queries:
# 1. pos = 2, amount = 10:
# Alex visits cubicles 2 through 5 and can buy at most 2
# products.
#
# Alex can either buy from:
# • Cubicles 2 and 3: 4 + 5 = 9 (≤ 10)
# • Cubicles 2 and 4: 4 + 5 = 9 (≤ 10)
# • Cubicles 3 and 4: 5 + 5 = 10 (≤ 10)
# . Cubicles 2 and 5: 4 + 7 = 11 (≤ 10)
#
# The answer is 2.
#
# 2. pos = 1, amount = 24:
# Alex visits all cubicles and can buy from all of them since the
# total cost is 3 + 4 + 5 + 5 + 7 = 24 (≤ 24).
# The answer is 5.
#
#
# 3. pos= 5, amount = 5:
# Alex can only visit cubicle 5 but cannot make any purchase
# since the price (7) exceeds the available amount (5).
# The answer is 0.

# [2, 5, 0]

def findMaximumValue(prices, pos, amount):
    n = len(prices)
    results = []

    prefix_sum = [0] * (n + 1)
    # print("prefix sum ", prefix_sum)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + prices[i]

    # print("prefix sum after :", prefix_sum)
    #prices = [3, 4, 5, 5, 7]
    # prefix sum  [0, 3, 7, 0, 0, 0]
    # prefix sum after : [0, 3, 7, 12, 17, 24]

    # #iteration 1:
    #  i = 0
    #  prefix_sum[1] = 0 + 3

    #iteration 2:
    # i = 1
    #prefix_sum[2] = 3 + 4 = 7

    #iteration 3:
    # i = 2
    #prefix_sum[3] = 7 + 5 = 12
    print(" zip :", list(zip(pos, amount)))
    queries = list(zip(pos, amount))
    #[(2, 10), (1, 24), (5, 5)]
    for p_start, max_amount in queries:
        # print("start :", p_start)    #5
        # print("max_amount :", max_amount) #5
        #n = 5

        start_index = p_start - 1 #0
        max_k = n - start_index   #5

        low = 0   #0
        high = max_k  #5
        max_affordable_k = 0 #2
        #low = 6
        #high = 5
        #max_affordable_k = 5

        while low <= high: # 6 <= 5

            k = (low + high) // 2 #k = 5

            current_cost = prefix_sum[start_index + k] - prefix_sum[start_index]
            #prewfix +sum = [0, 3, 7, 12, 17, 24]
            # current_cost = 24 - 0 = 24

            if current_cost <= max_amount: #17 <= 24
                max_affordable_k = k #5
                low = k + 1  #6
            else:
                high = k - 1
                #2

        results.append(max_affordable_k)
        #result = [2, 5]

    return results


    # Happy Birthday Harsha !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


prices = [3, 4, 5, 5, 7]
pos = [2, 1, 5]
amount = [10, 24, 5]
output = findMaximumValue(prices, pos, amount)
print(f"Test 0: {output} == [2, 5, 0] -> {'PASS' if output == [2, 5, 0] else 'FAIL'}")

#     # Test Case 1
# prices = [1, 2, 2, 2, 3]
# pos = [2, 5]
# amount = [5, 2]
# output = findMaximumValue(prices, pos, amount)
# print(f"Test 1: {output} == [2, 0] -> {'PASS' if output == [2, 0] else 'FAIL'}")
