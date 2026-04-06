# 🍕 ZomatoInsights: Restaurant Analytics Pipeline

A comprehensive data engineering and analysis project that processes large-scale Zomato restaurant data to uncover consumer behavior and operational trends.

## 📊 Key Insights & Features
- **Automated Data Cleaning**: Handled mixed-type columns and cleaned un-named indices from raw CSV imports.
- **Currency Standardization**: Implemented a conversion layer to unify multi-currency (USD/INR) sales data into a single operational metric.
- **Demographic Profiling**: Visualized user distributions across Marital Status, Gender, and Family Size to identify core customer segments.
- **Age-Group Segmentation**: Categorized users into strategic age bins (16-20, 21-24, etc.) for targeted marketing analysis.

## 🛠 Tech Stack
- **Language**: Python
- **Libraries**: Pandas, Matplotlib, Seaborn
- **Environment**: Kaggle / Jupyter

## 📈 Analysis Workflow
1. **Ingestion**: Load multi-table datasets including `orders`, `users`, `menu`, and `restaurants`.
2. **Preprocessing**: Filter invalid sales (amounts <= 0) and resolve currency discrepancies.
3. **Visualization**: Generate distribution reports using grouped analysis and pie charts.
4. **Export**: Prepare grouped statistical summaries for business intelligence.

## 🗂 Dataset Attribution
The analysis is based on the [Zomato Restaurant Dataset](https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data) featuring comprehensive order history and user metadata.
