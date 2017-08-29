import urllib.request
import requests
import json

try:
    tracking_number = int(input("Enter your tracking id : "))
    #print("https://www.fedex.com/apps/fedextrack/?action=track&trackingnumber="+str(track)+"&cntry_code=in")
except Exception as e:
    print(e)


#the json request being sent to the fedex website can be viewed using a browser extension that lets you see http requests made by the client
#this data is sent with a post method. It is appended at the end of the url. The tracking number is part of this data    



data1 = requests.post('https://www.fedex.com/trackingCal/track', data={
    'data': json.dumps({
        'TrackPackagesRequest': {
            'appType': 'wtrk',
            'uniqueKey': '',
            'processingParameters': {
                'anonymousTransaction': True,
                'clientId': 'WTRK',
                'returnDetailedErrors': True,
                'returnLocalizedDateTime': False
            },
            'trackingInfoList': [{
                'trackNumberInfo': {
                    'trackingNumber': tracking_number,
                    'trackingQualifier': '',
                    'trackingCarrier': ''
                }
            }]
        }
    }),
    'action': 'trackpackages',
    'locale': 'en_In',
    'format': 'json',
    'version': 1
}).json()


print(data1['TrackPackagesResponse']['errorList'])



#resp_dict = json.loads(data1)
#source = urllib.request.urlopen('https://www.fedex.com/apps/fedextrack/?action=track&trackingnumber='+str(track)+'&cntry_code=in').read()
#soup = bs.BeautifulSoup(source,'lxml')
#print (soup)
