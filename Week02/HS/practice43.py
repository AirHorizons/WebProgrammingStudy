import re
url = re.compile('^(https?:\/\/)([A-Za-z0-9\-]+\.)+[A-Za-z0-9\-]+(\/[A-Za-z0-9\-_\?=\.]+)*$')
print(url.match(input().strip()) != None)
