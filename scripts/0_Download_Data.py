import os
import requests
from zipfile import ZipFile

# Function to download and extract ZIP files
def download_and_extract_zip(url, zip_file_path, extracted_dir):
    # Create the output and extraction directories if they don't exist
    os.makedirs(extracted_dir, exist_ok=True)

    # Download the ZIP file
    response = requests.get(url)
    if response.status_code == 200:
        # Save the ZIP file to disk
        with open(zip_file_path, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully and saved to {zip_file_path}")

        # Extract the ZIP file to the specific directory
        try:
            with ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extracted_dir)
            print(f"Files extracted successfully to {extracted_dir}")

            # Delete the ZIP file after extraction
            os.remove(zip_file_path)
            print(f"ZIP file deleted: {zip_file_path}")
        except Exception as e:
            print(f"Error extracting ZIP file: {e}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

# Create directories for Project-2-BNPL-Tables
for i in range(1, 5):
    path = f'../data/tables/tables {i}'
    os.makedirs(path, exist_ok=True)

# Download and extract SA2 information and its geometry
url_sa2_geometry = 'https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip'
zip_file_path_sa2_geometry = '../data/tables/SA2_2021_AUST_SHP_GDA2020.zip'
extracted_dir_sa2_geometry = '../data/tables/SA2_2021_AUST_SHP_GDA2020'
download_and_extract_zip(url_sa2_geometry, zip_file_path_sa2_geometry, extracted_dir_sa2_geometry)

# Download and extract SA2 information and postcode lookup table
url_asgs = 'https://data.gov.au/data/dataset/6cd8989d-4aca-46b7-b93e-77befcffa0b6/resource/cb659d81-5bd2-41f5-a3d0-67257c9a5893/download/asgs2021codingindexs.zip'
zip_file_path_asgs = '../data/tables/asgs2021codingindexs.zip'
extracted_dir_asgs = '../data/tables/asgs2021codingindexs'
download_and_extract_zip(url_asgs, zip_file_path_asgs, extracted_dir_asgs)

# Download and extract Census dataset
url_census = 'https://www.abs.gov.au/census/find-census-data/datapacks/download/2021_GCP_SA2_for_AUS_short-header.zip'
zip_file_path_census = '../data/tables/2021_GCP_SA2_for_AUS_short-header.zip'
extracted_dir_census = '../data/tables/2021_GCP_SA2_for_AUS_short-header'
download_and_extract_zip(url_census, zip_file_path_census, extracted_dir_census)

# Download Population dataset
url_population = 'https://www.abs.gov.au/statistics/people/population/regional-population/2021-22/32180DS0003_2001-22r.xlsx'
output_dir_population = '../data/tables/'
excel_file_path_population = os.path.join(output_dir_population, '32180DS0003_2001-22r.xlsx')

# Create the output directory if it doesn't exist
os.makedirs(output_dir_population, exist_ok=True)

# Download the Excel file
response_population = requests.get(url_population)
if response_population.status_code == 200:
    with open(excel_file_path_population, 'wb') as f:
        f.write(response_population.content)
    print(f"File downloaded successfully and saved to {excel_file_path_population}")
else:
    print(f"Failed to download the file. Status code: {response_population.status_code}")

# Note: For the unemployment dataset, manual download is required
print("The unemployment dataset does not have a direct download link. Please visit ABS Data Explorer on the website and click to download.")
