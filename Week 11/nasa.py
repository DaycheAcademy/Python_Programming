
# http://api.mysite.com/v1/topic/

import requests
import os

# base_url = 'https://randomuser.me/'
# end_point = 'api/?nat=ir&gender=female'

# api_url = os.path.join(base_url, end_point)


# api_url = 'https://randomuser.me/api'
api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'  # uri
print(api_url)

query_parameters = {'earth_date': '2022-07-28',
                    'api_key': 'DEMO_KEY'}

response = requests.get(api_url, params=query_parameters)
print(response.json())
print(response)

# print(response.json().get('photos'))
# print(len(response.json().get('photos')))

print(response.json().get('photos')[0]['img_src'])



