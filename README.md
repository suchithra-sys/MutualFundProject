# Mutual Fund Analytics Platform

## Project Overview

This project is a Mutual Fund Analytics Platform developed as part of the Bluestock Fintech Capstone Project. The system analyzes mutual fund data, computes risk and performance metrics, and provides investment insights through interactive Power BI dashboards.

---

## Objectives

- Analyze mutual fund performance using historical NAV data.
- Calculate risk metrics such as VaR and CVaR.
- Evaluate fund performance using Alpha and Beta.
- Generate investment recommendations.
- Build interactive Power BI dashboards for decision-making.

---

## Technology Stack

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Jupyter Notebook
- Power BI

---

## Project Structure

BLUESTOCK_MF_CAPSTONE/

├── dashboard/
│   └── bluestock_mf.pbix
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── reports/
│   ├── charts/
│   ├── Bluestock_MF_Presentation.pptx
│   └── Final_Report.docx
│
├── scripts/
│   ├── clean_data.py
│   ├── clean_performance.py
│   ├── clean_transactions.py
│   ├── compute_metrics.py
│   ├── create_database.py
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── data_dictionary.md
├── requirements.txt
└── README.md
```

## Key Features

### Data Processing
- Data ingestion and cleaning
- Data validation
- SQLite database creation

### Performance Analytics
- Alpha Calculation
- Beta Calculation
- CAGR Analysis
- Sharpe Ratio Analysis

### Risk Analytics
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)

### Recommendation Engine
- Fund scoring model
- Investment recommendation system

### Dashboard Analytics
- Executive Overview Dashboard
- Fund Performance Dashboard
- Risk Analytics Dashboard
- Fund Recommendation Dashboard

---

## Dashboard Pages

### Page 1: Executive Overview
- Average VaR
- Average CVaR
- Total Funds
- Risk Summary Table

### Page 2: Fund Performance
- Alpha Analysis
- Beta Analysis
- Fund Performance Comparison

### Page 3: Risk Analytics
- VaR by Fund
- CVaR by Fund
- Risk Distribution Analysis

### Page 4: Fund Recommender
- Fund Ranking
- Recommendation Score
- Investment Insights

---

## Files Submitted

- Python Scripts (.py)
- Jupyter Notebooks (.ipynb)
- SQL Files (.sql)
- Power BI Dashboard (.pbix)
- Final Report (.docx/.pdf)
- Presentation (.pptx)

---

## Author

**Suchithra S**  
Intern ID:BFDA76968
Email Id:suchithra.s.work@gmail.com
Bluestock Fintech Capstone Project

---

## Conclusion

The project demonstrates end-to-end mutual fund analytics, risk assessment, performance evaluation, and dashboard visualization using Python, SQL, SQLite, and Power BI.