import subprocess

# Specify the path to your list.txt file
file_path = 'requirements.txt'

# Open the file and read each line
with open(file_path, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Remove leading and trailing whitespaces
        package_name = line.strip()
        
        # Uninstall the package using subprocess
        subprocess.run(['pip', 'uninstall', package_name, '-y'])
