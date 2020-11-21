import base64

str_input = "HAPPY+/=~!@#$%^&*"
print("str_input:", str_input)     #// str_input: HAPPY+/=~!@#$%^&*

#// Encode bytes using the URL and filesystem-safe Base64 alphabet
#// 인코딩합니다
str_encoded = base64.urlsafe_b64encode(bytes(str_input, 'UTF-8')).decode("UTF-8")
print('str_encoded:', str_encoded) #// str_encoded: SEFQUFkrLz1-IUAjJCVeJio=

#// Decode bytes using the URL and filesystem-safe Base64 alphabet
#// 디코딩합니다
str_decoded = base64.urlsafe_b64decode(bytes(str_encoded, 'UTF-8')).decode("UTF-8")
print('str_decoded:', str_decoded) #// str_decoded: HAPPY+/=~!@#$%^&*

print(str_input == str_decoded)