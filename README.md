# NYC Ride-Share Demand Analysis & Forecasting

**Author:** Uma Barnes  
**Contact:** [umacbarnes@gmail.com](mailto:umacbarnes@gmail.com) | 0427 097 021  
**GitHub:** [github.com/umabarnes](https://github.com/umabarnes)  
**LinkedIn:** [linkedin.com/in/uma-barnes](https://linkedin.com/in/uma-barnes)  


## Project Overview

This project analyzes and models ride-share demand across New York City’s boroughs, focusing on understanding the influence of weather, public transport reliability, and spatial factors on hourly ride-share usage. Leveraging extensive open datasets, the work applies advanced machine learning techniques - specifically Random Forest Regression and Linear Regression - to forecast demand patterns and inform sustainable urban transportation strategies.

The analysis aims to support decision-making around reducing traffic congestion and emissions by optimizing rideshare operations and enhancing public transport services. The insights align with broader goals of environmental sustainability and urban mobility efficiency, crucial areas for both public policy and business strategy.

## Motivation & Business Relevance

With increasing urbanization, understanding transportation demand is critical for cities to optimize infrastructure, reduce congestion, and minimize environmental impact. Ride-sharing services contribute significantly to traffic and emissions, especially when drivers spend time cruising for passengers.

This project provides actionable insights for:

- **Transportation planners** seeking to optimize public transit scheduling and capacity.  
- **Ride-share companies** aiming to improve driver routing and reduce unnecessary mileage.  
- **Policy makers** focused on promoting sustainable transport and reducing urban pollution.  

## Data Sources

- **New York City Taxi and Limousine Commission (TLC) Trip Records (2016+)**  
- **NYC Public Transport Ridership and Service Disruptions**  
- **Weather data for New York City (hourly and daily summaries)**  

Datasets were aggregated and cleaned to create a comprehensive view of ride-share demand influenced by external factors.


## Key Methods & Tools

- **Data Processing:** Python, Pandas, PySpark for handling large datasets  
- **Geospatial Analysis:** GeoPandas for mapping demand by borough and location  
- **Machine Learning:**  
  - Random Forest Regression (RFR) to capture non-linear demand relationships  
  - Linear Regression for baseline comparison and interpretability  
- **Visualization:** Matplotlib, Seaborn, and interactive maps to illustrate spatial and temporal demand patterns  


## Findings & Recommendations

- Random Forest Regression outperformed linear models, highlighting complex, non-linear interactions between demand and influencing factors.  
- Manhattan and Brooklyn show highly variable and high ride-share demand, indicating the need for increased public transit capacity and service during peak times.  
- Service disruptions on public transport strongly correlate with increased ride-share demand, underscoring the importance of reliable transit infrastructure.  
- Real-time demand forecasting can guide drivers to high-demand zones, reducing cruising time and emissions.  
- Enhancing last-mile connectivity and public transit accessibility can reduce dependence on ride-share vehicles.  


## How to Use This Repository

- **Data Preparation:** Scripts to download, clean, and aggregate TLC, transit, and weather data.  
- **Model Training:** Jupyter notebooks with implementation of Random Forest and Linear Regression models, including hyperparameter tuning and evaluation.  
- **Visualization:** Code for generating spatial and temporal demand maps and charts.  
- **Report:** Comprehensive project report in LaTeX summarizing methodology, analysis, and strategic recommendations.  


## Future Work

- Incorporate real-time traffic and event data for more dynamic forecasting.  
- Extend the model to predict demand during special events and holidays.  
- Explore deep learning methods for improved predictive accuracy.  


## Contact

For questions, collaborations, or feedback, please reach out via email or LinkedIn.


**Uma Barnes**  
Data Scientist
[umacbarnes@gmail.com](mailto:umacbarnes@gmail.com) | 0427 097 021  
[github.com/umabarnes](https://github.com/umabarnes) | [linkedin.com/in/uma-barnes](https://linkedin.com/in/uma-barnes)
