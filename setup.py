import os
f = open('api','w+')
api_key = input('API:')
f.write(api_key)
os.system("pip install -r requirements.txt")
