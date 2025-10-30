#!/usr/bin/env python3
"""
url_extractor.py – Pull URLs that start with http[s]:// and end in a common TLD.

New feature: `-s` / `--strip-http`  —  removes the leading http:// or https://
from each matched URL before output.

Author:  Your Name
"""

import argparse
import re
import sys
from typing import Iterable, List, Set

# ------------------------------------------------------------------
# 1.  Regex – explanation
# ------------------------------------------------------------------
URL_RE = re.compile(
    r"https?://(?:[A-Za-z0-9-]+\.)+"
    r"(?:com|net|org|edu|gov|io|info|biz|co|us|uk|de|jp|fr|au|ca|cn|ru|info|com\.org|nl|es|it|pl|br|in|mil|mobi|asia|int|tv|cc|jobs|me|name|movie|space|shop|art|tech|jobs)\b"
    r"[^\s]*",
    flags=re.IGNORECASE,
)

# ------------------------------------------------------------------
# 2.  Helpers
# ------------------------------------------------------------------
def extract_urls(text: str) -> List[str]:
    """Return a *unique* list of URLs that match the pattern."""
    matches = URL_RE.findall(text)
    return list(dict.fromkeys(matches))

def read_input(path: str | None) -> str:
    """Read the full file content or stdin."""
    if path is None:
        return sys.stdin.read()
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def strip_scheme(urls: Iterable[str]) -> List[str]:
    """Remove http:// or https:// from each URL."""
    return [re.sub(r'^https?://', '', u, flags=re.IGNORECASE) for u in urls]

def write_output(urls: Iterable[str], out: str | None):
    """Write URLs to stdout or a file."""
    out_handle = sys.stdout
    if out is not None:
        out_handle = open(out, "w", encoding="utf-8")
    for url in urls:
        out_handle.write(url + "\n")
    if out is not None:
        out_handle.close()

# ------------------------------------------------------------------
# 3.  Command‑line interface
# ------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Extract URLs that start with http:// or https:// and end with a common TLD.\n"
                    "Add -s / --strip-http to drop the leading scheme."
    )
    parser.add_argument("-i", "--input", default=None,
                        help="Input file (default: stdin)")
    parser.add_argument("-o", "--output", default=None,
                        help="Output file (default: stdout)")
    parser.add_argument("-s", "--strip-http", action="store_true",
                        help="Strip http:// or https:// from each URL")

    args = parser.parse_args()

    content = read_input(args.input)
    urls = extract_urls(content)

    if args.strip_http:
        urls = strip_scheme(urls)

    write_output(urls, args.output)

if __name__ == "__main__":
    main()
