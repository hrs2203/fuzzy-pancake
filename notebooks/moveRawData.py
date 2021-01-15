""" Move data from collection center. """

import os, pathlib


BASE_FILE = pathlib.Path(__file__).parent.absolute().parent.absolute()

COLLECTED_DATA_SET_LOCATION = os.path.join(BASE_FILE, "backend", "dataCollection","database","processedData")
RAW_DATASET_PATH = os.path.join(BASE_FILE, 'notebooks','raw_data_set')

def getRawFileList():
	return list( set(os.listdir(COLLECTED_DATA_SET_LOCATION)) - set(os.listdir(RAW_DATASET_PATH)) )

def moveAllData(self):
	filesToMove = getRawFileList()