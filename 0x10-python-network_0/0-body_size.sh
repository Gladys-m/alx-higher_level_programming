#!/bin/bash
#script that takes in a URL and displays the body size in bytes
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f2
