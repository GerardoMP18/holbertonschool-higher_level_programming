#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl $1 -sX POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD'
