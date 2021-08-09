# Simple script to download the list of companies 
# working in Madrid from the audiovisual field.

# Python depencencies
import pandas as pd
import subprocess as sp

# Start by downloading the "empresas.js" file from the filmmadrid web
try:
    print("Downloading empresas.js")
    node_process = sp.run(["node", "dump_empresas.js"])
    print("Download successful")
except PermissionError:
    print("nodejs not found.\nTry 'sudo apt install nodejs'")
    exit()

# Parse the downloaded json file as a Dataframe in pandas
data = pd.read_json("empresas.json")

# Create Excel file for ease of use
try:
    print("Creating Excel file")
    data.to_excel('empresas.xlsx', index=False)
    print("Excel created successfuly")
except:
    print("Could not create Excel")