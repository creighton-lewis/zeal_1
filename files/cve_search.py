import os
import requests  # type:ignore
import yaml  # type:ignore
from rich.console import Console  # type:ignore
from rich.table import Table  # type:ignore
from rich.progress import track  # type:ignore
from banner import print_banner

console = Console()

def fetch_cve(cve_id: str):
    """Fetch CVE data from cve.circl.lu API"""
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    console.print(f"Fetching [bold cyan]{cve_id}[/bold cyan] from {url} ...")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Save JSON
        json_path = f"{cve_id}_file.json"
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        console.print(f"[green]✓ Saved JSON file as {json_path}[/green]")

        # Convert to YAML and save
        yaml_path = f"{cve_id}_file.yaml"
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, sort_keys=False)
        console.print(f"[yellow]✓ Saved YAML file as {yaml_path}[/yellow]")

        # ✅ Remove JSON file after conversion
        if os.path.exists(json_path):
            os.remove(json_path)
            console.print(f"[red]✗ Removed temporary JSON file ({json_path})[/red]")

        # Display a short summary
        if "summary" in data:
            console.print(f"\n[bold magenta]Summary:[/bold magenta]\n{data['summary']}")
        else:
            console.print("[red]No summary found in CVE data[/red]")

    except requests.RequestException as e:
        console.print(f"[bold red]Failed to fetch CVE data:[/bold red] {e}")

def main():
    cve_id = console.input("\nEnter CVE ID (e.g. CVE-2023-12345): ")
    fetch_cve(cve_id.strip())

if __name__ == "__main__":
    main()
