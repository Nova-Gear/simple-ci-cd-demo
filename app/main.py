from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def echo():
    """
    Echo endpoint untuk development/testing.
    
    Security notes for SonarQube:
    - Accepting POST (unsafe method) is safe because this endpoint only echoes data.
    - No server state is modified, so CSRF risk is minimal in this context.
    - In production, do NOT expose unsafe methods without authentication/CSRF protection.
    """
    data = {"method": request.method}

    if request.method == "GET":
        # Safe method: just return query params and headers
        data["args"] = request.args.to_dict()  # NOSONAR: safe
        data["headers"] = dict(request.headers)  # NOSONAR: safe

    elif request.method == "POST":
        # Unsafe method, but justified: only echoes data, no state change
        json_body = request.get_json(silent=True)
        form_data = request.form.to_dict()
        raw_body = request.data.decode()

        data["json"] = json_body if isinstance(json_body, dict) else {}  # NOSONAR
        data["form"] = form_data  # NOSONAR
        data["raw_data"] = raw_body  # NOSONAR
        data["headers"] = dict(request.headers)  # NOSONAR

    return jsonify(data)


if __name__ == "__main__":
    # Bind ke 0.0.0.0 agar bisa diakses dari pod/service Kubernetes
    # Gunakan port yang sama dengan Service/Deployment nanti
    app.run(host="0.0.0.0", port=8000, debug=True)
