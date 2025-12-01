from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def echo():
    # Ambil data dari user
    data = {
        "method": request.method,
        "args": request.args.to_dict(),       # query params ?a=1
        "headers": dict(request.headers),     # header
        "json": request.get_json(silent=True),# JSON body
        "form": request.form.to_dict(),       # form data
        "raw_data": request.data.decode()     # raw body
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
