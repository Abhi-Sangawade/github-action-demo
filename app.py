from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>AI DevOps App</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family:Arial,sans-serif; background:#0f172a; color:white; min-height:100vh; display:flex; justify-content:center; align-items:center; }
        .container { max-width:700px; width:90%; }
        .header { text-align:center; margin-bottom:40px; }
        .badge { background:#7c3aed; font-size:12px; padding:4px 16px; border-radius:20px; display:inline-block; margin-bottom:16px; }
        h1 { font-size:32px; margin-bottom:8px; }
        .subtitle { color:#94a3b8; font-size:16px; }
        .cards { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:24px; }
        .card { background:#1e293b; border:1px solid #334155; border-radius:12px; padding:20px; text-align:center; }
        .card-icon { font-size:24px; margin-bottom:8px; }
        .card-title { font-size:13px; color:#94a3b8; margin-bottom:4px; }
        .card-value { font-size:20px; font-weight:bold; color:#a78bfa; }
        .status { background:#1e293b; border:1px solid #334155; border-radius:12px; padding:20px; margin-bottom:20px; }
        .status-row { display:flex; justify-content:space-between; align-items:center; padding:8px 0; border-bottom:1px solid #1e293b33; }
        .status-row:last-child { border-bottom:none; }
        .dot { width:8px; height:8px; border-radius:50%; background:#22c55e; display:inline-block; margin-right:8px; }
        .stack { display:flex; flex-wrap:wrap; gap:8px; justify-content:center; }
        .tag { background:#0f172a; border:1px solid #334155; border-radius:6px; padding:5px 14px; font-size:12px; color:#38bdf8; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="badge">AI DevOps Pipeline</div>
            <h1>Deployed to AWS EC2</h1>
            <p class="subtitle">Auto-deployed via GitHub Actions + Docker + AI Agent</p>
        </div>
        <div class="cards">
            <div class="card">
                <div class="card-icon">🤖</div>
                <div class="card-title">AI Agent</div>
                <div class="card-value">Active</div>
            </div>
            <div class="card">
                <div class="card-icon">🚀</div>
                <div class="card-title">Pipeline</div>
                <div class="card-value">Live</div>
            </div>
            <div class="card">
                <div class="card-icon">☁️</div>
                <div class="card-title">Cloud</div>
                <div class="card-value">AWS EC2</div>
            </div>
        </div>
        <div class="status">
            <div class="status-row"><span><span class="dot"></span>Flask App</span><span style="color:#22c55e">Running</span></div>
            <div class="status-row"><span><span class="dot"></span>Docker Container</span><span style="color:#22c55e">Healthy</span></div>
            <div class="status-row"><span><span class="dot"></span>AI Agent</span><span style="color:#22c55e">Monitoring</span></div>
            <div class="status-row"><span><span class="dot"></span>CI/CD Pipeline</span><span style="color:#22c55e">Ready</span></div>
        </div>
        <div class="stack">
            <span class="tag">GitHub Actions</span>
            <span class="tag">Docker</span>
            <span class="tag">AWS EC2</span>
            <span class="tag">Python Flask</span>
            <span class="tag">AI Agent</span>
            <span class="tag">MLOps</span>
        </div>
    </div>
</body>
</html>
"""

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": str(datetime.datetime.now()),
        "version": "2.0",
        "ai_agent": "active"
    })

@app.route("/api/info")
def info():
    return jsonify({
        "app": "AI DevOps Pipeline",
        "environment": os.getenv("ENV", "production"),
        "deployed_via": "GitHub Actions + Docker + AI Agent",
        "cloud": "AWS EC2",
        "stack": ["Flask", "Docker", "GitHub Actions", "AWS", "AI Agent"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)