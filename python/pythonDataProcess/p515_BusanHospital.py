import json, urllib.request, datetime, math

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getHospitalData(pageNo, numOfRows):
    end_point = 'http://apis.data.go.kr/6260000/MedicInstitService/MedicalInstitInfo'
    access_key = 'CFAHqGsNsVSQwiMS5AzhGGhdN2oFt8nh1t%2Fu7%2B39ypEuz79UgbFqW4FWdcDaqUMH2lcGmF83c4OdreBuwpVOlg%3D%3D'

    parameters = ''
    parameters += "?resultType=json"
    parameters += "&serviceKey=" + access_key
    parameters += "&pageNo=" + str(pageNo) 
    parameters += "&numOfRows=" + str(numOfRows)  
    url = end_point + parameters

    print('URL')
    print(url)

    result = getRequestUrl(url)
    if (result == None):
        return None
    else:
        return json.loads(result)
# end def getHospitalData

jsonResult = []

pageNo = 1  
numOfRows = 100 
nPage = 0
while(True):
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    jsonData = getHospitalData(pageNo, numOfRows)
    print(jsonData)

    if (jsonData['MedicalInstitInfo']['header']['resultCode'] == '00'):
        totalCount = jsonData['MedicalInstitInfo']['body']['totalCount']
        print('데이터 총 개수 : ', totalCount)  

        for item in jsonData['MedicalInstitInfo']['body']['items']['item']:
            jsonResult.append(item)

        if totalCount == 0:
            break
        nPage = math.ceil(totalCount / numOfRows)
        if (pageNo == nPage):  
            break  

        pageNo += 1
    else :
        break

    savedFilename = 'xx_Busan_medical.json'
    with open(savedFilename, 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print(savedFilename + ' file saved..')
