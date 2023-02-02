#file_data_dump

from sanic import Sanic
from sanic.response import json, file, text
import io
import csv
import numpy as np
import pandas as pd


app = Sanic("file_direct_dump")

# dump function to return or dump the file into csv format
def custom_csv_dumper(data):
    csv_file = io.StringIO()
    writer = csv.writer(csv_file)
    writer.writerow(data.columns)
    for i in range(len(data)):
        writer.writerow(data.iloc[i])
    return csv_file.getvalue()

@app.route("/csv", methods=["POST"])
async def process_csv(request):
    file = request.files.get("file")
    if not file:
        return json({"error": "No file found in request"})

    csv_reader = csv.reader(file.body.decode("utf-8").splitlines())
    header = next(csv_reader)
    data = [dict(zip(header, row)) for row in csv_reader]

    df = pd.DataFrame(data)
    df["new_number"] = 6  # just added to check whether the API is able to make changes in the data or not
#    request.app.config["csv_data"] = df.to_dict() # Store the DataFrame in app config

    return text(custom_csv_dumper(df), content_type="text/csv")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
