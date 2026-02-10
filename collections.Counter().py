from collections import Counter

# Read number of shoes (though not strictly needed for the logic)
num_shoes = int(input())

# Read shoe sizes and convert to a Counter dictionary
shoe_inventory = Counter(map(int, input().split()))

# Read number of customers
num_customers = int(input())

total_earned = 0

for _ in range(num_customers):
    # Read desired size and offered price
    size, price = map(int, input().split())
    
    # Check if size is in stock
    if shoe_inventory[size] > 0:
        total_earned += price
        shoe_inventory[size] -= 1  # Reduce stock by 1

print(total_earned)