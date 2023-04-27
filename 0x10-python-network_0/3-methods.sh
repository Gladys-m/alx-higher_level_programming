#!/bin/bash
#bash script that displays all HTTP methods 
curl -sI "$1" | awk '/Allow:/ {print $2}'
