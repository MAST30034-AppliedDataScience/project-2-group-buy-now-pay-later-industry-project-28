# Raw Data
All relevant raw data are in the `data/tables` directory.

## Merchant Data Info
- Revenue Levels: `(a, b, c, d, e)` represents the level of revenue bands (unknown to groups). `a` denotes the smallest band whilst `e` denotes the highest revenue band.
- Take Rate: the fee charged by the BNPL firm to a merchant on a transaction. That is, for each transaction made, a certain percentage is taken by the BNPL firm.
- The dataset has been created to mimic a Salesforce data extract (i.e salespeople will type in tags and segments within a free-text field).
- As such, please be aware of small human errors when parsing the dataset.
- For Example, the tag field may have errors as they were manually input by employees.

## Transaction Data Info
- This is partitioned by the `order_datetime` field. For example, this means you just need to read the `transactions_20210228_20210828` directory, and it will treat the `order_datetime` directories as a partition column (or just another column you can take as is in layman terms).
- There is an underlying distribution with 10% random noise if groups would like to figure it out.
    - This is optional and not expected, though, groups may be able to better predict transaction rates if they find the correct distribution.
- There will be a delta file provided in week 2 representing the records with a fraud outcome.
- These are records that have been flagged and analysed by a Fraud Detection Model and can either be used as an additional feature i.e an `is_fraud` flag or records that can be deleted to keep the transactions data clean.


## Consumer Data Info
- The address field is fake and derived from USA street names. We have included it to mimic a more realistic dataset, but the streets themselves are non-existent and if there are any matches, it will be a pure coincidence.
- The postcode field is accurate and **should** be used for aggregated analysis for joining with other geospatial datasets for demographic information (i.e ABS datasets)
- There is roughly a uniform distribution at the state level (i.e number of consumers per state is the same for all states).

## User to Consumer ID Mapping Table
- Due to a difference between the internal system and a poor design choice (for some reason), the transaction tables use a surrogate key for each new `user_id`.
- However, the Consumer table has a unique ID (some are missing on purpose) field which will require some form of mapping between `consumer_id` to `user_id`.
- An additional mapping table has been provided to join the two datasets together.

## SA2 Information and Geometry

- This dataset provides the geometrical boundaries of the Statistical Area Level 2 (SA2) regions in Australia, as defined by the Australian Bureau of Statistics (ABS). It includes detailed shapefiles which represent the spatial boundaries of each SA2 region.
- Use these shapefiles for mapping and spatial analysis in GIS software (e.g., QGIS, ArcGIS) or for integration into spatial databases.

## SA2 Information and Postcode Lookup Table

- This dataset provides a lookup table that links SA2 regions with postcodes. It is useful for translating postcode information into SA2 regions and vice versa.
- Use this lookup table to match postcodes with their corresponding SA2 regions for analysis, reporting, and data enrichment purposes.

## Census Dataset - 2021 SA2 Data

- This dataset includes census data aggregated by SA2 regions. The data provides insights into various demographic and socio-economic characteristics, such as population, age distribution, employment, and education levels.

## Regional Population Dataset (2021-2022)

- This dataset includes annual population estimates for different regions across Australia, spanning from 2021 to 2022. It provides insights into population changes, distributions, and trends over time.

## Unemployment Rate Dataset

- This dataset provides unemployment rate data for different SA2 regions in Australia. The data is sourced from the Australian Bureau of Statistics (ABS) and includes various unemployment metrics for the year 2021.
