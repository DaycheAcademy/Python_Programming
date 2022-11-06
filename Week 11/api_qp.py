
from typing import Union  # python user version 3.6 to 3.9
from fastapi import FastAPI

# api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2022-07-28&api_key=DEMO_KEY'
# query_parameters = {'earth_date': '2022-07-28',
#                     'api_key': 'DEMO_KEY'}

app = FastAPI()


@app.get('/v1/users/{userID}')  # application/path/function ,  method/path/function
async def get_user_id(userID: int, user_name: str, password: str, location: str | None = None):
    items = {'Message': 'you are using API for user ID: {}'.format(userID),
             'ID Data Type': '{}'.format(type(userID)),
             'user_name': user_name,
             'password': password}
    if location:
        items.update({'location': location})
    return items


@app.get('/v1/users/details/{userID}')  # application/path/function ,  method/path/function
async def get_user_id(userID: int, user_name: str, password: str):  # annotation == type validation
    items = {'Message': 'you are using API for user ID: {}'.format(userID),
             'ID Data Type': '{}'.format(type(userID)),
             'user_name': user_name,
             'password': password}
    return items





