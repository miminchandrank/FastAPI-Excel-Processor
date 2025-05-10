import pandas as pd
from typing import List


class ExcelParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.sheets = pd.ExcelFile(file_path).sheet_names

    def get_sheet_names(self) -> List[str]:

        return self.sheets

    def get_row_names(self, sheet_name: str) -> List[str]:

        if sheet_name not in self.sheets:
            raise ValueError(f"Table '{sheet_name}' not found.")

        df = pd.read_excel(self.file_path, sheet_name=sheet_name)
        if df.empty:
            return []

        first_column = df.iloc[:, 0].dropna().astype(str).tolist()
        return first_column

    def calculate_row_sum(self, sheet_name: str, row_name: str) -> float:

        if sheet_name not in self.sheets:
            raise ValueError(f"Table '{sheet_name}' not found.")

        df = pd.read_excel(self.file_path, sheet_name=sheet_name)
        if df.empty:
            raise ValueError(f"Table '{sheet_name}' is empty.")


        matching_rows = df[df.iloc[:, 0].astype(str).str.strip() == row_name.strip()]
        if matching_rows.empty:
            raise ValueError(f"Row '{row_name}' not found in table '{sheet_name}'.")


        row_data = matching_rows.iloc[0, 1:].dropna()
        numeric_values = pd.to_numeric(row_data, errors='coerce').dropna()

        if numeric_values.empty:
            raise ValueError(f"No numerical data found in row '{row_name}'.")

        return float(numeric_values.sum())