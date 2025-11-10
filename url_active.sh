#!/bin/bash

file="$1"
temp_file="temp_active_hosts.txt"

> "$temp_file"
GREEN='\033[0;32m'
RED='\033[0;31m'

NC='\033[0m' # No Color
echo "Checking hosts from '$file'..."

while IFS= read -r host; do
    if [ -z "$host" ]; then
        continue
    fi

echo "Pinging $host..."
if nmap -sn "$host" > /dev/null 2>&1; then
    echo -e "${GREEN}Host $host is active.${NC}"
    echo "$host" >> "$temp_file"

    else
        echo -e "${RED}Host $host is inactive or unreachable.${NC}"
    fi
done < "$file"

mv "$temp_file" "$file"
echo ""
echo "Original file '$file' updated with active hosts."
