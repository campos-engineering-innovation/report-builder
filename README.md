Current WIP Version: 7.7  
Current Known Working Version: 7.6  
  
This is the master copy of the Report Builder File and Folders.  
The .gitkeep files are there to ensure the folder structure is kept intact, as blank folders do not get tracked correctly.  
They should not affect the function of the program.  

clear.py is a script to delete the files that are generated from the Report Builder to speed up testing.  
Make sure `clear_config.json` is in the current directory
It can be run in the terminal with  
`python .\clear.py`

If the error "Don't run this here" pops up, edit `clear_config.json` with the current name of the folder the Report Builder and folders reside in.  
MAKE SURE THE ALL FILES AND FOLDERS ARE CONTAINED WITH THE SAME FOLDER, DO NOT RUN CLEAN OUTSIDE OF THE FOLDER

TODO: password protect config file and compile clear.py into executable  
      maybe share with others after security testing?
