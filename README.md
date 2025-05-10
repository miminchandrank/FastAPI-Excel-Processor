# FastAPI Excel Processor

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/pandas-2.2.0-blue.svg?style=for-the-badge&logo=pandas)

A production-ready FastAPI application for processing Excel files with robust error handling and RESTful endpoints.

## Table of Contents
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Evaluation Criteria](#evaluation-criteria)
- [Potential Improvements](#potential-improvements)
- [Missed Edge Cases](#missed-edge-cases)
- [License](#license)

## Features
- ✅ Excel file processing (.xls format)
- ✅ REST API endpoints for data exploration
- ✅ Dynamic table/row validation
- ✅ Numerical sum calculations
- ✅ Comprehensive error handling
- ✅ Interactive API documentation

## API Endpoints

### Base URL
`http://localhost:9090`

### 1. List All Tables
**Endpoint**: `GET /list_tables`  
**Description**: Retrieve all sheet names from the Excel file  
**Response**:
```json
{
  "tables": ["Initial Investment", "Revenue Projections"]
}
