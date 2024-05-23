import os
import pandas as pd
import sqlite3

# Define input file paths
co2_file_path = "/project/co2-emissions.csv"
air_quality_file_path = "/project/air-quality.csv"

# Define output directory
output_dir = "/data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def transform_co2_data(file_path, db_path):
    df = pd.read_csv(file_path)
    
    # Drop unnecessary columns and rows
    df = df.drop(df.columns[[0, 2, 7]], axis=1)
    rows_to_drop = [0, 1, 2, 3, 9, 14, 19, 24, 29, 30]
    rows_to_drop = [row for row in rows_to_drop if row < len(df)]
    df = df.drop(rows_to_drop, axis=0).reset_index(drop=True)
    
    # Add new header row
    new_row = pd.DataFrame([["Time period", "Total emissions", "Road transport", "Air transport", "Others"]], columns=df.columns)
    df = pd.concat([new_row, df], ignore_index=True)
    
    # Replace with new data
    conn = sqlite3.connect(db_path)
    df.to_sql('co2_emissions', conn, if_exists='replace', index=False)
    conn.close()
    
    return df

def transform_air_quality_data(file_path, db_path):
    df = pd.read_csv(file_path, skiprows=2)
    
    # Drop unnecessary columns and rows
    columns_to_drop = [0, 3, 9]
    columns_to_drop = [col for col in columns_to_drop if col < len(df.columns)]
    df = df.drop(df.columns[columns_to_drop], axis=1)
    rows_to_drop = [0, 1, 2, 21, 22]
    rows_to_drop = [row for row in rows_to_drop if row < len(df)]
    df = df.drop(rows_to_drop, axis=0).reset_index(drop=True)
    
    # Add new header row
    new_row = pd.DataFrame([["Pollution", "EU Norm", "2018", "2019", "2020", "2021", "2022"]], columns=df.columns)
    df = pd.concat([new_row, df], ignore_index=True)
    
    # Replace with new data
    conn = sqlite3.connect(db_path)
    df.to_sql('air_quality', conn, if_exists='replace', index=False)
    conn.close()
    
    return df

def save_to_sqlite(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def main():
    # Transform datasets
    co2_df = transform_co2_data(co2_file_path, os.path.join(output_dir, "co2_emissions.db"))
    air_quality_df = transform_air_quality_data(air_quality_file_path, os.path.join(output_dir, "air_quality.db"))
    
    # Save datasets to SQLite databases
    save_to_sqlite(co2_df, os.path.join(output_dir, "co2_emissions.db"), "co2_emissions")
    save_to_sqlite(air_quality_df, os.path.join(output_dir, "air_quality.db"), "air_quality")

if __name__ == "__main__":
    main()
