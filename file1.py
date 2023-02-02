#   Rest_Api
from sanic import Sanic
from sanic.response import json
#import requests

app = Sanic("Rest_api")


users = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]

@app.route("/users", methods = ['POST'])
async def get_users(request):
    data = request.json
    new_user = {'id' : len(users)+1 , 'name': data['name']}
    users.append(new_user)
    return json({"user":new_user}, status = 201)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)



