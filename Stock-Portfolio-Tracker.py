import csv
import datetime

# --- Hardcoded stock prices (can be extended) ---
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "MSFT": 330,
    "META": 420,
}

# --- Function to display the header ---
def display_header():
    print("\n📈 STOCK PORTFOLIO TRACKER 📊")
    print("-" * 45)

# --- Function to get user portfolio ---
def get_portfolio():
    portfolio = {}
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("❌ Stock not found. Available stocks:", ", ".join(STOCK_PRICES.keys()))
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity <= 0:
                print("⚠️ Quantity must be a positive integer.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")
    return portfolio

# --- Function to calculate and display portfolio summary ---
def display_summary(portfolio):
    print("\n🧾 Portfolio Summary:")
    print(f"{'Stock':<10}{'Quantity':<10}{'Price ($)':<12}{'Total Value ($)':<15}")
    print("-" * 45)

    total_investment = 0
    rows = []

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        total_value = price * quantity
        total_investment += total_value
        rows.append([stock, quantity, price, total_value])
        print(f"{stock:<10}{quantity:<10}{price:<12}{total_value:<15}")

    print("-" * 45)
    print(f"{'TOTAL':<32}${total_investment}")

    return rows, total_investment

# --- Function to save portfolio to CSV ---
def save_to_csv(rows, total_investment):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"portfolio_{timestamp}.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        writer.writerows(rows)
        writer.writerow([])
        writer.writerow(["", "", "Total Investment", total_investment])
    
    print(f"\n✅ Portfolio saved to file: {filename}")

# --- Main program ---
def main():
    display_header()
    portfolio = get_portfolio()

    if not portfolio:
        print("📭 No stocks entered. Exiting.")
        return

    rows, total = display_summary(portfolio)

    save = input("\n💾 Do you want to save this portfolio to a CSV file? (yes/no): ").lower()
    if save == "yes":
        save_to_csv(rows, total)
    else:
        print("📌 Portfolio not saved.")

# --- Run the program ---
if __name__ == "__main__":
    main()
