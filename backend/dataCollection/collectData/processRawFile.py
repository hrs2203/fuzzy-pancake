import os, pathlib, json
from saveRawData import (
    saveJsonFileInProcessedFolder,
    RAW_DATA_FILE_PATH,
    PROCESSED_DATA_FILE_PATH,
)


class NewsAPIParser:
    def getFileList(self) -> list:
        """Get list of unprocessed files

        Returns:
            list: file path list
        """
        processedFiles = set(os.listdir(PROCESSED_DATA_FILE_PATH))
        rawFiles = set(os.listdir(RAW_DATA_FILE_PATH))

        return rawFiles - processedFiles

    def processFiles(self, fileName: list) -> None:
        """Process the file content and store it in processed file

        Args:
            fileName (list): list of file to be processed
        """

        for eachFile in fileName:
            fileObj = open(os.path.join(RAW_DATA_FILE_PATH, eachFile), "r")
            fileContent = fileObj.read()
            fileContent = json.loads(fileContent)
            fileObj.close()

            fileContent = fileContent["articles"]

            parsedContent = {
                "body": [
                    {
                        "title": item["title"],
                        "description": item["description"],
                        "content": item["content"],
                    }
                    for item in fileContent
                ]
            }

            fileObj = open(os.path.join(PROCESSED_DATA_FILE_PATH, eachFile), "w")
            fileContent = json.dump(parsedContent, fileObj, indent=4)
            fileObj.close()


# if __name__ == "__main__":
#     parserObject = NewsAPIParser()

#     fileList = parserObject.getFileList()
#     parserObject.processFiles(fileList)
