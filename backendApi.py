import requests
import json
import constants

#TODO generate API key

def getListOfSpecies(userHash):
    brainsListResp = requests.get(f'{constants.backendBase}/CC/getDetailsOfSeriesStatsAllRestricted/{userHash}')
    return brainsListResp.text

def get_brain_list(self):

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

    def get_single_brain_details(self):
        print("Single brain details using seriesset id :")
        seriessetDetailsResp = requests.get(f'{constants.backendBase}/GW/getBrainThumbNailDetails/IIT/V1/SS-15:-1:-1')
        seriessetDetail = json.loads(seriessetDetailsResp.text)

        for i in range(len(self.seriessetDetail)):
            print(self.seriessetDetail[i]['seriesType'])

        for i in range(len(self.seriessetDetail[4]['thumbnails'])):
            print(self.seriessetDetail[4]['thumbnails'][i]['brainid'])

        return seriessetDetail

    def get_section_no(self):

        sectionDetaisRest = requests.get(f'{constants.backendBase}/GW/getBrainViewerDetails/IIT/V1/SS-15:10:1186').text
        sectionDetails = json.loads(sectionDetaisRest)
        return sectionDetails

    def get_annotation_types(self):
        

        headers= {'Authorization': 'Basic YWRtaW46YWRtaW4='}
        annotationTypeResp = requests.get(f'{constants.backendBase}/BR/AppAnnotationType/', headers={'Authorization': 'Basic YWRtaW46YWRtaW4='})
        annotationType = json.loads(annotationTypeResp.text)
        return annotationType




