from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>YMB Banking App</title>
    </head>
    <body>
        <h1>Yarrow-Mullein Bank</h1>
        <h2>Banking Application</h2>
        <p>Welcome to the YMB Banking App!</p>
        <p>Student: Harman Nahal</p>
        <p>Module 4 - Docker Assignment</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="ok", application="YMB Banking App")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5090)
