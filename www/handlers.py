from models import User
from coroweb import get
import asyncio

@get('/')
async def index():
    users = await User.findAll()
    return {
        '__template__':'test.html',
        'users':users
    }