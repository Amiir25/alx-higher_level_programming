#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /dev/null -w "%{http_code}" "http://example.com" | grep -q 200 && curl -s "http://example.com"
