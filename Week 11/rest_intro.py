
# REST API: Utilise HTTP(s)
# url: https://api.github.com     https://api.twitter.com
import os

import requests
response = requests.get('https://randomuser.me/api/?nat=ir')
print(response)


base_url = 'https://randomuser.me/'
end_point = 'api/?nat=ir&gender=female'

# Query Parameters ---> ?

# HTTP STATUS CODES: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# HTTP METHODS: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
# GET, POST, PUT, DELETE, PATCH, TRACE, HEAD, OPTIONS, CONNECT

print('=' * 40)
print(response.content)
print(response.text)

# content_type: 1 - text, 2 - content

print('=' * 40)
print(response.status_code)
print(response.reason)

print('=' * 40)
print(response.headers)

print('=' * 40)

req = response.request
print(req.headers)
print(req.path_url)  # endpoint
print(req.url)  # full request url
print(req.method)




