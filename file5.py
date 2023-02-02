#dumping -- dump function
#The code directly saves or downloads the file into csv format------->used the dumper function here

import io
from sanic import Sanic
from sanic.response import text
import csv

app = Sanic(__name__)


#dump function to return or dump the file into csv format
def custom_csv_dumper(data):
    csv_file = io.StringIO()
    writer = csv.writer(csv_file)
    writer.writerow(data.keys())
    writer.writerows(zip(*data.values()))
    return csv_file.getvalue()

@app.route("/")
async def test(request):
    data = {"column1": [1,2,3], "column2": [4,5,6]}
    return text(custom_csv_dumper(data), content_type="text/csv")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)