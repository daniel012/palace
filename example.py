from bitsoRequestMethod import requestHandle
# make a order
"""
http_method = "POST" 
request_path = "/v3/orders/"
parameters = {
    'book':'btc_mxn',
    'side': 'buy',
    'type': 'limit',
    'major':'1',
    'price':'501'
}     

response = requestHandle(http_method, request_path, parameters)

""" 

http_method = "DELETE" 
request_path = "/v3/orders/28kz2561cCTKyU2M"
parameters = {}     

response = requestHandle(http_method, request_path, parameters)

print(response)