Current WIP Version: 7.11.8
Current Known Working Version: 7.11.8
  
This is the master copy of the Report Builder File and Folders.  
The .gitkeep files are there to ensure the folder structure is kept intact, as blank folders do not get tracked correctly.  
They should not affect the function of the program.  

`clear.py/exe` is a script to delete the files that are generated from the Report Builder to speed up testing.  
Make sure `clear_config.json` is in the current directory
It can be run in the command line with  
`python .\clear.py` or double click on the `clear.exe`(RECOMMENDED) command script if it exists  
Running it through python requires python and the proper libraries to be installed  
If the error "Can't clean up here" pops up, rename your current working directory to `report-builder` or talk to Joseph/Dirk  
ONLY EVER RUN THIS SCRIPT IN ITS OWN DIRECTORY, DO NOT RUN THIS ANYWHERE ELSE AS IT MAY DELETE UNRELATED FOLDERS  
