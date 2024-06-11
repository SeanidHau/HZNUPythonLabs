class Stock :

    def __init__(self, stock_code = 0, total_shares = 0, total_cost = 0):
        self.stock_code = stock_code
        self.total_shares = total_shares
        self.total_cost = total_cost
    
    def get_stock_code(self):
        return self.stock_code
    
    def get_total_shares(self):
        return self.total_shares
    
    def get_total_cost(self):
        return self.total_cost
    
    def purchase(self, shares, cost):
        self.total_shares += shares
        self.total_cost += cost*shares
    
    def get_profit(self, price):
        return self.total_shares * price - self.total_cost


class DividendStock(Stock):
    
    def __init__(self, stock_code, dividends=0):
        super().__init__()
        self.stock_code = stock_code
        self.dividends = dividends
    
    def pay_dividend(self, num):
        self.dividends += num * super().get_total_shares()
    
    def get_profit(self, price):
        return super().get_total_shares() * price - super().get_total_cost() + self.dividends