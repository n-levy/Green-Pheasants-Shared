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
    ('https://raw.githubusercontent.com/n-levy/Green-Pheasants-Shared/main/scripts/choose_items_many_offline_users.py', os.path.join(temp_dir, 'choose_items_many_offline_users.py'))
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

# Load data
# 1. Load all scripts into memory
def load_scripts_into_memory(script_list):
    script_content = {}
    
    for _, path in script_list:
        with open(path, 'r') as file:
            script_content[os.path.basename(path)] = file.read()
    
    return script_content

# 2. Load all pickle data into memory
def load_data_into_memory(data_list):
    data_content = {}
    
    for _, path in data_list:
        data_content[os.path.basename(path)] = pd.read_pickle(path)
    
    return data_content

# Execute the functions
scripts_in_memory = load_scripts_into_memory(scripts_to_download)
data_in_memory = load_data_into_memory(data_to_download)

# Print paths for scripts to easily open them in your IDE
print("Scripts downloaded to:")
for _, path in scripts_to_download:
    print(path)
    
print("Data downloaded to:")
for _, path in data_to_download:
    print(path)

print("\nData loaded into 'data' dictionary.")


