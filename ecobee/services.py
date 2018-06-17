import requests

#TYPE : POST
def refreshToken( client_id, refresh_token):
  url = "https://api.ecobee.com/token?grant_type=refresh_token"
  params = {"refresh_token": refresh_token, "client_id" :client_id}
  res = requests.post(url, params=params)
  res = res.json()
  print( res ) 
  return res

#TYPE : POST
def getThermostatData( client_id, access_token ): 
  pass

#TYPE: POST
def requestAccessToken( client_id, code ):
  pass


if __name__ == "__main__":
  client_id = "VMm9LjRZmLB8SSsoSc6cu2ac3WI9zvWq"
  refresh_token = "D4OJfJSGjRVLD8qvbsomg0noOC2mMFRC"
  refreshToken( client_id, refresh_token)
