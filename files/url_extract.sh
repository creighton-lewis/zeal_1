#!/bin/bash 
file="$1"

# Extract:
#   - URLs starting with http, https, ftp
#   - Bare domains like example.com or sub.domain.org
grep -Eo '((https?|ftp)://[a-zA-Z0-9./?=_%-]+|[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})' "$file" \
  | sed 's/[[:punct:]]*$//' \
  | sort -u
