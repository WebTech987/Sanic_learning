from sanic import Sanic
from sanic.response import json
from sanic.response import file 
import pandas as pd
import numpy as np

app = Sanic("file_transform")

@app.route("/file_convert_csv", methods = ["POST"])
async def convert_to_csv(request):
    file = request.files.get("file")
    if file :
    #   file_name = file.name
        file_body = file.body

        data = pd.read_excel(file_body)

        data["number"] = 5
        new_file = data.to_csv()

        #Return the modified CSV file for download
        return file(new_file, headers={"Content-Disposition": "attachment;filename=modified_file.csv"})
    else:
        return json({"error":"No file"}, status = 400)

if __name__ == "__main__" :
    app.run(host = "127.0.0.1", port = 8000)


