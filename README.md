# FastAPI Excel Processor

This FastAPI project allows users to process an Excel file (`capbudg.xls`) and interact with its contents through a set of API endpoints. The application supports table listing, row extraction, and numerical summation for specified rows.

---

## 🚀 Project Overview

This API is built using **FastAPI** and is designed to:

1. **Read and parse** data from a given Excel file.
2. **Expose API endpoints** to list tables, show row details, and compute row-wise numerical sums.

Base URL: `http://localhost:9090`

### Run the API server

```bash
uvicorn main:app --host 127.0.0.1 --port 9090
```

---

## 📌 API Endpoints

### ✅ GET /list\_tables

Returns the names of all sheets (treated as "tables") in the Excel file.

#### Response:

```json
{
  "tables": [
    "Initial Investment",
    "Revenue Projections",
    "Operating Expenses"
  ]
}
```

---

### ✅ GET /get\_table\_details?table\_name={name}

Returns the list of row names (first column values) from a given sheet.

#### Example Request:

```
GET /get_table_details?table_name=Initial Investment
```

#### Response:

```json
{
  "table_name": "Initial Investment",
  "row_names": [
    "Initial Investment=",
    "Opportunity cost (if any)=",
    "Lifetime of the investment",
    "Salvage Value at end of project=",
    "Deprec. method(1:St.line;2:DDB)=",
    "Tax Credit (if any )=",
    "Other invest.(non-depreciable)="
  ]
}
```

---

### ✅ GET /row\_sum?table\_name={name}\&row\_name={row}

Calculates and returns the sum of all numeric values in the given row.

#### Example Request:

```
GET /row_sum?table_name=Initial Investment&row_name=Tax Credit (if any )=
```

#### Response:

```json
{
  "table_name": "Initial Investment",
  "row_name": "Tax Credit (if any )=",
  "sum": 10.0
}
```

> Note: Only numeric values in the row are summed. Percentage symbols or text are ignored using `pandas.to_numeric(errors='coerce')`.

---

## 🧪 Postman Collection

A ready-to-use Postman collection is included in the repo to test the API endpoints.

To import:

* Open Postman
* Click on Import
* Paste or upload `postman.json`
* Set base URL to `http://localhost:9090`


### ⚠️ Missed Edge Cases

* Empty sheets with no data.
* Tables where all values are non-numeric (returns an error).
* Row names with invisible whitespaces or encoding issues.
* Malformed Excel file structure.

---

## ✅ Testing

Postman base URL: `http://localhost:9090`

Endpoints:

* `/list_tables`
* `/get_table_details?table_name=...`
* `/row_sum?table_name=...&row_name=...`

---

## 📝 Author

Developed by - Miminchandran K
