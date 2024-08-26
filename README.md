
# MAST30034 Project 1 README.md
- Name: Uma Barnes
- Student ID: 1277919


**Research Goal:** My research goal is to predict hourly rideshare vehicle demand 

**Timeline:** The timeline for the research area is 2018 - 2021.

To run the pipeline, please visit the `notebooks` directory and run the files in order:
1. `download.ipynb`: This downloads the raw data into the `data/landing` directory.
2. `tlc_preprocess.ipynb`: This notebook details all preprocessing steps for the TLC Data and outputs it to the `data/curated` directory.
3. `mta_preprocess.ipynb`: This notebook details all preprocessing steps for the MTA Service Alert Data and outputs it to the `data/curated` directory.
4. `weather_preprocess.ipynb`: This notebook details all preprocessing steps for the Weather Data and outputs it to the `data/curated` directory.
5. `EDA.ipynb`: This notebook is used to conduct analysis and creare visualisations on the curated data.
6. `model.ipynb`: The notebook is used to run and evaluate the model.
