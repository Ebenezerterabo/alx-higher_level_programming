#!/bin/bash
# A script that takes in a URL and displays the size of the body in bytes
curl -s "$1" | wc -c
