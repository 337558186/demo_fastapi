from fastapi import APIRouter,Request,Body,Header
import uvicorn
from starlette.responses import HTMLResponse,JSONResponse,FileResponse
from fastapi.templating import Jinja2Templates  # 模板引擎
# 日志组件
from src.component.Logger import logger
# 自定义的响应体
import src.component.APIResponse as resp

# templates路径(注意此处路径写法)
templates = Jinja2Templates(directory="./templates/")
# 创建服务
router = APIRouter()

"""
主页
"""
@router.get("/", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("index.html",context={"request":request})


@router.get("/index", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("index.html",context={"request":request})

"""
登录页
"""
@router.get("/login",response_class=HTMLResponse)
async def login(request:Request):

    logger.info("跳转登录页")
    return templates.TemplateResponse("login.html",context={"request":request})

"""
注册页
"""
@router.get("/register",response_class=HTMLResponse)
async def login(request:Request):

    logger.info("跳转注册页")
    return templates.TemplateResponse("register.html",context={"request":request})



