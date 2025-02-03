#!/bin/bash
#Sends a JSON POST request to aURL passed as the irst arguement and displays the body o the response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
