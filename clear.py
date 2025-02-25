import os
import shutil
import json
import hashlib


def main():
    currentDir = os.getcwd()
    currentFolder = os.path.basename(currentDir)
    currentHash = (
        "0ce1f9435f4daf405aadd8d971e0a7c2c21453bbf1593ef588f0a269357d8024"
    )  # hash of the state of the file 8/20/24
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
        print("No configuration file found, please retrieve a certified copy.")
        os.system("pause")
        return

    for folder in config["FOLDERS"]:
        if folder == currentFolder:
            allowed = True
            break

    if not allowed or fileHash != currentHash:
        print(f'Working Directory Not Matched - "{currentFolder}" or Config Modified')
        print("Can't run clean up here!")
        os.system("pause")
        return

    print(f'Working Directory Match - "{currentFolder}"')
    print("Cleaning up last run...")

    for root, dirs, files in os.walk(currentDir):
        if dirs == [] or dirs[0][0].isdigit() or "git" in root or dirs[0] == ".git":
            continue

        for tempDir in dirs:
            deletedDir = True
            dirToRemove = root + "\\" + tempDir
            print(f"Removing folder: {os.path.basename(dirToRemove)}")
            try:
                shutil.rmtree(dirToRemove)
            except Exception:
                print(
                    f"Failed to remove folder: {os.path.basename(dirToRemove)}, check if any files in this folder are open..."
                )

    if not deletedDir:
        print("No files to delete!")

    os.system("pause")


if __name__ == "__main__":
    main()
