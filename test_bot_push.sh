#!/bin/bash

# === Configuration ===
REPO_PATH="/home/notime/Desktop/LeetCode"
TEST_FILE="bot_test_$(date +%s).txt"
LOG_FILE="$REPO_PATH/bot_cron.log"
WAIT_SECONDS=60

# === Step 1: Create a test file ===
cd "$REPO_PATH" || exit 1
echo "This is a test file created at $(date)" > "$TEST_FILE"
echo "📝 Test file created: $TEST_FILE"

# === Step 2: Wait for bot to detect and push ===
echo "⏳ Waiting up to $WAIT_SECONDS seconds for bot to process..."
sleep $WAIT_SECONDS

# Optional: check if changelog was updated (optional)
LATEST_LOG=$(ls -t "$REPO_PATH/changelog" 2>/dev/null | head -n 1)
if [ -f "$REPO_PATH/changelog/$LATEST_LOG" ]; then
  echo "✅ Change explanation detected in changelog: $LATEST_LOG"
else
  echo "⚠️ No explanation log found. Bot might not have triggered."
fi

# === Step 3: Delete the test file ===
rm "$TEST_FILE"
git add "$TEST_FILE"
git commit -m "Remove test file $TEST_FILE"
git push
echo "🧹 Test file cleaned up and changes pushed."

exit 0
