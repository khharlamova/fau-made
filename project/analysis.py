import pandas as pd
import matplotlib.pyplot as plt

# Load data
co2_df = pd.read_csv('processed_co2_emissions_2018_2022.csv')
air_quality_df = pd.read_csv('processed_air_quality_2018_2022.csv')

# Filter CO2 data to include only annual results
annual_co2_df = co2_df[co2_df['Time_Period'].str.match(r'^\d{4}$')]

# Plot CO2 emissions by sector (2018-2022)
plt.figure(figsize=(10, 6))
for sector in ['Total', 'Road transport', 'Air transport', 'Others']:
    plt.plot(annual_co2_df['Time_Period'], annual_co2_df[sector], label=sector)
plt.xlabel('Year')
plt.ylabel('CO2 Emissions')
plt.title('CO2 Emissions by Sector (2018-2022)')
plt.legend()
plt.savefig('co2_emissions_by_sector.png')
plt.show()

# Plot annual average pollutant levels (2018-2022)
plt.figure(figsize=(10, 6))
for pollutant in air_quality_df['Type_of_Pollution']:
    plt.plot(air_quality_df.columns[2:], air_quality_df.loc[air_quality_df['Type_of_Pollution'] == pollutant].iloc[0, 2:], label=pollutant)
plt.xlabel('Year')
plt.ylabel('Pollutant Levels')
plt.title('Annual Average Pollutant Levels (2018-2022)')
plt.legend()
plt.savefig('annual_avg_pollutant_levels.png')
plt.show()

# Create summary statistics table
summary_stats = pd.DataFrame({
    'CO2 Emissions (Mean)': annual_co2_df[['Total', 'Road transport', 'Air transport', 'Others']].mean(),
    'Pollutant Levels (Mean)': air_quality_df.set_index('Type_of_Pollution').loc[:, '2018':'2022'].mean(axis=1)
})
summary_stats.to_csv('summary_statistics.csv')
