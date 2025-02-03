#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond 'You got me!'.
curl -sX GET 0.0.0.0:5000/catch_me
