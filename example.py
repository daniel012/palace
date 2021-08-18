from bitsoRequestMethod import requestHandle

http_method = "GET" 
request_path = "/v3/balance/"
parameters = {}     

response = requestHandle(http_method, request_path, parameters)

print(response)