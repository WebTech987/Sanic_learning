#new_file----it takes csv as the input and add the different columns on the data

from sanic import Sanic
from sanic import response
from sanic.response import json, file, text
import io
import csv
import pandas as pd


app = Sanic(__name__)

@app.route("/csv/download")
async def download_csv(request):
    df = pd.DataFrame(request.app.config.get("csv_data")) # Get the DataFrame from app config

    if df is None:
        return json({"error": "No CSV data found"})
    df["number"] = 5     #just added to check whether the API is able to make changes in the data or not
    csv = df.to_csv(index=False)

    async def stream_fn(response):
        response.write(csv)

    return response.HTTPResponse(body=csv, content_type="text/csv")

@app.route("/csv", methods=["POST"])
async def process_csv(request):
    file = request.files.get("file")
    if not file:
        return json({"error": "No file found in request"})

    csv_reader = csv.reader(file.body.decode("utf-8").splitlines())
    header = next(csv_reader)
    data = [dict(zip(header, row)) for row in csv_reader]

    df = pd.DataFrame(data)
    df["new_number"] = 6  #just added to check whether the API is able to make changes in the data or not
    request.app.config["csv_data"] = df.to_dict() # Store the DataFrame in app config

    return json({"data": df.to_dict()})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)