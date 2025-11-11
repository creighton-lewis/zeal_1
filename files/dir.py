import requests # Used if you were to implement custom HTTP requests, but ffuf handles this.
import os
import subprocess
from rich.console import Console
from rich.table import Table

console = Console()

def clear_console():
    """Clears the console window."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Dir_Find:
    @staticmethod
    def dir_enum():
        console.print("FINDING Directory FILES...", style="bold cyan", justify="left")
        
        target = console.input("[bold green]Enter target URL (e.g., example.com):[/bold green] ")
        
        # Basic validation for target
        if not target:
            console.print("[bold red]Target cannot be empty. Exiting.[/bold red]", style="bold red")
            return
        
        # Ensure target doesn't start with http(s):// for ffuf, it adds it later
        if target.startswith("http://"):
            target = target[7:]
        elif target.startswith("https://"):
            target = target[8:]

        dir_list_path = "wordlists/dir_list" # Path to your wordlist
        
        # Check if wordlist exists
        if not os.path.exists(dir_list_path):
            console.print(f"[bold red]Error: Wordlist not found at {dir_list_path}. Exiting.[/bold red]", style="bold red")
            return

        # Use f-string for file_name to embed the target value
        output_file_name = f"{target.replace('.', '_')}_directories" # Replace dots for valid filename

        console.print(f"[bold yellow]Starting FFUF scan on {target} with wordlist {dir_list_path}...[/bold yellow]")

        try:
            # Construct the ffuf command using subprocess for better control
            ffuf_command = [
                "ffuf",
                "-u", f"https://{target}/FUZZ", # Assuming HTTPS, adjust if needed
                "-w", dir_list_path,
                "-t", "100", # Threads
                "-of", "md", # Output format: markdown
                "-o", output_file_name, # Output file
                "-p", "0.10-0.30", # Delay between requests
                "-mc", "200-299" # Match status codes 200-299
            ]
            
            # Execute ffuf command
            ffuf_result = subprocess.run(ffuf_command, capture_output=True, text=True, check=True)
            console.print(f"[bold green]FFUF scan completed. Results saved to {output_file_name}.md[/bold green]")
            # You might want to print ffuf_result.stdout or ffuf_result.stderr for debugging
            
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]FFUF command failed with error:[/bold red] {e}", style="bold red")
            console.print(f"[bold red]FFUF stdout:[/bold red]\n{e.stdout}", style="red")
            console.print(f"[bold red]FFUF stderr:[/bold red]\n{e.stderr}", style="red")
            return
        except FileNotFoundError:
            console.print("[bold red]Error: 'ffuf' command not found. Please ensure ffuf is installed and in your PATH.[/bold red]", style="bold red")
            return
        
        # Execute the external shell script
        shell_script_path = "../url_active.sh"
        if not os.path.exists(shell_script_path):
            console.print(f"[bold red]Error: Shell script not found at {shell_script_path}. Skipping.[/bold red]", style="bold red")
        else:
            console.print(f"[bold yellow]Running external script {shell_script_path} with {output_file_name}.md...[/bold yellow]")
            try:
                # Pass the full filename including extension to the shell script
                script_result = subprocess.run([shell_script_path, f"{output_file_name}.md"], capture_output=True, text=True, check=True)
                console.print("[bold green]External script completed successfully.[/bold green]")
                # console.print(script_result.stdout) # Uncomment to see script output
            except subprocess.CalledProcessError as e:
                console.print(f"[bold red]Shell script failed with error:[/bold red] {e}", style="bold red")
                console.print(f"[bold red]Script stdout:[/bold red]\n{e.stdout}", style="red")
                console.print(f"[bold red]Script stderr:[/bold red]\n{e.stderr}", style="red")
            except FileNotFoundError:
                console.print(f"[bold red]Error: '{shell_script_path}' not found. Please ensure the script exists and is executable.[/bold red]", style="bold red")

        # Import and call move_file
        if os.path(output_file_name) is not None:
            try:
                from results import move_file
                console.print("[bold yellow]Moving output file...[/bold yellow]")
                # Pass the full filename including extension to move_file
                move_file(f"{output_file_name}.md") 
                console.print("[bold green]File moved successfully.[/bold green]")
            except ImportError:
                console.print("[bold red]Error: Could not import 'move_file' from 'results'. Please ensure results.py exists.[/bold red]", style="bold red")
            except Exception as e:
                console.print(f"[bold red]Error during file movement:[/bold red] {e}", style="bold red")
        else:
            console.print("File does not exist")
def main():
    clear_console() # Clear console at start
    try:
        Dir_Find.dir_enum() # Correctly call the static method
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Script interrupted by user. Exiting.[/bold yellow]", style="yellow")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}", style="bold red")

if __name__ == '__main__':
    main()
