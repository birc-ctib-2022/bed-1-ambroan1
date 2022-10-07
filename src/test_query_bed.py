from bed import (
    parse_line, print_line
)
from query import Table

def test_query_bed() -> None:
    "Testing query bed."

    assert(query_bed("input.bed","output.bed","query-1.txt") == "expected-1.txt")

