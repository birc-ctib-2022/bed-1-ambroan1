from bed import (
    parse_line, print_line
)
from query import Table

from query_bed import main

def test_query_bed() -> None:
    "Testing query bed."
    main() # "large.bed","query-1.txt","output-1.txt"
    assert("output-1.txt" == "expected-1.txt")

