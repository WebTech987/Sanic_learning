from sanic import Sanic
from sanic.response import html

app = Sanic(__name__)


@app.route("/")
async def handler(request):
    return html('<!DOCTYPE html><html lang="en"><meta charset="UTF-8"><div>Hi Sir😎</div>')