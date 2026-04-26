import gradio as gr
from accounts import Account

# Initialize a single global account instance for the demo
account = None

def init_account(initial_deposit):
    global account
    account = Account(float(initial_deposit))
    return "Account initialized with balance: " + str(initial_deposit)

def perform_deposit(amount):
    if not account: return "Initialize account first"
    account.deposit(float(amount))
    return f"Deposited {amount}. Current Balance: {account.balance}"

def perform_withdraw(amount):
    if not account: return "Initialize account first"
    try:
        account.withdraw(float(amount))
        return f"Withdrew {amount}. Current Balance: {account.balance}"
    except ValueError as e:
        return str(e)

def perform_trade(action, symbol, quantity):
    if not account: return "Initialize account first"
    try:
        if action == "BUY":
            account.buy(symbol, int(quantity))
        else:
            account.sell(symbol, int(quantity))
        return f"Success: {action} {quantity} of {symbol}"
    except ValueError as e:
        return str(e)

def update_ui():
    if not account: return 0, 0, {}, []
    return (
        account.get_portfolio_value(),
        account.get_profit_loss(),
        account.get_holdings(),
        str(account.get_transaction_history())
    )

with gr.Blocks() as demo:
    gr.Markdown("# Trading Simulation UI")
    
    with gr.Tab("Account Setup"):
        init_val = gr.Number(label="Initial Deposit", value=1000)
        init_btn = gr.Button("Create Account")
        status = gr.Textbox(label="Status")
        init_btn.click(init_account, inputs=[init_val], outputs=[status])
        
    with gr.Tab("Transactions"):
        with gr.Row():
            d_amt = gr.Number(label="Deposit Amount")
            dep_btn = gr.Button("Deposit")
            w_amt = gr.Number(label="Withdraw Amount")
            wit_btn = gr.Button("Withdraw")
        
        with gr.Row():
            action = gr.Dropdown(["BUY", "SELL"], label="Action")
            symbol = gr.Dropdown(["AAPL", "TSLA", "GOOGL"], label="Symbol")
            qty = gr.Number(label="Quantity")
            trade_btn = gr.Button("Execute Trade")
            
        trade_out = gr.Textbox(label="Trade Output")
        dep_btn.click(perform_deposit, inputs=[d_amt], outputs=[trade_out])
        wit_btn.click(perform_withdraw, inputs=[w_amt], outputs=[trade_out])
        trade_btn.click(perform_trade, inputs=[action, symbol, qty], outputs=[trade_out])
        
    with gr.Tab("Portfolio"):
        val = gr.Number(label="Total Value")
        pl = gr.Number(label="Profit/Loss")
        holdings = gr.JSON(label="Holdings")
        history = gr.Textbox(label="History")
        refresh = gr.Button("Refresh View")
        refresh.click(update_ui, outputs=[val, pl, holdings, history])

demo.launch()