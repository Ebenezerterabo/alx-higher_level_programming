#!/bin/bash
# A script that takes in a URL, sends POST request and display the body response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
