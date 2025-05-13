import os
import subprocess
import openai
import datetime
from dotenv import load_dotenv

# === Load environment variables ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# === Configuration ===
REPO_PATH = "/home/notime/Desktop/LeetCode"
REMOTE_REPO_URL = "http://192.168.64.7:3000/noclout/LeetCode_EasyQuiz"
CHANGELOG_DIR = os.path.join(REPO_PATH, "changelog")

# === Utilities ===
def run_git(args):
    return subprocess.run(["git"] + args, cwd=REPO_PATH, text=True, capture_output=True, check=False)

def get_git_diff():
    # Only include staged changes to .py files
    result = run_git(["diff", "--cached", "--", "*.py"])
    return result.stdout.strip()

def explain_diff(diff_text):
    if not diff_text:
        return "No changes detected."

    # Truncate to approx 12,000 characters (~3,000 tokens)
    MAX_CHARS = 12000
    if len(diff_text) > MAX_CHARS:
        diff_text = diff_text[:MAX_CHARS] + "\n\n[Truncated due to size limits]"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)

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
    run_git(["push", "origin", "main"])  # Update if you're using a different branch

# === Main Bot Logic ===
def main():
    os.chdir(REPO_PATH)
    run_git(["remote", "set-url", "origin", REMOTE_REPO_URL])  # Ensure remote is set

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
        print(f"✅ Explanation saved and pushed.")
    else:
        print("ℹ️ No changes detected to commit.")

if __name__ == "__main__":
    main()
