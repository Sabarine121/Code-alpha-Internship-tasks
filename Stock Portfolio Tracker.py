import csv

stock_prices = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOG": 2700.0,
    "MSFT": 310.0
}

def get_portfolio():
    portfolio = {}
    print("Enter your stock holdings. Leave ticker blank to finish.")
    while True:
        ticker = input("Ticker (e.g. AAPL): ").strip().upper()
        if not ticker:
            break
        if ticker not in stock_prices:
            print(f"Unknown ticker. Known tickers: {', '.join(stock_prices.keys())}")
            continue
        try:
            qty = float(input(f"Quantity of {ticker}: ").strip())
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
        portfolio[ticker] = portfolio.get(ticker, 0) + qty
    return portfolio

def calculate_total(portfolio):
    total = 0.0
    print("\nYour portfolio breakdown:")
    for ticker, qty in portfolio.items():
        price = stock_prices[ticker]
        value = price * qty
        print(f"  {ticker}: {qty} shares × ${price:.2f} = ${value:.2f}")
        total += value
    print(f"\nTotal investment value: ${total:.2f}")
    return total

def save_to_file(portfolio, total):
    choice = input("Save results? (y/n): ").strip().lower()
    if choice != 'y':
        return
    filename = input("Enter filename (e.g. portfolio.csv or portfolio.txt): ").strip()
    if filename.endswith(".csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Ticker", "Quantity", "Price", "Value"])
            for ticker, qty in portfolio.items():
                price = stock_prices[ticker]
                writer.writerow([ticker, qty, price, price * qty])
            writer.writerow([])
            writer.writerow(["", "", "Total", total])
    else:
        with open(filename, "w") as f:
            f.write("Ticker\tQuantity\tPrice\tValue\n")
            for ticker, qty in portfolio.items():
                price = stock_prices[ticker]
                f.write(f"{ticker}\t{qty}\t{price:.2f}\t{price * qty:.2f}\n")
            f.write(f"\nTotal investment value:\t${total:.2f}\n")
    print(f"Results saved to {filename}")

def main():
    portfolio = get_portfolio()
    if not portfolio:
        print("No holdings entered. Exiting.")
        return
    total = calculate_total(portfolio)
    save_to_file(portfolio, total)

if __name__ == "__main__":
    main()