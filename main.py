from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

"""
引入子路由
"""
from src.app.user import router as user
from src.app.index import router as index

# 创建服务
app = FastAPI(title="测试文档",docs_url="/my_docs",openapi_url="/my_openapi")
# 挂载静态文件 StaticFiles
app.mount("/static", StaticFiles(directory="./static"), name="static")
# 优化  HTML网页跳转  /templates/login.html
# app.mount("/templates", StaticFiles(directory="./templates/"), name="templates")


"""
路由挂载:将每个 APIRouter 添加到主 FastAPI 应用程序中
"""
app.include_router(index,tags=['主页'])
app.include_router(user, prefix='/user', tags=['用户模块'])

