# Generic Buy Now, Pay Later Project

**Group Number**: 28

**Group Members**:
- Yule Luo 1346472
- Delphine Ding 1353446 
- Hongyu He 1313969 
- Mengyue Zhang 1315635 
- Zhipeng Liu 1403778

**Research Goal:** Our research goal is to design a robust ranking system that enables a Buy Now, Pay Later (BNPL) firm to efficiently identify and prioritize the top 100 most reputable and reliable merchants overall, as well as the top 10 merchants within each segment for onboarding.

**Timeline:** 2021-02-28 to 2022-10-26

# To run the pipeline:

Firstly, please visit the `scripts` directory to see the file `0_Download_Data.py`: To download part of the raw data, first navigate to the `project-2-group-buy-now-pay-later-industry-project-28` folder in the terminal. Then, run the following command to save part of the raw data into the `data/tables` directory.
```bash
cd scripts && python 0_Download_Data.py
```
please note: 
- for the BNPL data: please donwnload data from LMS and drag to corresponding folders in `data/tables` directory
- for the unemployment dataset: please visit ABS Data Explorer on the website and click to download
- another README in `data` directory provides the general informaiton for all datasets used in this project.

Secondly, please visit the `notebook` folder and run the files in order:
1. `01_Preliminary_Analysis.ipynb`: This notebook involves the preliminary analysis and prepcocessing on all raw datasets individually.
2. `02_Feature_Engineering.ipynb`: This notebook focuses on creating new features through the aggregation of variables and analyzing missing value information.
3. `03_Data_Transformation.ipynb`: This notebook involves one-hot encoding for categorical variables.
4. `04_Imputation.ipynb`: This notebook impute missing values for consumer and merchant fraud probability.
5. `05_Transaction_Analysis.ipynb`: This notebook is used to conduct analysis on the transaction tables. 
6. `06_Classification.ipynb`: This notebook is used to split merchants into segments. 
7. `07_Interesting_Findings.ipynb`: This notebook is used to find merchants with particular characteristics.
8. `08_Modelling.ipynb`: This notebook is used to create Random Forest Classification and Gradient Boosted Trees models to predict whether the transaction is fraud in the future.
9. `09_Ranking.ipynb`: This notebook is used to create a ranking system to select top merchants. 
10. `10_Visualisation.ipynb`: This notebook is used to conduct analysis on the curated data. With Visualisations of the distribution of variables and relationships between the variables. 