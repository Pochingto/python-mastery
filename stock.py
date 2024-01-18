import csv


class Stock:
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = int(shares)
        self.price = float(price)

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    @classmethod
    def read_portfolio(cls, filename):
        f = open(filename)
        rows = csv.reader(f)
        headings = next(rows)
        portfolio = [cls(*row) for row in rows]

        return portfolio

    @staticmethod
    def print_portfolio(portfolio):
        headings = ["name", "shares", "price"]
        print("%10s %10s %10s" % (headings[0], headings[1], headings[2]))
        for s in portfolio:
            print("%10s %10d %10.2f" % (s.name, s.shares, s.price))
