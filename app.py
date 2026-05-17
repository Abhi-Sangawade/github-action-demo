from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>My DevOps App</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 16px;
            padding: 40px 50px;
            text-align: center;
            max-width: 500px;
        }
        .badge {
            background: #22c55e;
            color: white;
            font-size: 12px;
            padding: 4px 14px;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 20px;
        }
        h1 { font-size: 28px; margin-bottom: 10px; }
        p  { color: #94a3b8; font-size: 15px; margin-bottom: 24px; }
        .stack {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .tag {
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 6px 14px;
            font-size: 13px;
            color: #38bdf8;
        }
        .footer {
            margin-top: 28px;
            font-size: 12px;
            color: #475569;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">Live on AWS EC2</div>
        <h1>DevOps Pipeline Working!</h1>
        <p>Deployed automatically via GitHub Actions + Docker</p>
        <div class="stack">
            <span class="tag">GitHub Actions</span>
            <span class="tag">Docker</span>
            <span class="tag">AWS EC2</span>
            <span class="tag">Python Flask</span>
        </div>
        <div class="footer">Push code → auto deploys in seconds</div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)