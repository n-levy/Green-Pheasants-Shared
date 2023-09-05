###############################################################################
#### Download the python scripts and example data, and load them to memory ####
###############################################################################

"""
This script:
1. Downloads the python code and example data for the Green Pheasants recommendation system.
2. Loads the scripts and the data to memory.
"""

"""
Install (if necessary) and import the packages for the testing script
"""
# pip install requests
# pip install subprocess
# pip install pandas

import requests
import os
import tempfile
import pandas as pd

"""
Define functions for downloading the scripts and sample datasets from Github and saving them in the local environment
"""

def download_github_file(url, save_path):
    response = requests.get(url)
    response.raise_for_status()
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    with open(save_path, 'wb') as file:
        file.write(response.content)

def download_multiple_files(file_list):
    for url, save_path in file_list:
        download_github_file(url, save_path)
        print(f"Downloaded {url} to {save_path}")
        
# Create a temporary directory
temp_dir = tempfile.mkdtemp()

"""
Download the files from Github
"""

# Define lists of files to download
scripts_to_download = [
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/scripts/configuration.py', os.path.join(temp_dir, 'configuration.py')),
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/scripts/functions.py', os.path.join(temp_dir, 'functions.py')),
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/scripts/train_visitors.py', os.path.join(temp_dir, 'train_visitors.py')),
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/scripts/train_users.py', os.path.join(temp_dir, 'train_users.py')),
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/scripts/choose_item_online_visitor.py', os.path.join(temp_dir, 'choose_item_online_visitor.py')),
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/scripts/choose_item_online_user.py', os.path.join(temp_dir, 'choose_item_online_user.py')),
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/scripts/choose_items_many_offline_users.py', os.path.join(temp_dir, 'choose_items_many_offline_users.py')),
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/scripts/functions_for_testing.py', os.path.join(temp_dir, 'functions_for_testing.py'))
]

data_to_download = [
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/example_data/df_users.pkl', os.path.join(temp_dir, 'df_users.pkl')),
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/example_data/df_items.pkl', os.path.join(temp_dir, 'df_items.pkl')),
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/example_data/df_interactions.pkl', os.path.join(temp_dir, 'df_interactions.pkl'))
]

# Download the scripts and data
download_multiple_files(scripts_to_download)
download_multiple_files(data_to_download)

"""
Load the data into memory
"""

# Load all scripts into memory directly as strings
def load_scripts_as_strings(script_list):  
    for _, path in script_list:
        script_name = os.path.basename(path).replace('.py', '')
        with open(path, 'r') as file:
            globals()[script_name] = file.read()

# Load all pickle data into memory and assign it to dataframes
def load_dataframes(data_list):
    for _, path in data_list:
        name_without_extension = os.path.basename(path).replace('.pkl', '')
        globals()[name_without_extension] = pd.read_pickle(path)

# Execute the functions
load_scripts_as_strings(scripts_to_download)
load_dataframes(data_to_download)

# Print paths for scripts to easily open them in your IDE
print("Scripts downloaded to:")
for _, path in scripts_to_download:
    print(path)
    
print("Data downloaded to:")
for _, path in data_to_download:
    print(path)

print("\nData loaded into memory.")

### Caching the dataframes
from joblib import dump

def cache_dataframes(dataframes_dict, cache_dir):
    """
    Save the dataframes to disk for caching purposes.
    
    This function uses the joblib library to efficiently cache pandas dataframes. 
    The dataframes are saved in the specified directory with a '.cache' extension.

    Parameters:
    - dataframes_dict (dict): A dictionary where the keys are dataframe names and 
                              the values are the dataframes themselves.
    - cache_dir (str): The directory where the cached dataframes will be saved.

    Returns:
    None
    """
    
    for name, df in dataframes_dict.items():
        dump(df, os.path.join(cache_dir, f"{name}.cache"))

# Define a dictionary containing the dataframes you want to cache
dataframes = {
    "df_users": df_users,
    "df_items": df_items,
    "df_interactions": df_interactions
}

# Cache the dataframes to a temporary directory for later use
cache_dataframes(dataframes, temp_dir)

# Save temp_dir to a text file
with open("H:\\My Drive\\sync\\Green Pheasants\\Data and code\\Production\\Green-Pheasants-Shared\\scripts\\temp_dir_path.txt", "w") as file:
    file.write(temp_dir)