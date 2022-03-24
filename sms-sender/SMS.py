#requirements
#make sure you have python3 and requests installed
#Signup a account in www.fast2sms.com - good service in for Indian users
#You can send 20 free SMS daily
#Find Dev API tab and open
#find API key tab and open
#copy the API Authorization key

import requests
url = "https://www.fast2sms.com/dev/bulk"

#If you are using the Free SMS service than the default sender_id is FSTSMS.
#Replace DIA with your message
#Replace 3699633699 with the destination number 
#you can add one or more numbers by adding ","
#The message is sent with your mobile number as initials.

payload = "sender_id=FSTSMS&message=DIA&language=english&route=p&numbers=3699633699"
headers = {
'authorization': "API_Authorization_key",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload,  headers=headers)
fun_part = "Subscribe to DIA Sessions on Youtube"
print(response.text+fun_part)
