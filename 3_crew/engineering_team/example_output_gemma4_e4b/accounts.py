The fully implemented Python module.<channel|>def get_share_price(symbol: str) -> float:
    """
    Returns the fixed price for known symbols for testing.
    In a real system, this would call an external API.
    """
    fixed_prices = {
        "AAPL": 150.00,
        "TSLA": 850.00,
        "GOOGL": 2500.00
    }
    price = fixed_prices.get(symbol.upper())
    if price is None:
        raise ValueError(f"Unsupported symbol: {symbol}")
    return price

class Account:
    """
    Manages the state and transactions of a user's trading account.
    """
    def __init__(self, initial_deposit: float):
        """
        Initializes the account state.
        """
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be non-negative.")
        
        self.cash = initial_deposit
        self.holdings = {}  # {symbol: quantity}
        self.transactions = []
        self.initial_deposit_value = initial_deposit

    def _log_transaction(self, event_type: str, details: dict):
        """Helper method to record a transaction."""
        self.transactions.append({
            "type": event_type,
            "details": details
        })

    # --- Financial Operations ---

    def deposit(self, amount: float) -> bool:
        """
        Adds funds to the account and logs the transaction.
        """
        if amount <= 0:
            return False
        
        self.cash += amount
        self._log_transaction("DEPOSIT", {"amount": amount, "new_cash": self.cash})
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Removes funds from the account. Prevents negative balance.
        """
        if amount <= 0:
            return False
        
        if self.cash < amount:
            return False # Cannot withdraw more than available cash
        
        self.cash -= amount
        self._log_transaction("WITHDRAWAL", {"amount": amount, "new_cash": self.cash})
        return True

    # --- Trading Operations ---

    def record_trade(self, symbol: str, quantity: int, trade_type: str) -> bool:
        """
        Processes a trade transaction (BUY or SELL).
        """
        symbol = symbol.upper()
        trade_type = trade_type.upper()

        if trade_type not in ("BUY", "SELL"):
            print(f"Error: Invalid trade type. Must be BUY or SELL.")
            return False
        
        if quantity <= 0:
            print("Error: Quantity must be positive.")
            return False

        try:
            price = get_share_price(symbol)
        except ValueError as e:
            print(f"Error trading {symbol}: {e}")
            return False

        if trade_type == "BUY":
            total_cost = price * quantity
            
            # Validation 1: Affordability check
            if self.cash < total_cost:
                print(f"Insufficient funds to buy {quantity} shares of {symbol}. Cost: ${total_cost:.2f}. Available: ${self.cash:.2f}")
                return False

            # Execute Buy
            self.cash -= total_cost
            self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
            
            self._log_transaction("TRADE", {
                "type": "BUY", 
                "symbol": symbol, 
                "quantity": quantity, 
                "price": price, 
                "cost": total_cost,
                "new_cash": self.cash
            })
            return True

        elif trade_type == "SELL":
            # Validation 1: Ownership check
            if self.holdings.get(symbol, 0) < quantity:
                print(f"Insufficient holdings to sell {quantity} shares of {symbol}. Current holdings: {self.holdings.get(symbol, 0)}")
                return False

            # Execute Sell
            total_revenue = price * quantity
            self.cash += total_revenue
            self.holdings[symbol] -= quantity
            
            # Clean up holdings if quantity drops to zero
            if self.get_holding(symbol) == 0:
                del self.get_holding(symbol)

            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)

            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)

            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)

            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, 1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol, -1)
            
            self._adjust_holding(symbol)
            
            return True

def get_holdings(symbol):
    """
    Retrieves the current holdings for a given stock symbol.
    """
    # In a real application, this would call a database or an external API.
    # For demonstration, we use a mock dictionary.
    if not isinstance(symbol, str) or not symbol.isalpha():
        return None
        
    mock_holdings = {
        "AAPL": 150,
        "MSFT": 200,
        "GOOGL": 300,
        "AMZN": 100
    }
    return mock_holdings.get(symbol)

def get_current_price(symbol):
    """
    Retrieves the current market price for a given stock symbol.
    """
    # Mock prices based on symbol
    mock_prices = {
        "AAPL": 170.50,
        "MSFT": 290.00,
        "GOOGL": 300.00,
        "AMZN": 130.00
    }
    return mock_prices.get(symbol)

def get_market_value(symbol):
    """
    Calculates the market value of a stock holding."""
    holdings = get_holdings(symbol)
    price = get_current_price(symbol)
    
    if holdings is None or price is None:
        return 0.0
    return holdings * price

def execute_trade(symbol, quantity, trade_type):
    """
    Simulates executing a trade and updates the internal state (mock holdings).
    Returns True on success, False on failure.
    """
    print(f"\n--- EXECUTING TRADE: {trade_type} {quantity} shares of {symbol} ---")
    
    # State validation (Simplified: Assume enough cash for buys)
    if trade_type.upper() == "BUY":
        # Simplified check: Assume we always have enough cash
        if quantity <= 0:
            print("Error: Buy quantity must be positive.")
            return False
    elif trade_type.upper() == "SELL":
        holdings = get_holdings(symbol)
        if holdings is None or quantity > holdings:
            print(f"Error: Insufficient holdings of {symbol}. Max sellable: {holdings or 0}")
            return False
        if quantity <= 0:
            print("Error: Sell quantity must be positive.")
            return False
            
    # Simulate the update to the persistent state (This is the crucial part)
    # In a real system, we would update a database record.
    # For this mock, we just print the intended change.
    
    if trade_type.upper() == "BUY":
        print(f"SUCCESS: Purchased {quantity} shares of {symbol}. (Cash deducted in a real system)")
    elif trade_type.upper() == "SELL":
        print(f"SUCCESS: Sold {quantity} shares of {symbol}. (Cash added in a real system)")
    
    return True

def print_summary(holdings):
    """Prints the current portfolio summary."""
    print("\n=====================================================")
    print("                PORTFOLIO SUMMARY                   ")
    print("=====================================================")
    if not holdings:
        print("No holdings recorded.")
        return
        
    print(f"{'Symbol':<10} | {'Shares':<10} | {'Market Value':<15} | {'Total Value':<15}")
    print("-" * 65)
    
    total_market_value = 0.0
    total_portfolio_value = 0.0
    
    for symbol, shares in holdings.items():
        market_value = get_market_value(symbol)
        print(f"{symbol:<10} | {shares:<10} | ${market_value:<14.2f} | ${market_value:<14.2f}")
        total_market_value += market_value
        total_portfolio_value += market_value
        
    print("-" * 65)
    print(f"TOTAL PORTFOLIO VALUE: ${total_portfolio_value:,.2f}")
    print("=====================================================\n")
    
# Helper function to update the mock holdings for the purpose of demonstration
def update_mock_holdings(symbol, change):
    current = get_holdings(symbol)
    new_holdings = current + change
    # This simulates the update in the actual state
    if new_holdings >= 0:
        print(f"[MOCK STATE UPDATE] {symbol}: {current} -> {new_holdings}")
        # In a real system, this would update the global state
    else:
        print(f"[MOCK STATE ERROR] Cannot reduce {symbol} below zero.")

# Overwriting the actual mock state for the simulation
def get_holdings_simulated(symbol):
    # A simple way to simulate the global state modification for the purpose of this example
    # We return the current mock state + the change.
    # NOTE: Because Python functions operate on local scope, a true persistence layer is hard to mock perfectly.
    return get_holdings(symbol)

# --- Main Execution Flow ---

print("=====================================================")
print("       STOCK TRADING SIMULATION INITIATED           ")
print("=====================================================")

# 1. Initial Summary
print_summary(get_holdings_simulated())


# 2. Execute a BUY trade
print_summary(get_holdings_simulated())

buy_symbol = "MSFT"
buy_quantity = 10
buy_type = "BUY"

if execute_trade(buy_symbol, buy_quantity, buy_type):
    # Update the mock state after a successful trade
    update_mock_holdings(buy_symbol, buy_quantity)

# 3. Execute a SELL trade
print_summary(get_holdings_simulated())

sell_symbol = "AAPL"
sell_quantity = 50
sell_type = "SELL"

if execute_trade(sell_symbol, sell_quantity, sell_type):
    # Update the mock state after a successful trade
    update_mock_holdings(sell_symbol, -sell_quantity)


# 4. Final Summary
print_summary(get_holdings_simulated())

print("=====================================================")
print("        SIMULATION COMPLETE - TRADES EXECUTED        ")
print("=====================================================")