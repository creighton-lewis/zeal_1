#!/usr/bin/env python3
# ------------------------------------------------------------------
# A **single, tidy CLI** that can:
#   1️⃣  Download the CVE markdown file from Trickest
#   2️⃣  Pull the CVE details from cve.circl.lu and save them as YAML
#   3️⃣  Do both of the above in one run
# ------------------------------------------------------------------

import os
import sys
import requests
import yaml
from rich.console import Console
from results import move_file              # <- helper that copies the file to `../results/`

console = Console()

# ------------------------------------------------------------------
# 1️⃣  Download the Markdown file for a CVE
# ------------------------------------------------------------------
def download_cve_md(cve_id: str) -> None:
    """Download `…/CVE‑<YEAR>‑<NNN>.md` and store it in `../results/`."""
    # ---- Normalise the id --------------------------------------------
    if not cve_id.upper().startswith("CVE-"):
        cve_id = f"CVE-{cve_id}"

    year = cve_id.split("-")[1]
    url  = f"https://raw.githubusercontent.com/trickest/cve/refs/heads/main/{year}/{cve_id}.md"

    resp = requests.get(url)
    if resp.status_code == 404:
        console.print(f"[red]❌  CVE {cve_id} not found on Trickest[/red]")
        return

    local_file = f"{cve_id}.md"
    with open(local_file, "wb") as fh:
        fh.write(resp.content)

    console.print(f"[green]✅  Downloaded {cve_id}.md[/green]")
    move_file(local_file)  # copy to ../results/
    console.print(f"[bold]✓  Moved to {os.path.abspath(os.path.join('..', 'results'))}[/bold]")

# ------------------------------------------------------------------
# 2️⃣  Fetch CVE details from cve.circl.lu
# ------------------------------------------------------------------
def fetch_cve_details(cve_id: str) -> None:
    """Get the CVE JSON, save it as YAML, and show a short summary."""
    if not cve_id.upper().startswith("CVE-"):
        cve_id = f"CVE-{cve_id}"

    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    console.print(f"Fetching {cve_id} …")

    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        data = r.json()

        yaml_path = f"{cve_id}_file.yaml"
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, sort_keys=False)

        console.print(f"[green]✓  YAML written to {yaml_path}[/green]")

        summary = data.get("summary", "No summary available.")
        console.print(f"\n[bold magenta]Summary:[/bold magenta]\n{summary}")

    except requests.RequestException as exc:
        console.print(f"[bold red]❌  Failed to fetch {cve_id}[/bold red] ({exc})")

# ------------------------------------------------------------------
# 3️⃣  CLI driver
# ------------------------------------------------------------------
def main() -> None:
    if len(sys.argv) < 2:
        console.print(
            "\nUsage:\n  cve_tool.py <CVE-ID> [--md|--json|--both]\n",
            style="bold cyan"
        )
        sys.exit(1)

    cve_id = sys.argv[1]
    mode = "--both" if len(sys.argv) < 3 else sys.argv[2].lower()

    if mode in ("--md", "--both"):
        download_cve_md(cve_id)

    if mode in ("--json", "--both"):
        fetch_cve_details(cve_id)

    if mode not in ("--md", "--json", "--both"):
        console.print("[red]❌  Unknown option. Use --md, --json or --both[/red]")

if __name__ == "__main__":
    main()
