#!/bin/sh
USER="ctf"
EXEC="python3 ./chall.py"
PORT=1337

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr,su="$USER"
