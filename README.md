# 📊 CSV Insight

A lightweight Python CLI tool that generates a quick summary of a CSV dataset.

## Features

- Count rows and columns
- Detect missing values
- Identify numeric columns
- Calculate numeric averages
- No external dependencies

## Run

```bash
python main.py
```

## Example

```text
📊 CSV Insight
========================================

Enter CSV file path: sales.csv

📈 Dataset Summary
========================================

Rows       : 120
Columns    : 4

📋 Column Information:
- product: text | missing=0
- price: numeric | missing=2
  Average: 542.75
- quantity: numeric | missing=0
  Average: 18.43
- region: text | missing=1
```

## Built With

- Python
- CSV
- File handling
