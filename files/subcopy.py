#!/usr/bin/env python3
# ------------------------------------------------------------
#  A tiny, “sub‑domain enumerator” helper that uses
#  ffuf + two helper scripts and moves the output into a
#  shared directory.
# ------------------------------------------------------------

import os
import subprocess
from pathlib import Path

from rich.console import Console
from colorama import Fore

# the helper that actually moves the files
from results_copy import move_file

console = Console()

# -----------------------------------------------------------------
#  Utilities (used in the CLI part)
# -----------------------------------------------------------------
def clear_console() -> None:
    """Clear the terminal screen (cross‑platform)."""
    os.system("cls" if os.name == "nt" else "clear")

# -----------------------------------------------------------------
#  Main helper – the class that does the enumeration
# -----------------------------------------------------------------
class SubFind:

    def __init__(self) -> None:
        self.target = console.input("Enter target domain: ").strip()
        self.work_dir = Path.cwd()
        self.wl_path = self.work_dir / "wordlists" / "sub_list"
        self._set_filenames()

    def _set_filenames(self) -> None:
        t = self.target
        self.dnsbrute_file = self.work_dir / f"{t}_dnsbrute"
        self.subdomains_file = self.work_dir / f"{t}_subdomains"
        self.ffuf_file = self.work_dir / f"{t}_ffuf"

    # -----------------------------------------------------------------
    #  Step 1 – run ffuf
    # -----------------------------------------------------------------
    def _run_ffuf(self) -> None:
        console.print("[bold cyan]Running ffuf…[/bold cyan]")

        ffuf_cmd = [
            "ffuf",
            "-w", f"{self.wl_path}:SUB",
            "-u", f"https://SUB.{self.target}",
            "-maxtime", "30",
            "-t", "100",
            "-s",
            "-of", "md",
            "-o", str(self.ffuf_file),
            "-mc", "200-299,302,307",
            "-H", "User-Agent: Mozilla/5.0",
        ]
        subprocess.run(ffuf_cmd, check=True)

    # -----------------------------------------------------------------
    #  Step 2 – post‑process the ffuf output
    # -----------------------------------------------------------------
    def _extract_urls(self) -> None:
        try:
            console.print("[white]Extracting URLs…[/white]")
            subprocess.run(
                ["./url_extract.sh", str(self.ffuf_file)],
                stdout=open(self.subdomains_file, "a"),
                check=True,
            )
        except Exception:
            console.print("[red]❌  Unable to extract URLs.[/red]")

    def _check_active(self) -> None:
        try:
            console.print("[white]Checking active URLs…[/white]")
            subprocess.run(
                ["chmod", "700", "url_active.sh"],
                check=True,
            )
            subprocess.run(
                ["./url_active.sh", str(self.subdomains_file)],
                check=True,
            )
        except Exception:
            console.print("[red]❌  Unable to check active URLs.[/red]")

    # -----------------------------------------------------------------
    #  Step 3 – tidy up & move files
    # -----------------------------------------------------------------
    def finalize(self) -> None:
        console.print(f"Subdomains stored in [green]{self.subdomains_file}[/green]")
        move_file(self.subdomains_file)
        move_file(self.ffuf_file)
        move_file(self.dnsbrute_file)

    # -----------------------------------------------------------------
    #  Public entry point for the class
    # -----------------------------------------------------------------
    def run(self) -> None:
        self._run_ffuf()
        self._extract_urls()
        self._check_active()
        self.finalize()


# -----------------------------------------------------------------
#  Small wrapper that launches the helper
# -----------------------------------------------------------------
def main() -> None:
    try:
        SubFind().run()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user.[/red]")


if __name__ == "__main__":
    main()
