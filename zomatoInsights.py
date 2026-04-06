import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ZomatoDataEngine:
    """
    A professional data processing engine for Zomato restaurant datasets.
    """
    def __init__(self, data_paths):
        self.data_paths = data_paths
        self.dfs = {}

    def load_and_clean(self):
        # Load all datasets
        for name, path in self.data_paths.items():
            self.dfs[name] = pd.read_csv(path)
        
        # Specific cleaning logic from original notebook
        orders = self.dfs['orders']
        orders = orders[orders["sales_amount"] > 0]
        orders.drop(["Unnamed: 0"], axis=1, errors='ignore', inplace=True)
        
        # Optimized currency conversion
        def standardize_currency(row):
            if row["currency"] == "USD":
                row["sales_amount"] *= 80.0
                row["currency"] = "INR"
            elif "INR" in str(row["currency"]):
                row["currency"] = "INR"
            return row

        self.dfs['orders'] = orders.apply(standardize_currency, axis=1)
        return self.dfs

    def generate_demographics_report(self):
        """
        Generates visual insights for user demographics.
        """
        users = self.dfs['users']
        sns.set_theme(style="whitegrid")
        
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # Gender Distribution
        users['Gender'].value_counts().plot.pie(
            autopct='%1.1f%%', ax=axes[0], cmap='Pastel1', title='User Gender split'
        )
        
        # Marital Status
        users['Marital Status'].value_counts().plot.pie(
            autopct='%1.1f%%', ax=axes[1], cmap='Pastel2', title='Marital Status'
        )
        
        plt.tight_layout()
        plt.show()

# Usage
paths = {
    'orders': "/kaggle/input/zomato-database/orders.csv",
    'users': "/kaggle/input/zomato-database/users.csv",
    'restaurants': "/kaggle/input/zomato-database/restaurant.csv"
}

engine = ZomatoDataEngine(paths)
engine.load_and_clean()
engine.generate_demographics_report()