import requests

url = 'https://thinkpython.com/code/words.txt' # or whatever the file url is
r = requests.get(url, allow_redirects=True)

open('/home/nemptage/words.txt', 'wb').write(r.content)
