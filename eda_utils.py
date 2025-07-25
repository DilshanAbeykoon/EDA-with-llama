import pandas as pd

def generate_eda_prompt(df: pd.DataFrame) -> str:
    prompt = []

    # Dataset shape
    prompt.append(f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n")

    # Column names and types
    prompt.append("Columns and their data types:\n")
    for col in df.columns:
        prompt.append(f"- {col}: {df[col].dtype}\n")

    # Summary stats
    prompt.append("\nSummary statistics for numeric columns:\n")
    prompt.append(df.describe(include='all').to_string())

    # Missing values
    prompt.append("\n\nMissing values per column:\n")
    missing = df.isnull().sum()
    for col, count in missing.items():
        prompt.append(f"- {col}: {count} missing values\n")

    return ''.join(prompt)
