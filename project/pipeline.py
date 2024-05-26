import requests
import pandas as pd
import os

api_url_1 = "https://lustat.statec.lu/rest/data/LU1,DF_A3207,1.0/.Q?startPeriod=2018-Q1&endPeriod=2022-Q4"
api_url_2 = "https://lustat.statec.lu/rest/data/LU1,DF_A3200,1.1/A..?startPeriod=2018&endPeriod=2022"

output_dir = os.path.expanduser("~/data")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_path_1 = os.path.join(output_dir, "co2_emissions_2018_2022.csv")
file_path_2 = os.path.join(output_dir, "air_quality_2018_2022.csv")

def download_csv(api_url, file_path):
    headers = {
        'Accept': 'application/vnd.sdmx.data+csv;urn=true;file=true;labels=both'
    }
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Check if the request was successful
    
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Data has been downloaded to {file_path}")

def process_emissions_data(file_path, output_path):
    df = pd.read_csv(file_path)
    
    # Split the 'DATAFLOW' column to extract relevant information, handling missing parts
    dataflow_split = df['DATAFLOW'].str.split(':', expand=True)
    dataflow_split = dataflow_split.reindex(columns=range(3), fill_value=None)
    df[['Region', 'Dataset', 'Version']] = dataflow_split
    df[['Dataset', 'Version']] = df['Dataset'].str.split('(', expand=True)
    df['Version'] = df['Version'].str.rstrip(')')
    
    # Split the 'EMISSIONS' column to extract emission types
    df[['Emission_Type', 'Emission_Type_Desc']] = df['EMISSIONS: Emissions'].str.split(': ', expand=True)
    
    # Organize and structure
    df = df[['Emission_Type_Desc', 'TIME_PERIOD: Time period', 'OBS_VALUE']]
    df_pivot = df.pivot(index='TIME_PERIOD: Time period', columns='Emission_Type_Desc', values='OBS_VALUE').reset_index()
    df_pivot.columns = ['Time_Period', 'Air transport', 'Others', 'Road transport', 'Total']
    df_pivot = df_pivot[['Time_Period', 'Total', 'Road transport', 'Air transport', 'Others']]
    
    # Calculate annual totals for 2018-2022, inserting info to the rows 2019-2022 and adding one more row for 2018
    df_pivot['Year'] = df_pivot['Time_Period'].str[:4]
    annual_totals = df_pivot.groupby('Year').sum().reset_index()
    total_2018 = annual_totals[annual_totals['Year'] == '2018']
    df_pivot = pd.concat([df_pivot, total_2018.assign(Time_Period='2018')])
    for year in range(2019, 2023):
        total_row = annual_totals[annual_totals['Year'] == str(year)]
        df_pivot.loc[df_pivot['Time_Period'] == str(year), ['Total', 'Road transport', 'Air transport', 'Others']] = total_row[['Total', 'Road transport', 'Air transport', 'Others']].values
    
    # Drop the 'Year' column
    df_pivot = df_pivot.drop(columns=['Year'])
    
    # Sort by Time_Period and save the processed DataFrame to a new CSV file
    df_pivot = df_pivot.sort_values(by='Time_Period').reset_index(drop=True)
    df_pivot.to_csv(output_path, index=False)
    print(f"Processed data has been saved to {output_path}")

def process_air_quality_data(file_path, output_path):
    df = pd.read_csv(file_path)
    
    # Organize and structure
    df.columns = df.columns.str.strip()
    df = df[['SPECIFICATION: Specification', 'EU_NORM: EU Norm', 'TIME_PERIOD: Time period', 'OBS_VALUE']]
    df.columns = ['Type_of_Pollution', 'EU_Norm', 'Year', 'Value']
    df_pivot = df.pivot_table(index=['Type_of_Pollution', 'EU_Norm'], columns='Year', values='Value', aggfunc='first').reset_index()
    df_pivot.columns = [str(col) if isinstance(col, int) else col for col in df_pivot.columns]
    df_pivot = df_pivot[['Type_of_Pollution', 'EU_Norm', '2018', '2019', '2020', '2021', '2022']]
    
    # Save the processed DataFrame to a new CSV file
    df_pivot.to_csv(output_path, index=False)
    print(f"Processed data has been saved to {output_path}")

def main():
    # Download datasets
    download_csv(api_url_1, file_path_1)
    download_csv(api_url_2, file_path_2)
    
    # Process the downloaded data
    processed_file_path_1 = os.path.join(output_dir, "processed_co2_emissions_2018_2022.csv")
    processed_file_path_2 = os.path.join(output_dir, "processed_air_quality_2018_2022.csv")
    
    process_emissions_data(file_path_1, processed_file_path_1)
    process_air_quality_data(file_path_2, processed_file_path_2)

if __name__ == "__main__":
    main()
