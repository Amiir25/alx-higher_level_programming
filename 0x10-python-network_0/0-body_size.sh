#!/bin/bash
# Takes a URL, sends a request to that URL and displays the size of the body
curl -s "$1" -o /dev/null -w '%{size_download}\n'
