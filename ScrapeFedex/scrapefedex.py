#Author - Dalton De Souza

import urllib.request
import urllib.parse
import requests
import json
from time import sleep
import datetime

try:
    tracking_number = int(input("Enter your tracking id : "))
except Exception as e:
    print(e)

#tracking_number = 744668909687
#the json request being sent to the fedex website can be viewed using a browser extension that lets you see http requests made by the client
#this data is sent with a post method. It is appended at the end of the url. The tracking number is part of this data. The other values are the
#default values that are sent to fetch the tracking information

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


#converting the retrieved input to be able to access the keys and their values
q=json.loads(json.dumps(data1['TrackPackagesResponse']['packageList']))

shipDate= q[0]['displayShipDt']     #the shipping date of the package
status = q[0]['keyStatus']          #status of the package

if (status!='Delivered'):
    deliveryDate=q[0]['displayEstDeliveryDt']                                        #if the package isn't delivered then display estimated delivery date
    deliveryTime=q[0]['displayEstDeliveryTm']                                        #if the package isn't delivered then display estimated delivery time
    day = datetime.datetime.strptime(deliveryDate, '%d/%m/%Y').strftime('%a')
    deliveryDate='"'+day+' '+deliveryDate+' by '+deliveryTime+'"'
else:    
    deliveryDate=q[0]['displayActDeliveryDt']                                        #the actual delivery date
    deliveryTime=q[0]['displayActDeliveryTm']                                        #the acutal delivery time
    day = datetime.datetime.strptime(deliveryDate, '%d/%m/%Y').strftime('%a')
    deliveryDate='"'+day+' '+deliveryDate+' at '+deliveryTime+'"'                    #converting the delivery date into the format expected


#getting the day of the week the package was shipped from the date as this info is not available in the json data fron fedex
day = datetime.datetime.strptime(shipDate, '%d/%m/%Y').strftime('%a')

shipDate='"'+day+' '+shipDate+'"'           #converting the ship date into the format expected


#saving the information in variable outp in string format
outp = '{"tracking no":'+str(tracking_number)+',\n"ship date":'+shipDate+',\n"status":"'+status+'",\n"scheduled delivery":'+deliveryDate+'}'


outp=json.loads(outp)           #converting variable outp that contains string data into a json object
print(outp)

#Author - Dalton De Souza
