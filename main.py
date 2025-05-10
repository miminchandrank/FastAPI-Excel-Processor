from fastapi import FastAPI, Query, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from typing import Optional, List
import os
from app.excel_parser import ExcelParser

app = FastAPI()



excel_file_path = os.path.join("app", "Data", "capbudg.xls")  # Changed to .xlsx
excel_parser = ExcelParser(excel_file_path)

@app.get("/list_tables", response_model=dict)
async def list_tables():

    tables = excel_parser.get_sheet_names()
    return {"tables": tables}

@app.get("/get_table_details", response_model=dict)
async def get_table_details(table_name: str = Query(..., description="Name of the Excel sheet")):

    try:
        row_names = excel_parser.get_row_names(table_name)
        return {"table_name": table_name, "row_names": row_names}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/row_sum", response_model=dict)
async def calculate_row_sum(
    table_name: str = Query(..., description="Name of the Excel sheet"),
    row_name: str = Query(..., description="Row name to sum")
):

    try:
        row_sum = excel_parser.calculate_row_sum(table_name, row_name)
        return {
            "table_name": table_name,
            "row_name": row_name,
            "sum": row_sum
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))