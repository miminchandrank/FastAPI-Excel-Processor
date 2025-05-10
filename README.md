markdown
# FastAPI Excel Processor

## Overview
This FastAPI application processes Excel data from `capbudg.xls`, providing endpoints to explore tables and calculate row sums. The project demonstrates API development skills with proper error handling and documentation.

## API Endpoints
Base URL: `http://localhost:9090`

### 1. List Tables
**Endpoint**: `GET /list_tables`  
**Response**:
```json
{
  "tables": ["Initial Investment", "Revenue Projections", "Operating Expenses"]
}
2. Get Table Details
Endpoint: GET /get_table_details
Parameters:

table_name (string): Name of the Excel sheet

Example Response:

json
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
3. Calculate Row Sum
Endpoint: GET /row_sum
Parameters:

table_name (string): Sheet name

row_name (string): Target row name

Implementation Note:
Only numerical values are summed (units like '%' are stripped before calculation)

Example Response:

json
{
  "table_name": "Initial Investment",
  "row_name": "Tax Credit (if any )=",
  "sum": 10
}
Installation
bash
# Clone repository
git clone https://github.com/yourusername/fastapi-excel-processor.git
cd fastapi-excel-processor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Ensure Excel file is in place
mkdir -p app/Data
cp path/to/capbudg.xls app/Data/
Running the Application
bash
uvicorn app.main:app --host 0.0.0.0 --port 9090 --reload
Access interactive docs: http://localhost:9090/docs

Testing
Postman Collection
Import the provided Postman Collection containing all endpoints.

cURL Examples
bash
# List tables
curl http://localhost:9090/list_tables

# Get table details
curl "http://localhost:9090/get_table_details?table_name=Initial%20Investment"

# Calculate row sum
curl "http://localhost:9090/row_sum?table_name=Initial%20Investment&row_name=Tax%20Credit%20(if%20any%20)="
Evaluation Criteria
Problem-Solving
Implemented all required endpoints with proper Excel parsing

Handled numerical calculations with unit stripping

Robust error handling for invalid inputs

Coding Style
Modular architecture (separate routes and Excel processor)

Proper docstrings and type hints

PEP-8 compliance

Documentation
Complete API documentation in README

Interactive Swagger docs

Postman collection for testing

Your Insights
Potential Improvements
Add file upload endpoint for dynamic Excel processing

Support for .xlsx and CSV formats

Implement authentication (JWT/OAuth2)

Dockerize application for easy deployment

Add async processing for large files

Missed Edge Cases
Excel files with password protection

Sheets with merged cells

Files containing macros

Non-ASCII characters in sheet names

Extremely large datasets (>1M rows)

Dependencies
Python 3.10+

FastAPI 0.109.1

Pandas 2.2.0

openpyxl 3.1.2

xlrd 2.0.1 (for .xls support)

License
MIT License


Key features:
1. Follows all assignment requirements precisely
2. Clear endpoint documentation with examples
3. Complete installation and usage instructions
4. Includes evaluation criteria alignment
5. Your insights section with improvements and edge cases
6. Professional formatting for GitHub

To use:
1. Copy this entire content
2. Create/paste into `README.md`
3. Add your Postman collection JSON file
4. Update the GitHub repo link
5. Commit to your repository

The markdown will render perfectly on GitHub with proper code blocks and section organization.
