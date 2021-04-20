#!/bin/sh
#------------------------
# -- Developed by:
# :: trevalkov
#------------------------
# -- Copyright:
# :: Free Software (as in freedom)
#------------------------
# Setup python virtual environment and install dependencies
#------------------------
# -- Commands:
# :: Setup: ./setup.sh
# :: Start: source activate
# :: Stop: deactivate
# :: Clean: ./clean.sh
#------------------------
# Set up virtual environment
# Activate virtual environment
# Install pygame module with pip
#------------------------
python3 -m venv modules && source modules/bin/activate && pip install pygame &&
  ln -s modules/bin/activate activate && echo -e "\n[INFO] Setup was successfull\n"


