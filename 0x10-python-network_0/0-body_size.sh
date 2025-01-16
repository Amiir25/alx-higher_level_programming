#!/usr/bin/bash
# Takes a URL, sends a request to that URL and displays the size of the body

# Check if URL is provided
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Assign the first argument as the URL
URL="$1"

# Send a request and calculate the size of the body
SIZE=$(curl -s "$URL" -o /dev/null -w '%{size_download}')

# Display the size
echo "$SIZE"
