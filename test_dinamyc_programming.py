
def knapsack_wit1hout_repeats(capacity, weight_list):
    """Time complexity: O(capacity * n), where n = len(item_list)
    Gold cost per unit is constant => item cost in proportional to it's weight
    Let the cost per unit = 1
    """
    cost = 1
    previous = [0] * (capacity + 1)

    for i in range(1, len(weight_list) + 1):
        current = [0]

        for w in range(1, capacity + 1):
            current.append(previous[w])
            if weight_list[i - 1] <= w:
                current[w] = max(current[w], previous[w - weight_list[i - 1]] + cost * weight_list[i - 1])
        previous = current

    return previous[capacity] // cost


def main():
    capacity = (int(i) for i in input().split())
    weight_list = [int(i) for i in input().split()]

    print(knapsack_wit1hout_repeats(capacity, weight_list))
main()
