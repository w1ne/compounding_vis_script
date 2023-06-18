# README

## Investment Projection Script 

This Python program calculates and visualizes an investment strategy for achieving a given target amount. The program allows you to specify a principal amount, an interest rate, a monthly contribution, and a target value. It then calculates the projected growth of your investment over time and visualizes the results.

See [shylenko.com/Selling-options-strategy/](https://shylenko.com/Selling-options-strategy/) for more info.

### Prerequisites

The program uses the following Python libraries:

- pandas
- matplotlib

You can install them using pip:

```bash
pip install pandas matplotlib
```

### Running Instructions

To run the program, you can simply use the following command in your terminal:

```bash
python3 Compound_table.py
```

The output will be a table in the console indicating the projected value of your investment over time, as well as a plot visualizing this data.

### Parameters

You can adjust the following parameters at the end of the script to reflect your specific situation:

- `principal`: This is the initial amount of money you are investing.
- `rate`: This is the annual interest rate of your investment.
- `monthly_contribution`: This is the amount of money you plan to add to the investment each month.
- `target`: This is the target amount you want your investment to reach.

Example:
```python
principal = 5000
rate = 0.09
monthly_contribution = 1000
target = 1000000
```

### Output

The script will output a table and a plot:

1. Table: Displays the projection for each month until the target is reached. It includes columns for the month, the future value of the investment, the total amount of money you've contributed, and the percentages of the total investment that come from your contributions and the compounded returns.

2. Plot: Visualizes the growth of your investment, breaking down the total into the amount you've contributed and the returns from compound interest.

Please note that the time it takes to reach your target will depend on the values you provide for the principal, rate, monthly contribution, and target.
