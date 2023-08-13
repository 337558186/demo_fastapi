from fastapi import APIRouter,Request,Body,Header
import uvicorn
from starlette.responses import HTMLResponse,FileResponse,JSONResponse
from fastapi.templating import Jinja2Templates  # 模板引擎，响应html页面
import json
# 将post请求 body转字典
from urllib.parse import parse_qs
# 数据库相关
from fastapi import Depends
from mysql.connector import cursor
from src.config.dbConfig import get_db
# 自定义组件
from src.component.Logger import logger  # 日志组件
import src.component.APIResponse as resp # 自定义的响应体


# 创建服务
# router = APIRouter(encodings = "utf-8")
router = APIRouter()


@router.get("/users")
async def get_users(db: cursor.MySQLCursor = Depends(get_db)):
    """
    查询所有user信息【查】
    :param db:
    :return:
    """
    sql = "SELECT * FROM user_info"
    db.execute(sql)
    result = db.fetchall()  # 结果集

    # 将查询结果按字典的方式输出
    list_result = []
    for i in result:
        date_list = list(i)
        des = db.description  # 获取表详情，字段名，长度，属性等
        table_head = [item[0] for item in des]  # 获取表头
        dict_result = dict(zip(table_head, date_list))  # 打包为元组的列表 再转换为字典
        list_result.append(dict_result)  # 将字典添加到list_result中

    print(list_result, end='\n')

    if result:
        return list_result
    else:
        return {"error": "User not found"}


@router.get("/{user_id}")
async def get_user_by_id(user_id: int = 1 , db: cursor.MySQLCursor = Depends(get_db)):
    """
    根据ID查询用户【条件查】
    :param user_id:
    :param db:
    :return:
    """
    sql = "SELECT * FROM user_info WHERE id >= (%s);"
    data = user_id
    db.execute(sql, data)
    result = cur.fetchmany(1) # 一次查找1条

    if result:
        return {"user_id": result[0][0], "username": result[0][1]}
    else:
        return {"error": "User not found"}


@router.get("/{user_name}")
async def delete_user_by_username(user_name: str = None , db: cursor.MySQLCursor = Depends(get_db)):
    """
    删除用户信息【删】
    :param user_name:
    :param db:
    :return:
    """
    # sql语句
    sql = "delete  from user_info where username = (%s);"  # 其中%s为mysql占位符
    data = user_name
    db.execute(sql,data)

    sql1 = "select * from user_info where username = (%s);"
    db.execute(sql1,data)
    result = db.fetchall() # 查所有
    if result == None:
        return resp.success()
    else:
        return resp.failure()


# ------------------------------------------------POST请求-------------------------------------

# 方案 解析
"""
from urllib.parse import parse_qs
from fastapi import Body

@router.post("/register")
async def register(body = Body(None)):  
    # 将body转成字典
    rep_dict = parse_qs(body.decode('utf-8'))
    username = str(rep_dict['username'][0])

"""

@router.post("/login",response_class=HTMLResponse,summary="跳转登录页")
async def login(body = Body(None),token = Header(None),db: cursor.MySQLCursor = Depends(get_db)):
    """
    json.dumps(): 对数据进行编码。将字典转成json
    json.loads(): 对数据进行解码。将json转成字典
    """
    # 解析请求体
    print(type(body))
    # 获取请求头token
    body["token"] = token
    logger.info(body)

    account = body["account"]
    logger.info(account+"开始登录")
    return resp.success(account)

@router.api_route("/register",methods=("POST,PUT"))
async def register(body = Body(None),db: cursor.MySQLCursor = Depends(get_db)):
    """
    注册【增】
    :param body:
    :return:
    """

    sql = "insert into user_info (id,name) values (%s,%s);"  # 其中%s为mysql占位符
    data = [(1, "li"), (2, "davy"), (3, "july")]  # 执行SQL语句时，使用元组传递参数（填充占位符）对应SQL语句的values
    db.execute(sql, data)

    return resp.success()


@router.api_route("/register",methods=("POST,PUT"))
async def update(body = Body(None),db: cursor.MySQLCursor = Depends(get_db)):
    """
    修改用户信息【改】
    :param body:
    :return:
    """
    # sql语句,表示更新表user中指定id记录的name属性
    sql = "update user_info set name = %s where id = (%s);"  # 其中%s为mysql占位符
    data = [("update1", 1), ("update2", 2)]
    db.execute(sql, data)

    return resp.success()

