from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)


def get_build_info():
    return {
        "environment": os.getenv("ENV", "production"),
        "build_commit": os.getenv("BUILD_COMMIT", "unknown"),
        "build_time": os.getenv("BUILD_TIME", "not available"),
        "build_image": os.getenv("BUILD_IMAGE", "local"),
        "deploy_host": os.getenv("DEPLOY_HOST", "AWS EC2"),
        "app_url": os.getenv("APP_URL", "http://localhost:5000")
    }

@app.route("/")
def home():
    build_info = get_build_info()
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Release Dashboard</title>
    <style>
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{ font-family:Inter,system-ui,sans-serif; background:#0b1120; color:#e2e8f0; min-height:100vh; }}
        .page {{ max-width:1080px; margin:0 auto; padding:40px 24px; }}
        .hero {{ display:grid; gap:24px; grid-template-columns:1.4fr 1fr; align-items:center; margin-bottom:40px; }}
        .hero h1 {{ font-size:3rem; line-height:1.05; color:#f8fafc; }}
        .hero p {{ font-size:1.05rem; color:#94a3b8; max-width:640px; }}
        .badge {{ display:inline-flex; align-items:center; gap:10px; background:#312e81; color:#e0e7ff; border-radius:999px; padding:10px 16px; font-size:.9rem; margin-bottom:18px; }}
        .card-grid {{ display:grid; gap:16px; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); margin-bottom:32px; }}
        .card {{ background:#111827; border:1px solid #23303f; border-radius:18px; padding:24px; }}
        .card h2 {{ font-size:1rem; color:#94a3b8; margin-bottom:10px; text-transform:uppercase; letter-spacing:.08em; }}
        .card p {{ font-size:1.8rem; color:#e0e7ff; font-weight:700; margin:0; }}
        .section {{ margin-bottom:32px; }}
        .section h3 {{ margin-bottom:16px; color:#cbd5e1; }}
        .stack {{ display:flex; flex-wrap:wrap; gap:10px; }}
        .tag {{ background:#111827; border:1px solid #334155; border-radius:999px; padding:10px 14px; font-size:.9rem; color:#38bdf8; }}
        .info-list {{ display:grid; gap:14px; }}
        .info-item {{ display:flex; justify-content:space-between; gap:12px; padding:16px 18px; background:#111827; border:1px solid #23303f; border-radius:14px; }}
        .info-item span:first-child {{ color:#94a3b8; }}
        .info-item span:last-child {{ color:#f8fafc; font-weight:600; }}
    </style>
</head>
<body>
    <div class="page">
        <div class="hero">
            <div>
                <div class="badge">DevOps Release Website</div>
                <h1>AI-powered Build & Deployment Dashboard</h1>
                <p>Track your CI/CD pipeline, Docker image status, and deployment metadata in a single DevOps release dashboard built with Flask.</p>
            </div>
            <div class="card">
                <h2>Release summary</h2>
                <p>Live</p>
            </div>
        </div>

        <div class="card-grid">
            <div class="card">
                <h2>Pipeline</h2>
                <p>GitHub Actions</p>
            </div>
            <div class="card">
                <h2>Runtime</h2>
                <p>Flask + Docker</p>
            </div>
            <div class="card">
                <h2>Cloud</h2>
                <p>{build_info['deploy_host']}</p>
            </div>
            <div class="card">
                <h2>Environment</h2>
                <p>{build_info['environment'].title()}</p>
            </div>
        </div>

        <div class="section">
            <h3>Deployment metadata</h3>
            <div class="info-list">
                <div class="info-item"><span>Commit</span><span>{build_info['build_commit']}</span></div>
                <div class="info-item"><span>Build time</span><span>{build_info['build_time']}</span></div>
                <div class="info-item"><span>Image tag</span><span>{build_info['build_image']}</span></div>
                <div class="info-item"><span>Application URL</span><span>{build_info['app_url']}</span></div>
            </div>
        </div>

        <div class="section">
            <h3>Available endpoints</h3>
            <div class="stack">
                <span class="tag">/</span>
                <span class="tag">/health</span>
                <span class="tag">/api/info</span>
                <span class="tag">/api/build</span>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "2.1",
        "ai_agent": "active"
    })

@app.route("/api/info")
def info():
    build_info = get_build_info()
    return jsonify({
        "app": "AI DevOps Pipeline",
        "environment": build_info["environment"],
        "deployed_via": "GitHub Actions + Docker + AI Agent",
        "cloud": build_info["deploy_host"],
        "stack": ["Flask", "Docker", "GitHub Actions", "AWS", "AI Agent"]
    })

@app.route("/api/build")
def build_metadata():
    return jsonify(get_build_info())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)