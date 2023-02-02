#File_upload
#this API just takes the file as the input and read the file name and type
from sanic import Sanic
from sanic.response import json
from sanic.request import File


app = Sanic("File_Api")

@app.route("/upload", methods = ["POST"])

async def file_upload(request):
    file = request.files.get("file")
    if file:
        file_name = file.name
        file_body = file.body
        # Do something with the file here, such as saving it to disk or storing it in a database
        return json({"file_name": file_name, "file_size": len(file_body)})
    else:
        return json({"error":"No file"}, status = 400)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)