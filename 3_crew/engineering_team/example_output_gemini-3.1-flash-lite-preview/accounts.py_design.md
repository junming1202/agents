### Technical Design: `accounts.py`

This module provides the core logic for the trading simulation account management system. It encapsulates state management for cash balances and share holdings, enforces trade validation rules, and calculates performance metrics.

#### Module Structure

```python
"""
accounts.py
A self-contained module for managing trading simulation accounts.
"""

def get_share_price(symbol: str) -> float:
    """
    Mock function to retrieve current market price.
    Returns fixed values for AAPL, TSLA, GOOGL; raises ValueError for others.
    """
    pass

class Account:
    """
    Handles user account state, trade execution, and portfolio analysis.
    """

    def __init__(self, initial_balance: float):
        """
        Initializes the account with an starting balance.
        :param initial_balance: The starting cash in the account.
        """
        self.balance = initial_balance
        self.initial_deposit = initial_balance
        self.holdings = {}  # {symbol: quantity}
        self.transactions = [] # List of dicts: {'type': 'BUY'/'SELL', 'symbol': str, 'qty': int, 'price': float}

    def deposit(self, amount: float) -> None:
        """Increases account balance."""
        pass

    def withdraw(self, amount: float) -> None:
        """
        Withdraws funds.
        Raises ValueError if amount > balance.
        """
        pass

    def buy(self, symbol: str, quantity: int) -> None:
        """
        Executes a buy order.
        Validates: if user can afford the total cost.
        Updates balance, holdings, and transaction history.
        """
        pass

    def sell(self, symbol: str, quantity: int) -> None:
        """
        Executes a sell order.
        Validates: if user has enough shares to sell.
        Updates balance, holdings, and transaction history.
        """
        pass

    def get_portfolio_value(self) -> float:
        """
        Calculates total value (cash + (current_price * quantity for each holding)).
        """
        pass

    def get_profit_loss(self) -> float:
        """
        Calculates current portfolio value - initial deposit.
        """
        pass

    def get_holdings(self) -> dict:
        """Returns the dictionary of symbol: quantity holdings."""
        pass

    def get_transaction_history(self) -> list:
        """Returns the list of all recorded transactions."""
        pass
```

#### Detailed Implementation Requirements

1.  **Validation Logic**:
    *   `withdraw`: Must ensure `self.balance - amount >= 0`.
    *   `buy`: Must ensure `self.balance >= (price * quantity)`.
    *   `sell`: Must ensure `self.holdings.get(symbol, 0) >= quantity`.
2.  **Portfolio Calculation**:
    *   `get_portfolio_value` iterates through `self.holdings`, calls `get_share_price(symbol)` for each, and sums the total.
3.  **Transaction Tracking**:
    *   Each trade (`buy` or `sell`) should append a record to `self.transactions` containing the timestamp, symbol, quantity, price at time of execution, and type.
4.  **Error Handling**:
    *   All methods must raise descriptive `ValueError` or `RuntimeError` exceptions when validation logic fails, preventing illegal states.
5.  **Mock Price Source**:
    *   Ensure `get_share_price` returns `150.0` for 'AAPL', `700.0` for 'TSLA', and `2800.0` for 'GOOGL' to satisfy testing requirements.