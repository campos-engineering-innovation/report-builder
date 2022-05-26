import os
import shutil
import json
import hashlib

def main():
	currentDir = os.getcwd()
	currentFolder = os.path.basename(currentDir)
	currentHash = "b11b60c460e286a65cfcfc88dab9a7bb5f0c8b5806d57b3cd0c3e48088cc09f6" # hash of the state of the file 5/23/22
	deletedDir = False
	allowed = False

	print("Config:", end=" ")

	try:
		with open("clear_config.json") as f:
			config = json.load(f)
		with open("clear_config.json", "rb") as fHash:
			bytes = fHash.read()
			fileHash = hashlib.sha256(bytes).hexdigest()

	except EnvironmentError:
		print("Missing")
		print("No configuration file found, please create a \"clear_config.json\" file, specify the folder where the report builder is stored and try again")
		return

	for folder in config["FOLDERS"]:
		if folder == currentFolder:
			allowed = True
			break

	if not allowed or fileHash != currentHash:
		print(f"Working Directory Not Matched - \"{currentFolder}\"")
		print(f"Can't run clean up here, unconfigured directory")
		return

	print(f"Working Directory Match - {currentFolder}")
	print("Cleaning up last run...")

	for root, dirs, files in os.walk(currentDir):
		#print(dirs)
		if dirs == [] or dirs[0][0].isdigit() or "git" in root or dirs[0] == ".git": 
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