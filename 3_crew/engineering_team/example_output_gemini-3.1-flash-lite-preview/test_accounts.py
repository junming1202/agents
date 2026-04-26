import unittest

def get_share_price(symbol: str) -> float:
    prices = {'AAPL': 150.0, 'TSLA': 700.0, 'GOOGL': 2800.0}
    if symbol in prices:
        return prices[symbol]
    raise ValueError(f'Symbol {symbol} not supported')

class Account:
    def __init__(self, initial_balance: float):
        self.balance = float(initial_balance)
        self.initial_deposit = float(initial_balance)
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError('Deposit amount must be positive')
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError('Insufficient funds for withdrawal')
        self.balance -= amount

    def buy(self, symbol: str, quantity: int) -> None:
        price = get_share_price(symbol)
        total_cost = price * quantity
        if self.balance < total_cost:
            raise ValueError('Insufficient balance to buy shares')
        
        self.balance -= total_cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.transactions.append({'type': 'BUY', 'symbol': symbol, 'qty': quantity, 'price': price})

    def sell(self, symbol: str, quantity: int) -> None:
        if self.holdings.get(symbol, 0) < quantity:
            raise ValueError('Insufficient holdings to sell shares')
        
        price = get_share_price(symbol)
        self.balance += (price * quantity)
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append({'type': 'SELL', 'symbol': symbol, 'qty': quantity, 'price': price})

    def get_portfolio_value(self) -> float:
        holding_value = sum(get_share_price(sym) * qty for sym, qty in self.holdings.items())
        return self.balance + holding_value

    def get_profit_loss(self) -> float:
        return self.get_portfolio_value() - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings

    def get_transaction_history(self) -> list:
        return self.transactions

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)
        with self.assertRaises(ValueError):
            self.account.deposit(-100.0)

    def test_withdraw(self):
        self.account.withdraw(500.0)
        self.assertEqual(self.account.balance, 500.0)
        with self.assertRaises(ValueError):
            self.account.withdraw(2000.0)

    def test_buy_and_sell(self):
        self.account.buy('AAPL', 2)
        self.assertEqual(self.account.holdings['AAPL'], 2)
        self.assertEqual(self.account.balance, 700.0)
        self.account.sell('AAPL', 1)
        self.assertEqual(self.account.holdings['AAPL'], 1)
        self.assertEqual(self.account.balance, 850.0)

    def test_insufficient_funds_buy(self):
        with self.assertRaises(ValueError):
            self.account.buy('GOOGL', 1)

    def test_insufficient_holdings_sell(self):
        with self.assertRaises(ValueError):
            self.account.sell('AAPL', 1)

    def test_portfolio_value(self):
        self.account.buy('TSLA', 1)
        # Balance 300, TSLA 700 = 1000 total
        self.assertEqual(self.account.get_portfolio_value(), 1000.0)

    def test_profit_loss(self):
        self.account.buy('AAPL', 1)
        # Price 150. Portfolio value remains 1000. P/L = 0
        self.assertEqual(self.account.get_profit_loss(), 0.0)

    def test_invalid_symbol(self):
        with self.assertRaises(ValueError):
            get_share_price('INVALID')

if __name__ == '__main__':
    unittest.main()