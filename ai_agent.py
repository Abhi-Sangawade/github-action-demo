import requests
import subprocess
import datetime
import time
import json
import os

APP_URL = os.getenv("APP_URL", "http://localhost:5000")
LOG_FILE = "agent_log.json"

def log(action, status, detail=""):
    entry = {
        "time": str(datetime.datetime.now()),
        "action": action,
        "status": status,
        "detail": detail
    }
    print(f"[AI AGENT] {entry}")
    logs = []
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        pass
    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-50:], f, indent=2)

def check_health():
    try:
        res = requests.get(f"{APP_URL}/health", timeout=5)
        if res.status_code == 200:
            log("health_check", "pass", "App is healthy")
            return True
        else:
            log("health_check", "fail", f"Status code: {res.status_code}")
            return False
    except Exception as e:
        log("health_check", "fail", str(e))
        return False

def restart_container():
    log("auto_fix", "started", "Restarting container")
    subprocess.run(["docker", "stop", "my-app"], capture_output=True)
    subprocess.run(["docker", "rm", "my-app"], capture_output=True)
    result = subprocess.run([
        "docker", "run", "-d",
        "--name", "my-app",
        "-p", "80:5000",
        f"{os.getenv('DOCKER_USERNAME', 'user')}/my-app:latest"
    ], capture_output=True, text=True)
    if result.returncode == 0:
        log("auto_fix", "success", "Container restarted")
    else:
        log("auto_fix", "failed", result.stderr)

def check_container_running():
    result = subprocess.run(
        ["docker", "ps", "--filter", "name=my-app", "--format", "{{.Names}}"],
        capture_output=True, text=True
    )
    running = "my-app" in result.stdout
    log("container_check", "running" if running else "stopped")
    return running

def pull_latest_image():
    log("image_pull", "started", "Pulling latest image from Docker Hub")
    result = subprocess.run(
        ["docker", "pull", f"{os.getenv('DOCKER_USERNAME', 'user')}/my-app:latest"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        log("image_pull", "success")
    else:
        log("image_pull", "failed", result.stderr)

def run_agent():
    log("agent", "started", "AI Agent monitoring started")
    fail_count = 0

    while True:
        container_ok = check_container_running()
        if not container_ok:
            log("decision", "container_down", "Auto-restarting")
            pull_latest_image()
            restart_container()
            fail_count += 1
        else:
            health_ok = check_health()
            if not health_ok:
                fail_count += 1
                log("decision", f"health_fail_{fail_count}", "App not responding")
                if fail_count >= 3:
                    log("decision", "critical", "3 failures — pulling latest and restarting")
                    pull_latest_image()
                    restart_container()
                    fail_count = 0
            else:
                fail_count = 0

        time.sleep(30)

if __name__ == "__main__":
    run_agent()