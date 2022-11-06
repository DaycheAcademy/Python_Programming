
# https://github.com/Redocly/redoc
# https://github.com/OAI/OpenAPI-Specification

# Framework
# Django, Flask, fastAPI

from enum import Enum
from fastapi import FastAPI


class Models(str, Enum):
    vggnet = 'vggnet'
    resnet = 'resnet'
    alexnet = 'alexnet'
    googlenet = 'googlenet'
    lenet = 'lenet'

app = FastAPI()


@app.get('/')  # application/path/function ,  method/path/function
async def root():
    return {'Message': 'Welcome to Dayche Class'}


@app.get('/v1/users/')  # application/path/function ,  method/path/function
async def show_users():
    return {'Message': 'You are viewing user handling APIs'}


@app.get('/v1/users/{userID}')  # application/path/function ,  method/path/function
async def get_user_id(userID: int):  # annotation == type validation
    return {'Message': 'you are using API for user ID: {}'.format(userID),
            'ID Data Type': '{}'.format(type(userID))}

# pydantic: https://pydantic-docs.helpmanual.io/


@app.get('/v1/models/{model_name}')
async def specify_model(model_name: Models):
    if model_name.value == 'vggnet':
        return {'model name': model_name,
                'Message': 'you are using API for model: {}'.format(model_name)}
    if model_name.value == 'resnet':
        return {'model name': model_name,
                'Message': 'you are using API for model: {}'.format(model_name)}
    if model_name.value == 'alexnet':
        return {'model name': model_name,
                'Message': 'you are using API for model: {}'.format(model_name)}
    if model_name.value == 'googlenet':
        return {'model name': model_name,
                'Message': 'you are using API for model: {}'.format(model_name)}
    if model_name.value == 'lenet':
        return {'model name': model_name,
                'Message': 'you are using API for model: {}'.format(model_name)}


# -------------------------------------------
# def test(inp1: int, inp2: float) -> dict:
#     return {'firstValue': inp1,
#             'secondValue': inp2}


# base_url : http://api.mysite.com
# end_point : /v1/users/userAuth

# ===========================================

# Concurrency: threading, multiprocessing, asyncio

# Coroutines  ----> await
