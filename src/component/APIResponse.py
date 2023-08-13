from fastapi import status
from fastapi.responses import JSONResponse
from typing import Union

# 定义响应统一结构体

def success(data: Union[list, dict, str]):
    '''
    200系列的响应结构体
    *：代表调用方法时必须传参数
    Union：代表传入的参数可以是多种类型
    '''
    if data == None:
        data = {}
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 0,
            'message': "SUCCESS",
            'data': data,
        }
    )


def failure(data: str, message='Bad Request!'):

    if data == None:
        data = {}

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': 1,
            'message': message,
            'data': data,
        }
    )

def resp_400(*, data: str, message='Bad Request!'):
    '''
    400系列的响应结构体
    *：代表调用方法时必须传参数
    '''
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': 1,
            'message': message,
            'data': data,
        }
    )
