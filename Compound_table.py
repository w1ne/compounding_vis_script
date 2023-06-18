import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def future_value(principal, rate, months, monthly_contribution):
    fv = principal * (1 + rate / 12) ** months + monthly_contribution * (((1 + rate / 12) ** months - 1) / (rate / 12))
    return fv

def investment_table(principal, rate, monthly_contribution, target):
    data = []
    months = 0
    total_contributions = principal

    while True:
        future_val = future_value(principal, rate, months, monthly_contribution)
        compounded_returns_pct = (future_val - total_contributions) / future_val * 100
        savings_pct = total_contributions / future_val * 100

        data.append([months, future_val, total_contributions, compounded_returns_pct, savings_pct])

        if future_val >= target:
            break

        months += 1
        total_contributions += monthly_contribution

    df = pd.DataFrame(data, columns=['Month', 'Future Value', 'Total Contributions', '% Compounded Returns', '% Savings'])
    return df

def plot_growth(table):
    fig, ax = plt.subplots()

    ax.fill_between(table['Month'], 0, table['Total Contributions'], color='blue', alpha=0.3, label='Savings')
    ax.fill_between(table['Month'], table['Total Contributions'], table['Future Value'], color='orange', alpha=0.3, label='Compounded Returns')

    ax.plot(table['Month'], table['Future Value'], label='Total Investment', color='red')
    ax.plot(table['Month'], table['Total Contributions'], label='Total Contributions', color='blue')

    ax.set_xlabel('Month')
    ax.set_ylabel('Value')
    ax.set_title('Investment Growth: Savings vs Compounded Returns')
    ax.legend()
    
    # Format y-axis to show USD with comma separator
    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    plt.gca().yaxis.set_major_formatter(tick)

    plt.show()

principal = 5000
rate = 0.09
monthly_contribution = 1000
target = 1000000

table = investment_table(principal, rate, monthly_contribution, target)
print(table)


plot_growth(table)
