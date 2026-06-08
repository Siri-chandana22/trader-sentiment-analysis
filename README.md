# Trader Performance vs Bitcoin Sentiment

## Project Overview
This project analyzes the relationship between **trader performance** and **Bitcoin market sentiment**.  
By combining **Hyperliquid trading data** with the **Bitcoin Fear & Greed Index**, the study uncovers behavioral patterns and provides insights that can guide smarter trading strategies.

## Datasets
- [Historical Trader Data](https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing)  
- [Bitcoin Fear & Greed Index](https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing)

## Requirements
Install the following Python libraries before running the notebook:

```bash
pip install pandas numpy matplotlib seaborn
```

## Key Features

- Data cleaning and preprocessing of trader and sentiment datasets

- Merging datasets on Date for aligned analysis

- Statistical summaries of PnL by sentiment classification

- Visualizations:

  - Trade counts by sentiment

  - Mean and median PnL comparisons

  - Boxplots of PnL distribution

  - Win rate analysis

  - Correlation heatmap (PnL, Fee, Trade Size)

  - Leverage usage by sentiment

  - Buy vs Sell activity split

- Identification of top profitable and losing traders

- Trading volume analysis by sentiment

## Insights
- Highest mean profit occurred during Greed sentiment.

- Most trading activity occurred during Fear sentiment.

- Leverage usage tends to be riskier in Fear markets.

- BTC trades show stronger correlation with sentiment shifts compared to altcoins.

## Conclusion

Trader behavior is strongly influenced by market sentiment.The findings highlight opportunities for risk management and strategy optimization, showing that sentiment data can be a valuable input for trading decisions.

## Sample Outputs

![Mean Closed PnL by Sentiment](<img width="1032" height="557" alt="Image" src="https://github.com/user-attachments/assets/187e3e80-50dc-4658-b3f8-680f77b4ed76" />)

![Trade Counts by Sentiment](<img width="1272" height="558" alt="Image" src="https://github.com/user-attachments/assets/1b9a51df-5307-4b15-bbc0-39797a599e0b" />)
