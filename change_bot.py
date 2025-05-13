import os
import subprocess
import openai
import datetime
import time
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# === Load environment variables ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GIT_USERNAME = os.getenv("GIT_USERNAME")
GIT_TOKEN = os.getenv("GIT_TOKEN")

# === Configuration ===
REPO_PATH = "/home/notime/Desktop/LeetCode"
REPO_NAME = "LeetCode_EasyQuiz"
REPO_HOST = "192.168.64.7:3000"
CHANGELOG_DIR = os.path.join(REPO_PATH, "changelog")
FILE_TYPES = (".py", ".txt", ".md", ".js")  # watch these file types

REMOTE_REPO_URL = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{REPO_HOST}/noclout/{REPO_NAME}.git"

def run_git(args):
    return subprocess.run(["git"] + args, cwd=REPO_PATH, text=True, capture_output=True, check=False)

def get_git_diff():
    result = run_git(["diff", "--cached", "--"] + list(FILE_TYPES))
    return result.stdout.strip()

def explain_diff(diff_text):
    if not diff_text:
        return "No changes detected."

    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    MAX_CHARS = 12000
    if len(diff_text) > MAX_CHARS:
        diff_text = diff_text[:MAX_CHARS] + "\n\n[Truncated due to size limits]"

    prompt = f"Explain the following git diff:\n\n{diff_text}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who explains code changes."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
    )
    return response.choices[0].message.content

def commit_and_push(message):
    run_git(["add", "."])
    run_git(["commit", "-m", message])
    run_git(["push", "origin", "main"])

class ChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory or not event.src_path.endswith(FILE_TYPES):
            return

        print(f"🔍 Detected change: {event.src_path}")
        time.sleep(2)  # small delay for save to complete
        run_git(["remote", "set-url", "origin", REMOTE_REPO_URL])
        run_git(["add", "."])

        diff = get_git_diff()
        explanation = explain_diff(diff)

        if explanation != "No changes detected.":
            os.makedirs(CHANGELOG_DIR, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = os.path.join(CHANGELOG_DIR, f"explanation_{timestamp}.md")
            with open(log_file, "w") as f:
                f.write("# Explanation of Changes\n\n")
                f.write(explanation)

            run_git(["add", log_file])
            commit_and_push(f"Auto commit with GPT explanation @ {timestamp}")
            print(f"✅ Change explained and pushed.")
        else:
            print("ℹ️ No real change detected.")

def main():
    os.chdir(REPO_PATH)
    observer = Observer()
    handler = ChangeHandler()
    observer.schedule(handler, path=REPO_PATH, recursive=True)
    observer.start()
    print("👀 Watching for changes in your repo...")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
