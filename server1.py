from dbm import _Database
from sanic import Sanic

app = Sanic(name = "Application name")

#Most applications will have the need to share/reuse data or objects across different parts of the code base.
# we use DB-connections to connect the different sanic applications/api


app.ctx.db = _Database()