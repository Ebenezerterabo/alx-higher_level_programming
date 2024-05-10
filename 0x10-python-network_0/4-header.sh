#!/bin/bash
# A script that takes in a URL as an argument and assign value to X-School-User-Id
curl -sH "X-School-User-Id: 98" "$1"
