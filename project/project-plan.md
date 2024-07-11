# Project Plan

## Title
<!-- Give your project a short title. -->
Impact of Sector-Specific CO2 Emissions on Urban Air Quality in Luxembourg

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
How do sector-specific CO2 emissions from energy combustion influence urban air quality indicators in Luxembourg?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project explores the relationship between CO2 emissions from various sectors, such as road and air transport, and their impact on urban air quality in Luxembourg. The study will utilize quarterly CO2 emissions data and annual air quality measurements to determine how emissions from specific sectors correlate with levels of urban pollutants like nitrogen oxides, sulfur dioxide, and particulate matter. This analysis will help identify which sectors are the most significant contributors to air pollution and provide data-driven insights to enhance air quality management and policy-making.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### 1. Quarterly CO2 Emissions from Energy Combustion
* Metadata URL: https://lustat.statec.lu/vis?df[ds]=ds-release&df[id]=DF_A3207&df[ag]=LU1&df[vs]=1.0&vw=ov&pd=2015-Q1%2C2023-Q4&dq=.Q&ly[rw]=TIME_PERIOD&ly[cl]=EMISSIONS&lc=en&tm=Quarterly%20CO2%20emissions%20from%20energy%20combustion&pg=0&hc[dimensions]=Emissions&hc[Frequency]=Quarterly
* Data URL: https://lustat.statec.lu/vis?df[ds]=ds-release&df[id]=DF_A3207&df[ag]=LU1&df[vs]=1.0&vw=tb&pd=2015-Q1%2C2023-Q4&dq=.Q&ly[rw]=TIME_PERIOD&ly[cl]=EMISSIONS&lc=en&tm=Quarterly%20CO2%20emissions%20from%20energy%20combustion&pg=0&hc[dimensions]=Emissions&hc[Frequency]=Quarterly
* Data Type: CSV

Contains detailed data on CO2 emissions broken down by sectors such as road transport, air transport, and others, enabling the analysis of sector-specific impacts on air quality in Luxembourg.


### 2. Annual Air Quality Data
* Metadata URL: https://lustat.statec.lu/vis?lc=en&df[ds]=ds-release&df[id]=DF_A3200&df[ag]=LU1&df[vs]=1.1&pd=2015%2C2022&dq=A..&ly[rw]=SPECIFICATION%2CEU_NORM&ly[cl]=TIME_PERIOD&tm=Air%20quality&pg=0&vw=ov
* Data URL: https://lustat.statec.lu/vis?lc=en&df[ds]=ds-release&df[id]=DF_A3200&df[ag]=LU1&df[vs]=1.1&tm=Air%20quality&pg=0&pd=2015%2C2022&dq=A..&ly[rw]=SPECIFICATION%2CEU_NORM&ly[cl]=TIME_PERIOD
* Data Type: CSV

Provides annual measurements of urban air pollutants, including sulfur dioxide, nitrogen oxides, and particulate matter, crucial for assessing the environmental impact of CO2 emissions in Luxembourg.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->
1. **Issue #1: Data Collection and Preparation** [#1][i1]

2. **Issue #2: Exploratory Data Analysis (EDA)** [#2][i2]

3. **Issue #5: Report Writing and Recommendations** [#3][i3]
  

[i1]: https://github.com/khharlamova/fau-made/issues/1
[i2]: https://github.com/khharlamova/fau-made/issues/2
[i3]: https://github.com/khharlamova/fau-made/issues/5




