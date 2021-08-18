import time
import hmac
import hashlib
import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('configuration.ini')
bitso_key = config['Bitso']['key']
bitso_secret = config['Bitso']['secret']
   
def requestHandle(http_method, request_path, parameters):
  nonce =  str(int(round(time.time() * 1000)))
  message = nonce+http_method+request_path
  if (http_method == "POST"):
    message += json.dumps(parameters)
  signature = hmac.new(bitso_secret.encode('utf-8'),
                                              message.encode('utf-8'),
                                              hashlib.sha256).hexdigest()

  auth_header = 'Bitso %s:%s:%s' % (bitso_key, nonce, signature)

  if (http_method == "GET"):
    response = requests.get("https://api.bitso.com" + request_path, headers={"Authorization": auth_header})
  elif (http_method == "POST"):
    response = requests.post("https://api.bitso.com" + request_path, json = parameters, headers={"Authorization": auth_header})
  elif(http_method == "DELETE"):
    response = requests.delete("https://api.bitso.com" + request_path, headers={"Authorization": auth_header})
  return response.content