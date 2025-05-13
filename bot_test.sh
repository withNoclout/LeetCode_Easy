#!/bin/bash

# Config
LOG_FILE="/home/notime/Desktop/LeetCode/bot_cron.log"
MAX_AGE_MINUTES=40

# Check if log file exists
if [ ! -f "$LOG_FILE" ]; then
  echo "❌ Log file not found: $LOG_FILE"
  exit 1
fi

# Check last modified time
LAST_MODIFIED=$(stat -c %Y "$LOG_FILE")
CURRENT_TIME=$(date +%s)
AGE=$(( (CURRENT_TIME - LAST_MODIFIED) / 60 ))

if [ "$AGE" -gt "$MAX_AGE_MINUTES" ]; then
  echo "❌ Bot may not be running. Last log update was $AGE minutes ago."
  exit 2
else
  echo "✅ Bot is running smoothly. Last updated $AGE minutes ago."
  exit 0
fi
