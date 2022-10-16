# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import os
import filecmp

def test_1():
    input_path = "data/large.bed" 
    query_1_path = "data/query-1.txt" 
    expected_1_path = "data/expected-1.txt" 
    outfile_path = "data/output-1.txt"
    os.system("python3 src/query_bed.py " + input_path + " " + query_1_path +" -o" + outfile_path) 
    assert  filecmp.cmp(outfile_path,expected_1_path)
