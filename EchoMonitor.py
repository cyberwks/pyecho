# A test script for PyEcho
# By Scott Vanderlind, December 31 2014

import PyEcho, getpass

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
       print echo.get(api).text
