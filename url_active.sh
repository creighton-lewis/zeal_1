#!/bin/bash

file="$1"
temp_file="temp_active_hosts.txt"

> "$temp_file"

echo "Checking hosts from '$file'..."

while IFS= read -r host; do
    if [ -z "$host" ]; then
        continue
    fi

    echo "Pinging $host..."
    if nmap -sn  "$host" > /dev/null 2>&1; then
        echo "Host $host is active."
        echo "$host" >> "$temp_file"
    else
        echo "Host $host is inactive or unreachable."
    fi
done < "$file"

mv "$temp_file" "$file"
echo ""
echo "Original file '$file' updated with active hosts."
