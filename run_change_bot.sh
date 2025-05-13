#!/bin/bash

cd /home/notime/Desktop/LeetCode
source /home/notime/Desktop/LeetCode/myenv/bin/activate

while true
do
  echo "🕒 Running change_bot at $(date)"
  python3 change_bot.py
  echo "✅ Done. Waiting 30 minutes..."
  sleep 1800  # 1800 seconds = 30 minutes
done
