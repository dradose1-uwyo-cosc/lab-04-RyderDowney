items = ["deoderant", "goldfish", "legos", "candles", "toothpaste"]
prices = [5, 8, 40, 10, 3]
for I in range(len(items)):
    print(f"I bought {items[I]} for ${prices[I]} ")

total = 0
for t in prices:
    total = total + t
print(f"I spent ${total} at Walmart")

prices.sort()
print(f"The cheapest item I bought at walmart was ${prices[0]}")
print(f"The most expensive item I bought at Walmart was ${prices[-1]}")

leastIndex = prices.index(min(prices))
mostIndex = prices.index(max(prices))
print(f"The cheapest item was {items[leastIndex]}")
print(f"The most expensive item was {items[mostIndex]}")