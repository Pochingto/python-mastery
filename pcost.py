
def portfolio_cost(filename): 

    total_sum = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f: 
            try: 
                _, count, price = line.strip().split()
                count = int(count)
                price = float(price)

                total_sum += count * price
            except ValueError as e:
                print(f"Couldn't parse: {repr(line)}")
                print(f"Reason: {e}")

    return total_sum

if __name__ == "__main__": 
    cost = portfolio_cost("Data/portfolio3.dat")
    print(f"Total cost: {cost}")