```markdown
### accounts.py - Account Management System Design

This module, `accounts.py`, provides the core logic for managing a user's account in a trading simulation platform. It handles financial transactions (deposits/withdrawals) and investment trades (buy/sell), calculating portfolio value and profit/loss.

### Dependencies

The system relies on a function to fetch current share prices. A mandatory dependency function is defined below, including a test implementation.

#### Function: `get_share_price(symbol: str) -> float`

**Purpose:** Retrieves the current market price for a given stock symbol.
**Signature:** `get_share_price(symbol: str) -> float`
**Returns:** The current price of the share (float).

**Test Implementation (Mock):**
```python
def get_share_price(symbol: str) -> float:
    """Returns the fixed price for known symbols for testing."""
    fixed_prices = {
        "AAPL": 150.00,
        "TSLA": 850.00,
        "GOOGL": 2500.00
    }
    price = fixed_prices.get(symbol.upper())
    if price is None:
        raise ValueError(f"Unsupported symbol: {symbol}")
    return price
```

### Class: `Account`

**Purpose:** Encapsulates the entire state and business logic for a single user's trading account.

**Internal State Attributes:**

*   `cash`: `float` - The current liquid cash balance of the account.
*   `holdings`: `dict[str, int]` - Tracks the quantity of shares owned for each symbol (e.g., `{"AAPL": 10}`).
*   `transactions`: `list[dict]` - A comprehensive, immutable record of every financial and trade event.
*   `initial_deposit_value`: `float` - Stores the starting capital used as the baseline for P/L calculation.

#### Constructor

**Method:** `__init__(initial_deposit: float)`
*   **Description:** Initializes the account state.
*   **Parameters:**
    *   `initial_deposit`: The starting cash amount.
*   **Returns:** None.

#### Methods

**1. Financial Operations**

**Method:** `deposit(amount: float)`
*   **Description:** Adds funds to the account.
*   **Validation:** Ensures `amount` is positive.
*   **Side Effects:** Updates `self.cash`. Logs a `DEPOSIT` transaction.
*   **Returns:** `bool` (True on success, False on failure).

**Method:** `withdraw(amount: float)`
*   **Description:** Removes funds from the account.
*   **Validation:**
    1. Ensures `amount` is positive.
    2. Checks that `self.cash >= amount` (Preventing negative balance).
*   **Side Effects:** Updates `self.cash`. Logs a `WITHDRAWAL` transaction.
*   **Returns:** `bool` (True on success, False on failure).

**2. Trading Operations**

**Method:** `record_trade(symbol: str, quantity: int, trade_type: str)`
*   **Description:** Processes a trade transaction (BUY or SELL). This method enforces all trading rules and updates the account state atomically.
*   **Validation:**
    1. Checks if `symbol` is supported via `get_share_price()`.
    2. Ensures `quantity` is a positive integer.
    3. **If `trade_type` == 'BUY':**
        *   Retrieves price. Calculates total cost.
        *   Checks affordability: `self.cash >= total_cost`.
    4. **If `trade_type` == 'SELL':**
        *   Checks ownership: `self.holdings.get(symbol, 0) >= quantity` (Must own enough shares).
*   **Side Effects:**
    *   Updates `self.cash` (subtracting for BUY, adding for SELL).
    *   Updates `self.holdings`.
    *   Logs a `TRADE` transaction.
*   **Parameters:**
    *   `symbol`: Ticker symbol (e.g., "AAPL").
    *   `quantity`: Number of shares.
    *   `trade_type`: String, must be "BUY" or "SELL".
*   **Returns:** `bool` (True on successful trade, False otherwise, indicating violation).

**3. Reporting and Analysis**

**Method:** `get_holdings() -> dict[str, int]`
*   **Description:** Returns the current holdings of the account.
*   **Returns:** Dictionary mapping symbol to quantity.

**Method:** `get_portfolio_value() -> float`
*   **Description:** Calculates the current total market value of all holdings.
*   **Returns:** Total portfolio value.

**Method:** `get_profit_loss() -> float`
*   **Description:** Calculates the net profit or loss since the inception of the account (or since the first recorded transaction).
*   **Returns:** Net P&L value.

**Method:** `get_transactions_history() -> list`
*   **Description:** Returns a detailed list of all recorded trades.
*   **Returns:** List of transaction records.