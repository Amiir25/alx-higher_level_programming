#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond 'You got me!'.
curl -sX POST "http:// 0.0.0.0:5000/catch_me" -d "message=find_me"
