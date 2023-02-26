import requests
import json
import constants

#TODO generate API key

def getListOfSpecies(userHash):
    brainsListResp = requests.get(f'{constants.backendBase}/CC/getDetailsOfSeriesStatsAllRestricted/{userHash}')
    return brainsListResp.text

def get_brain_list():

    species_list = []
    brain_list = []


    for i in range(len(brainsList['data'])):
        print(brainsList['data'][i]['data']['species_name'])
    print(species_list)

    for i in range(len(brainsList['data'][3]['children'][0]['children'])):
        brain_name = brainsList['data'][3]['children'][0]['children'][i]['data']['brain_name']
        series_set_id = brainsList['data'][3]['children'][0]['children'][i]['data']['seriesset_id']
        brain_list.append((brain_name,series_set_id))
    print(brain_list)
    return species_list,brain_list 

def getSingleBrainDetails(seriesSetId):
    seriessetDetailsResp = requests.get(f'https://apollo2.humanbrain.in/GW/getBrainThumbNailDetails/IIT/V1/SS-{seriesSetId}:-1:-1')
    seriessetDetail = json.loads(seriessetDetailsResp.text)
    return seriessetDetail

def getListOfSeriesTypeForBrain(seriesSetId):
    seriesType = []
    seriessetDetailsResp = requests.get(f'https://apollo2.humanbrain.in/GW/getBrainThumbNailDetails/IIT/V1/SS-{seriesSetId}:-1:-1')
    seriessetDetail = json.loads(seriessetDetailsResp.text)
    for i in range(len(seriessetDetail)):
        seriesType.append(seriessetDetail[i]['seriesType'])
    return seriesType

def getSectionDetails(sectionNo):
    sectionDetaisRest = requests.get(f'https://apollo2.humanbrain.in/GW/getBrainViewerDetails/IIT/V1/SS-15:10:{sectionNo}').text
    sectionDetails = json.loads(sectionDetaisRest)
    return sectionDetails['Section'][0]
