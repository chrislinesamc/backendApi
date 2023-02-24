import requests
import json
import constants

#TODO generate API key

def getListOfSpecies(userHash):
    brainsListResp = requests.get(f'{constants.backendBase}/CC/getDetailsOfSeriesStatsAllRestricted/{userHash}')
    return brainsListResp.text
