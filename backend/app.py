from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok", "message": "Financial Management API"})


@app.route("/api/health")
def api_health():
    """API health check endpoint"""
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

