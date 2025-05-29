import os
import json
import shutil
import zipfile
import sys
import logging



# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_config(root_folder):
    mandatory_file_list = ["config.json", "app.py"]
    for file in mandatory_file_list:
        if not os.path.join(root_folder, file):
            logging.info(f"error: {file} not found insidr config")
            sys.exit(1)

def copy_folder(source_folder, destination_folder):
    if not os.path.isdir(source_folder):
        logging.info(f"The source folder '{source_folder}' does not exist.")
        return
    if os.path.isdir(destination_folder):
        shutil.rmtree(destination_folder)
    # Copy the folder
    shutil.copytree(source_folder, destination_folder)
    logging.info(f"Folder '{source_folder}' copied to '{destination_folder}'.")


def zip_folder(folder_path, zip_path):
    logging.info(f"creating zip: {folder_path}")
    # Create a new zip file at the specified path
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Traverse all files and folders in the directory
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Create the full path for each file
                file_path = os.path.join(root, file)
                # Write the file to the zip archive, preserving the folder structure
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

def get_valid_package_list(root_folder):
    valid_folders = []

    # Loop through all directories in the root folder
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Define paths for 'data' and 'meta' folders
            data_folder = os.path.join(folder_path, 'data')
            meta_folder = os.path.join(folder_path, 'meta')
            package_json = os.path.join(meta_folder, 'package.json')
            
            # Check if 'data' and 'meta' folders exist and 'package.json' is in 'meta'
            if os.path.isdir(data_folder) and os.path.isdir(meta_folder) and os.path.isfile(package_json):
                valid_folders.append(folder_name)
        
    return valid_folders

def create_pre_build(packages):
    valid_package_list = get_valid_package_list(packages)
    logging.info(f"package list: {valid_package_list}")
    global_dict = {}
    global_dict['packages'] = {}
    for package_name in valid_package_list:
        temp_package_data = {}
        package_json_file = os.path.join(packages, package_name, "meta", "package.json")
        with open(package_json_file, "r") as f:
            temp_package_data = json.load(f)
        global_dict['packages'][temp_package_data['name']] = temp_package_data
        copy_folder(os.path.join(packages, package_name, "data"), os.path.join(".build", temp_package_data['name']))
        global_dict['packages'][temp_package_data['name']]['folder'] = temp_package_data['name']
        zip_folder(os.path.join(".build", temp_package_data['name']), os.path.join(".build", f"{temp_package_data['name']}.zip"))
        global_dict['packages'][temp_package_data['name']]['archive'] = f"{temp_package_data['name']}.zip"

    global_dict['config'] = {}
    config_file = os.path.join(config, "config.json")
    with open(config_file, "r") as f:
        global_dict['config'] = json.load(f)

    configuration_folder = os.path.join(".build")
    if not os.path.exists(configuration_folder):
        os.makedirs(configuration_folder)
        logging.info(f"Directory '{configuration_folder}' created.")

    global_config_file = os.path.join(configuration_folder, "global_data.json")
    with open(global_config_file, "w+") as f:
        json.dump(global_dict, f, indent=4, sort_keys=True)

config = "config"
packages = "packages"

validate_config(config)
create_pre_build(packages)