class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value-to-weight ratio

def knapsack_greedy(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0
    for item in items:
        if capacity >= item.weight:
            total_value += item.value
            capacity -= item.weight
        else:
            total_value += item.ratio * capacity
            break

    return total_value

# Predefined example
items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]
capacity = 50

# Calculate maximum value
max_value = knapsack_greedy(items, capacity)
print("Maximum value in Knapsack:", max_value)
