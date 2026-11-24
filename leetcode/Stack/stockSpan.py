
# n -> number of calls
# TC -> worst: O(n); average: amortized O(1)
# SC -> O(n)


class StockSpanner:

    def __init__(self):
        self.stack = []


    def next(self, price: int) -> int:
        count = 1
        while self.stack and price >= self.stack[-1][0]:
            _, prev_count = self.stack.pop()
            count += prev_count

        self.stack.append((price, count))
        return count