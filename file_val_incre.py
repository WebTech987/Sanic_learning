import io
import csv
from sanic import response
from sanic import Sanic
from sanic.response import file, text

app = Sanic(__name__)

@app.route("/", methods=["GET", "POST"])
async def index(request):
    if request.method == "POST":
        uploaded_file = request.files.get("file")
        if uploaded_file:
            file_stream = io.StringIO(uploaded_file.body.decode("utf-8"))
            reader = csv.reader(file_stream)
            rows = [row for row in reader]
            for i, row in enumerate(rows):
                for j, val in enumerate(row):
#                    if type(val) == int:
 #                       val = val + 1
                    rows[i][j] =  int(val) + 1
 #                   rows[i][j] =  1
            file_stream = io.StringIO()
            writer = csv.writer(file_stream)
            writer.writerows(rows)
            file_stream.seek(0)
            return response.HTTPResponse(
    body=file_stream.read(),
    headers={"Content-Disposition": "attachment;filename=modified.csv"}
)
    return text("""
        <form action="/" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Submit">
        </form>
    """)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)