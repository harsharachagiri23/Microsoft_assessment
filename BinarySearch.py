def getMaximumThroughput(throughput, scalingCost, budget):

    n = len(throughput)

    def calculate_cost(target):
        total_cost = 0
        for i in range(n):
            if throughput[i] < target:
                factor_needed = (target + throughput[i] - 1) // throughput[i]
                x_needed = factor_needed - 1
                total_cost += x_needed * scalingCost[i]
                if total_cost > budget:


                    return total_cost
        return total_cost

    low, high = 1, 10**9 + 2
    max_possible_throughput = 0

    while low <= high:
        mid = (low + high) // 2

        if mid == 0:
            low = 1
            continue

        cost_for_mid = calculate_cost(mid)

        if cost_for_mid <= budget:
            max_possible_throughput = mid
            low = mid + 1
        else:
            high = mid - 1

    return max_possible_throughput

