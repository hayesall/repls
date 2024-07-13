# Copyright © 2024 Alexander L. Hayes
# MIT License

from typing import Any

from rich.box import MINIMAL_HEAVY_HEAD
from rich.console import Console
from rich.pretty import Pretty
from rich.table import Table


def tabprint(data: list[dict[str, Any]]):
    """Pretty-print a `list[dict]`, e.g. one from `csv.DictReader`"""
    if len(data) == 0:
        print("Empty table")
        return None

    table = Table(*data[0].keys(), box=MINIMAL_HEAVY_HEAD)
    for row in data:
        table.add_row(*map(Pretty, row.values()))

    console = Console()
    console.print(table)
