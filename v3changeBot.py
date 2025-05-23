import os
import subprocess
import datetime
import openai
from dotenv import load_dotenv

# === Load credentials ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GIT_USERNAME = os.getenv("GIT_USERNAME")
GIT_TOKEN = os.getenv("GIT_TOKEN")
REPO_HOST = os.getenv("REPO_HOST")
REPO_NAME = os.getenv("REPO_NAME")

REPO_PATH = "/home/notime/Desktop/LeetCode"
REMOTE_REPO_URL = f"http://{GIT_USERNAME}:{GIT_TOKEN}@{REPO_HOST}/noclout/{REPO_NAME}.git"

openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

def run_git(args):
    return subprocess.run(["git"] + args, cwd=REPO_PATH, text=True, capture_output=True, check=False)

def get_git_diff():
    result = run_git(["diff", "--cached" , "--", "*.py", "*.md", "*.txt" ,"SQL/*" , "java_only/*"])
    return result.stdout.strip()

def generate_short_commit_message(diff_text):
    if not diff_text:
        return None
    prompt = f"Write a short Git commit message (max 10 words) summarizing this diff:\n\n{diff_text}"
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a commit message assistant. Keep messages concise and helpful."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=40,
    )
    return response.choices[0].message.content.strip()

def commit_and_push(message):
    run_git(["add", "."])
    run_git(["commit", "-m", message])
    run_git(["remote", "set-url", "origin", REMOTE_REPO_URL])
    run_git(["push", "origin", "main"])
    print(f"✅ Pushed with commit: {message}")

def main():
    os.chdir(REPO_PATH)
    run_git(["add", "."])
    diff = get_git_diff()

    if not diff:
        print("ℹ️ No staged changes detected.")
        return

    commit_msg = generate_short_commit_message(diff)
    if commit_msg:
        commit_and_push(commit_msg)
    else:
        print("⚠️ Could not generate commit message.")

if __name__ == "__main__":
    main()

