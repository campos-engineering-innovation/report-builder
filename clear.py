import os
import shutil
import json

def main():
	currentDir = os.getcwd()
	currentFolder = os.path.basename(currentDir)
	deletedDir = False
	allowed = False

	try:
		with open("clear_config.json") as f:
			config = json.load(f)
	except EnvironmentError:
		print("No configuration file specified, please create a \"clear_config.json\" file, specify the folder where the report builder is stored and try again")
		return

	for folder in config["FOLDERS"]:
		if folder == currentFolder:
			allowed = True
			break

	if not allowed:
		print("Can't run clean up here, unconfigured directory - {currentFolder}")
		return

	print("Cleaning up last run...")

	for root, dirs, files in os.walk(currentDir):
		if dirs == [] or dirs[0][0].isdigit():
			continue
		
		for tempDir in dirs:
			deletedDir = True
			dirToRemove = root + '\\' + tempDir
			print(f"Removing folder: {os.path.basename(dirToRemove)}")
			shutil.rmtree(dirToRemove)
	
	if not deletedDir:
		print("No files to delete!")

if __name__ == '__main__':
	main()