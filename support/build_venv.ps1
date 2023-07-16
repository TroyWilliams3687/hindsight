# -----------
# SPDX-License-Identifier: MIT
# Copyright (c) 2023 Troy Williams

# uuid       = 19b82954-20f0-11ee-93b4-04cf4bfb0bc5
# author     = Troy Wiliams
# email      = troy.williams@bluebill.net
# date       = 2023-07-12
# -----------


#----
# Display the current working directory for reference

# Current Working Directory
"CWD = $(Get-Location)"

# Full Path to Script
"Script = $PSCommandPath"

# Script Root
"Script Path = $PSScriptRoot"

#----
# The path to the python binary.

$CFG="$PSScriptRoot\path.ini"

# read text file                        # find line beginning PYTHON
$LINE = Get-Content -Path $CFG | Where-Object { $_ -match 'PYTHON' }

# split on = symbol and take second item
$PYTHON = $LINE.Split('=')[1] -replace '"', ''

# ----
# Create the virtual environment

"Creating virtual environment..."
Start-Process -NoNewWindow -FilePath $PYTHON -ArgumentList "-m venv --clear --upgrade-deps .venv" -Wait

# ----
# Install Requirements


$VPYTHON=".venv\Scripts\python.exe"

"Installing Requirements..."
Start-Process -NoNewWindow -FilePath $VPYTHON -ArgumentList "-m pip install --upgrade -r requirements.txt" -Wait


"Installation and Configuration complete."