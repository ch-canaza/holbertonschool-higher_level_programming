#!/bin/bash
# script that takes in a URL and displays all
curl -isX OPTIONS "$1" | grep "Allow" | cut -d " " -f2-
