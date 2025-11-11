#!/bin/bash

if [ -z "$1" ] || [ ! -f "$1" ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

file="$1"
temp_file="temp_active_hosts.txt"
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

> "$temp_file"

echo "Checking hosts from '$file'..."
echo ""

while IFS= read -r host; do
    [ -z "$host" ] && continue
    
    echo "Checking $host..."
    
    # Using httpx for comprehensive web service check
    result=$(echo "$host" | httpx -silent -rt -timeout 1 -status-code -mc 200,201,202,203,204,301,302,307,308 -sc 2>/dev/null)
    
    if [ -n "$result" ]; then
        echo -e "${GREEN}Host $host is active. [Status: $result]${NC}"
        echo "$host" >> "$temp_file"
    else
        echo -e "${RED}Host $host is inactive or unreachable.${NC}"
    fi
    
done < "$file"

if [ -s "$temp_file" ]; then
    mv "$temp_file" "$file"
    echo ""
    echo "Original file '$file' updated with active hosts."
else
    echo ""
    echo "No active hosts found."
    rm "$temp_file"
fi
