# Project Plan

## Title
<!-- Give your project a short title. -->
Impact of Sector-Specific CO2 Emissions on Urban Air Quality in Luxembourg

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
How do sector-specific CO2 emissions from energy combustion influence urban air quality indicators?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project explores the relationship between CO2 emissions from various sectors, such as road and air transport, and their impact on urban air quality in Luxembourg. The study will utilize quarterly CO2 emissions data and annual air quality measurements to determine how emissions from specific sectors correlate with levels of urban pollutants like nitrogen oxides, sulfur dioxide, and particulate matter. This analysis will help identify which sectors are the most significant contributors to air pollution and provide data-driven insights to enhance air quality management and policy-making.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### 1. Quarterly CO2 Emissions from Energy Combustion
* Metadata URL: https://lustat.statec.lu/vis?lc=en&df[ds]=ds-release&df[id]=DF_A3200&df[ag]=LU1&df[vs]=1.1&pd=2015%2C2022&dq=A..&ly[rw]=SPECIFICATION%2CEU_NORM&ly[cl]=TIME_PERIOD&tm=Air%20quality&pg=0&vw=ov
* Data URL: https://lustat.statec.lu/vis?df[ds]=ds-release&df[id]=DF_A3207&df[ag]=LU1&df[vs]=1.0&lc=en&tm=Quarterly%20CO2%20emissions%20from%20energy%20combustion&pg=0&hc[dimensions]=Emissions&hc[Frequency]=Quarterly
* Data Type: CSV

Contains detailed data on CO2 emissions broken down by sectors such as road transport, air transport, and others, enabling the analysis of sector-specific impacts on air quality.


### 2. Annual Air Quality Data
* Metadata URL: 
* Data URL: https://lustat.statec.lu/vis?lc=en&df[ds]=ds-release&df[id]=DF_A3200&df[ag]=LU1&df[vs]=1.1&tm=Air%20quality&pg=0
* Data Type: CSV

Provides annual measurements of urban air pollutants, including sulfur dioxide, nitrogen oxides, and particulate matter, crucial for assessing the environmental impact of CO2 emissions.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->
1. **Issue #1: Data Collection and Preparation**
   - Download data from lustat.statec.lu for the relevant years and sectors.
   - Clean and preprocess the data to ensure accuracy and readiness for analysis.
   - Align the air quality data with the CO2 emissions data based on the time period and geographic relevance.

2. **Issue #2: Exploratory Data Analysis (EDA)**
   - Conduct preliminary analysis to understand the distribution and trends of both CO2 emissions and air pollutant levels.
   - Use visualizations to identify patterns and outliers in the datasets.

3. **Issue #3: Statistical Analysis and Modeling**
   - Employ regression analysis to determine the relationships between sector-specific CO2 emissions and various air pollutants.
   - Analyze the impact of seasonal variations and control for external factors such as weather conditions.

4. **Issue #4: Policy Impact Analysis**
   - Evaluate how current environmental policies are affecting sector-specific emissions and air quality.
   - Assess the effectiveness of existing regulations and identify sectors where further intervention is needed.

5. **Issue #5: Report Writing and Recommendations**
   - Compile the findings into a comprehensive report detailing the analysis, results, and methodological approaches.
   - Formulate policy recommendations based on the data to help local governments and environmental agencies target the most harmful sectors.



1. Example Issue [#1][i1]
2. ...

[i1]: https://github.com/jvalue/made-template/issues/1
