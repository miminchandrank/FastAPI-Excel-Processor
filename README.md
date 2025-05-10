# FastAPI Excel Processor

## Project Overview
A REST API built with FastAPI that processes Excel files, providing endpoints to extract and analyze data from specified tables. The application reads from `capbudg.xls` and exposes structured endpoints for table exploration and data calculation.

## API Endpoints
Base URL: `http://localhost:9090`

### 1. List All Tables
**Endpoint**: `GET /list_tables`  
**Description**: Returns all sheet names from the Excel file  
**Example Response**:
```json
{
  "tables": ["Initial Investment", "Revenue Projections", "Operating Expenses"]
}
