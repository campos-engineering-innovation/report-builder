Current WIP Version: 7.9  
Current Known Working Version: 7.8  
  
This is the master copy of the Report Builder File and Folders.  
The .gitkeep files are there to ensure the folder structure is kept intact, as blank folders do not get tracked correctly.  
They should not affect the function of the program.  

clear.py is a script to delete the files that are generated from the Report Builder to speed up testing.  
Make sure `clear_config.json` is in the current directory
It can be run in the command line with  
`python .\clear.py`
If the error "Can't clean up here" pops up, rename your current working directory to `report-builder` or talk to Joseph/Dirk  
ONLY EVER RUN THIS PYTHON SCRIPT IN ITS OWN DIRECTORY, DO NOT RUN THIS ANYWHERE ELSE AS IT MAY DELETE UNRELATED FOLDERS  
