import requests


# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# print(r.headers)

# payload = {'username': 'corey', 'password': 'testing'}
# r2 = requests.post('https://httpbin.org/post', data=payload)
#
# r2_dict = r2.json()
#
# print(r2.text)
# print(r2_dict['form'])

r = requests.get('https://httpbin.org/basic-auth/corey/testing',
                 auth=('corey', 'testing'))

print(r.text)