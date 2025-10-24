#!/usr/bin/env python3
import time
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn

tasks = [("fetching data", 20), ("processing…", 50), ("finalising…", 30)]

with Progress(
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TimeElapsedColumn(),
) as progress:
    for name, total in tasks:
        task_id = progress.add_task(name, total=total)

        # Simulating work: loop `total` times
        for _ in range(total):
            progress.update(task_id, advance=1)
            time.sleep(0.1)   # replace with real work
