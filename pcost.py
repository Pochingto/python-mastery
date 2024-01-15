TXT = "Data/portfolio.dat"

total_sum = 0
with open(TXT, "r", encoding="utf-8") as f:
    for line in f: 
        stock, count, price = line.strip().split(" ")
        count = int(count)
        price = float(price)

        total_sum += count * price

print(f"Final total price: {total_sum}")