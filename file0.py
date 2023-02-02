#first_sanic
from sanic import Sanic
from sanic.response import json

app = Sanic(name = "first_api")

@app.route("/")
async def test(request):
    return json({"hello" : "Sir"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)