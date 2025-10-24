# 🌿 Herbal Products API ETL

A lightweight **Python ETL pipeline** that extracts product data from a public API, cleans it with `pandas`, and loads it into a SQL database.  
Designed and tested in **GitHub Codespaces**, this project demonstrates a practical, modern data engineering workflow.

---

## 🧩 Features

- ✅ Extracts live product data from a REST API (`dummyjson.com`)
- 🧼 Transforms and standardizes product fields (id, name, price, category)
- 💾 Loads the cleaned data into a SQL database (`SQLite`)
- 🧠 Includes a verification script to preview and validate loaded data
- ⚙️ Fully containerized and Codespaces-ready (via `.devcontainer`)

---

## 🧱 Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.11 |
| Libraries | `pandas`, `requests`, `sqlalchemy`, `loguru`, `python-dotenv` |
| Database | SQLite (easily switchable to PostgreSQL or Azure SQL) |
| Environment | GitHub Codespaces / VS Code Dev Container |

---

## 🚀 Quick Start

### 1️⃣ Open in GitHub Codespaces
Click **Code → Open with Codespaces** (or use your local VS Code with Dev Container support).

### 2️⃣ Set up environment
Copy `.env.example` to `.env` and make sure it contains:

```bash
API_URL=https://dummyjson.com/products
DB_URL=sqlite:///data/herbal_products.db
```

### 3️⃣ Install dependencies

(automatically handled by Codespaces, or manually run:)
```
pip install -r requirements.txt
```

### 4️⃣ Run the ETL
python src/main.py


Expected output:

2025-10-24 ... INFO - Starting Herbal Products ETL...
✅ Extracted 30 products from DummyJSON API
2025-10-24 ... INFO - Loaded 30 products into database.

### 🔍 Verify the Load

After running the ETL, you can inspect what’s in your database with:
```
python src/verify_load.py
```

Example output:

✅ Loaded 30 rows from database.
   id                      name   price         category
0   1  Essence Mascara Lash ...    9.99           beauty
1   2          Skin Beauty Kit   19.99           beauty
...

### 🧠 Project Structure
```
herbal-products-api-etl/
│
├── src/
│   ├── main.py             # ETL orchestrator
│   ├── extract.py          # Extract from API
│   ├── transform.py        # Clean & normalize data
│   ├── load.py             # Load into database
│   ├── verify_load.py      # Verify & preview loaded data
│   └── config.py           # Environment variables
│
├── data/
│   └── herbal_products.db  # SQLite database
│
├── requirements.txt
├── .env.example
├── .gitignore
└── .devcontainer/
    └── devcontainer.json
```

### 🧩 Future Enhancements

Add retry logic (tenacity) for API reliability

Integrate validation with pandera or great_expectations

Schedule ETL with Prefect or GitHub Actions

Extend to Azure Data Factory or Databricks for cloud deployment
