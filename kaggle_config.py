import os
import shutil

# Define the source and destination paths
source_file = "/home/vasanth/Downloads/kaggle.json"  # Ensure this file is in the same directory as the script
destination_dir = os.path.expanduser("~/.kaggle")
destination_file = os.path.join(destination_dir, "kaggle.json")

# Create the .kaggle directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Move the kaggle.json file
shutil.move(source_file, destination_file)

# Set appropriate permissions
os.chmod(destination_file, 0o600)

print("Kaggle API is configured successfully!")



# Install Kaggle Package (if not installed)
#!pip install kaggle

#Verify the Configuration
#!kaggle datasets list

