# Analysis of Trader Performance vs Bitcoin Sentiment

# 1. LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# 2. LOAD DATA
trader_df = pd.read_csv("historical_data.csv")
sentiment_df = pd.read_csv("fear_greed_index.csv")

print("Trader Data Shape:", trader_df.shape)
print("Sentiment Data Shape:", sentiment_df.shape)

# 3. Initial Check
print("\nTrader Columns:")
print(trader_df.columns)

print("\nSentiment Columns:")
print(sentiment_df.columns)

# 4. CLEANING
# Clean column names
trader_df.columns = trader_df.columns.str.strip()
sentiment_df.columns = sentiment_df.columns.str.strip()

# Convert Timestamp to Daily Date
if "Timestamp IST" in trader_df.columns:
    trader_df["Date"] = pd.to_datetime(trader_df["Timestamp IST"], format="%d-%m-%Y %H:%M", errors="coerce").dt.date
elif "time" in trader_df.columns:
    trader_df["Date"] = pd.to_datetime(trader_df["time"], errors="coerce").dt.date

# Convert Sentiment data
sentiment_df["Date"] = pd.to_datetime(sentiment_df["date"], errors="coerce").dt.date

# Drop roes with missing dates
trader_df = trader_df.dropna(subset=["Date"])
sentiment_df = sentiment_df.dropna(subset=["Date"])

print("\nData Cleaning Done")

# 5. MERGE
combined = pd.merge(trader_df, sentiment_df, on="Date", how="inner")

print("\nCombined Shape:", combined.shape)
print(combined.head())

# 6. SUMMARY STATS
stats = combined.groupby("classification")["Closed PnL"].agg(["count", "mean", "median", "std", "min", "max"])
print("\nPnL Summary by Sentiment")
print(stats)

# 7. TRADE COUNTS
plt.figure(figsize=(8,5))
sns.countplot(data=combined, x="classification", order=combined["classification"].value_counts().index)
plt.title("No. of Trades by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("No. of Trades")
plt.show()

# 8. MEAN PNL
mean_pnl = combined.groupby("classification")["Closed PnL"].mean().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(data=mean_pnl, x="classification", y="Closed PnL")
plt.title("Mean Closed PnL by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Mean PnL")
plt.show()

# 9. MEDIAN PNL
median_pnl = combined.groupby("classification")["Closed PnL"].median().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(data=median_pnl, x="classification", y="Closed PnL")
plt.title("Median Closed PnL by Sentiment")
plt.show()

# 10. PNL DISTRIBUTION
plt.figure(figsize=(10,6))
sns.boxplot(data=combined, x="classification", y="Closed PnL")
plt.ylim(-1000, 1000)
plt.title("PnL Distribution by Sentiment")
plt.show()

# 11. WIN RATE
combined["WinFlag"] = combined["Closed PnL"] > 0
win_rate = combined.groupby("classification")["WinFlag"].mean() * 100
print("\nWin Rate (%)")
print(win_rate)

plt.figure(figsize=(8,5))
win_rate.plot(kind="bar")
plt.title("Win Rate by Sentiment")
plt.ylabel("Win Rate (%)")
plt.show()

# 12. COORELATION
corr_data = combined[["Closed PnL", "Fee", "Size USD"]].corr()
plt.figure(figsize=(6,5))
sns.heatmap(corr_data, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# 13. LEVERAGE
if "leverage" in combined.columns:
    lev_stats = combined.groupby("classification")["leverage"].mean()
    print("\nAverage Leverage")
    print(lev_stats)

# 14. TOP TRADERS
top_traders = combined.groupby("Account")["Closed PnL"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Traders")
print(top_traders)

plt.figure(figsize=(12,5))
top_traders.plot(kind="bar")
plt.title("Top 10 Traders by Total Profit")
plt.ylabel("Total Closed PnL")
plt.show()

# 15. TOP LOSING TRADERS
bottom_traders = combined.groupby("Account")["Closed PnL"].sum().sort_values().head(10)
print("\nTop 10 Losing Traders")
print(bottom_traders)

# 16. TRADING VOLUME
volumes = combined.groupby("classification")["Size USD"].sum()
print("\nVolume by Sentiment")
print(volumes)

plt.figure(figsize=(8,5))
volume.plot(kind="bar")
plt.title("Trading Volume by Sentiment")
plt.ylabel("Volume (USD)")
plt.show()

# 17. BUY VS SELL ANALYSIS
plt.figure(figsize=(8,5))
sns.countplot(data=combined, x="classification", hue="Side")
plt.title("Buy vs Sell by Sentiment")
plt.show()

# Profit Summary
profit_summary = combined.groupby('classification').agg(
    Total_Profit=('Closed PnL','sum'),
    Avg_Profit=('Closed PnL','mean'),
    Trade_count=('Closed PnL','count')
)
print(profit_summary)

# 18. INSIGHTS
print("\n========== KEY INSIGHTS ==========")
highest_pnl = mean_pnl.sort_values(by="Closed PnL", ascending=False).iloc[0]
print(f"Highest mean profit occurred during {highest_pnl['classification']} sentiment.")

highest_activity = combined["classification"].value_counts().idxmax()
print(f"Highest trading activity occurred during {highest_activity} sentiment.")

print("\nAnalysis Completed Successfully.")
