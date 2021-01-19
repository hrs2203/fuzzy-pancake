import requests, os

from key.NewsApi import APIkeyDict

from saveRawData import saveJsonFileInRawFolder


class CollectData:
    def newsAPIRequest(self, topic: str) -> dict:
        """Read Data from NewsApi

        Args:
            topic (str): Topic to look from

        Returns:
            dict: response json
        """
        
        API_KEY = APIkeyDict['NewsAPI_PERSONAL_KEY']

        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"

        response = requests.get(url)
        
        return response.json()


# if __name__ == "__main__":
#     collectionObject = CollectData()

#     bitcoinData = collectionObject.newsAPIRequest("tesla")
#     saveJsonFileInRawFolder(bitcoinData)
#     bitcoinData = collectionObject.newsAPIRequest("spacex")
#     saveJsonFileInRawFolder(bitcoinData)
