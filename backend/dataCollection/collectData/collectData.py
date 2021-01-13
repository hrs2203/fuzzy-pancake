"""File that will Collect Data based on list of paremeters provided"""

from scrapeWeb import CollectData
from saveRawData import saveJsonFileInRawFolder
from processRawFile import NewsAPIParser

if __name__ == "__main__":
    TopicList = ["android","harry potter"]

    collectionObject = CollectData()

    for topic in TopicList:
        print(f"Collecting for {topic}", end="... ")
        collectedData = collectionObject.newsAPIRequest(topic)
        print(f"Collected for {topic}", end="... ")
        saveJsonFileInRawFolder(collectedData)
        print(f"Saved for {topic}...")
    
    newsParserObject = NewsAPIParser()

    filesToProcess = newsParserObject.getFileList()
    print(filesToProcess)
    newsParserObject.processFiles(filesToProcess)

