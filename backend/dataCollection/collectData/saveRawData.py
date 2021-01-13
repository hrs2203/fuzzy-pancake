import os, pathlib, random, string, json

BASE_FILE = pathlib.Path(__file__).parent.absolute().parent.absolute()
RAW_DATA_FILE = os.path.join(BASE_FILE, "database", "raw_data")


def generateNewFileName(destinationFile: str, fileExtention: str) -> str:
    """Generate new unique file name to be save in destination File

    Args:
        destinationFile (str): save destination
        fileExtention (str): fileExtention to save, ( Preferably JSON )

    Returns:
        str: new file name, not path.
    """

    fileList = set(os.listdir(destinationFile))

    newFileNameLen = 10
    newFileName = "".join(
        [random.choice(string.ascii_lowercase) for i in range(newFileNameLen)]
    )
    newFileName = f"{newFileName}.{fileExtention}"
    newFilePath = os.path.join(destinationFile, newFileName)

    while os.path.isfile(newFileName):
        newFileName = "".join(
            [random.choice(string.ascii_lowercase) for i in range(newFileNameLen)]
        )
        newFileName = f"{newFileName}.{fileExtention}"
        newFilePath = os.path.join(destinationFile, newFileName)

    return newFileName


def saveJsonFileInRawFolder(jsonContent: dict) -> str:
    """Saves JSON data in `raw_data` folder

    Args:
        jsonContent (dict): json body

    Returns:
        str: file path
    """

    newFileName = generateNewFileName(RAW_DATA_FILE, "json")
    filePath = os.path.join(RAW_DATA_FILE, newFileName)

    with open(filePath, "w") as fileObject:
        json.dump(jsonContent, fileObject, indent=4)

    return filePath


