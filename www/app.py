import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

# 创建了一个 index视图
# 定义服务器响应请求的的返回为 "Awesome Python Web"
async def index(request):
    return web.Response(body=b'<h1>Awesome Python Web</h1>', content_type='text/html')

## 建立服务器应用，持续监听本地9000端口的http请求，对首页"/"进行响应
def init():
    app = web.Application()
    app.router.add_get('/', index)
    web.run_app(app, host='127.0.0.1', port=9000)
    logging.info('server started at http://127.0.0.1:9000')

if __name__=='__main__':
    init()
