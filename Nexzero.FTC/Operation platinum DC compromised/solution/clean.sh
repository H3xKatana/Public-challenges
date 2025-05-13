#!/bin/bash

# Specify the input file
input_file="./output"

# Extract each base64-encoded content from the stdout streams
grep -oP '<rsp:Stream Name="stdout"[^>]*>\K[^<]+' "$input_file" | while read -r base64_content; do
  # Decode the base64 content and output it
  echo "Decoded content:"
  echo "$base64_content" | base64 --decode
  echo # Add a new line after each decoded output
done
