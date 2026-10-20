
import csv

portfolio = []
total_invested = 0
total_value = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    print("\nStock", i + 1)
    ticker = input("Enter stock symbol: ").upper()
    buy_price = float(input("Enter buy price: "))
    quantity = int(input("Enter quantity: "))
    current_price = float(input("Enter current price: "))

    invested = buy_price * quantity
    value = current_price * quantity
    profit = value - invested
    percent = (profit / invested * 100) if invested else 0

    total_invested += invested
    total_value += value

    portfolio.append([
        ticker, buy_price, quantity, current_price,
        invested, value, profit, round(percent, 2)
    ])

print("\n===== PORTFOLIO SUMMARY =====")
for stock in portfolio:
    print(stock[0], "| Invested:", round(stock[4], 2),
          "| Current Value:", round(stock[5], 2),
          "| Profit/Loss:", round(stock[6], 2),
          "| Return:", stock[7], "%")

print("Total Invested:", round(total_invested, 2))
print("Total Value:", round(total_value, 2))
print("Total Profit/Loss:", round(total_value - total_invested, 2))

with open("portfolio_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Ticker", "Buy Price", "Quantity", "Current Price",
        "Invested", "Current Value", "Profit/Loss", "Return %"
    ])
    writer.writerows(portfolio)

print("\nCSV file created: portfolio_summary.csv")
