#!/bin/bash
# script that takes in a URL and displays all 
# HTTP methods the server will accept.
curl -isX OPTIONS "$1" | grep Allow | cut -d " " -sf2,3,4
