# A test script for PyEcho
# By Scott Vanderlind, December 31 2014

import PyEcho, getpass, json

with open('api.txt', 'r') as f:
    apis = f.readlines()

# for api in apis :
#     print "* " + api.strip() + "!"

email = raw_input("Email: ")
password = getpass.getpass()
echo = PyEcho.PyEcho(email, password)

if echo:
   print "API Monitor. Type an endpoint (starting with /api/) to fetch."
   for api in apis:
       api = api.strip()
       print "Using API : " + api
       jsonPayload = echo.get(api).text
       parsed = json.loads(jsonPayload)
       print json.dumps(parsed, indent=4, sort_keys=True)
