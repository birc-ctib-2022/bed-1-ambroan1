"""Tool for cleaning up a BED file.""" # ?

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    parse_line, print_line
)
from query import Table


def main() -> None:
    """Run the program."""  # a doctest wouldn't make sense as the input/outputs come from the user
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this  
                           metavar='output',  # name used in help text         
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    # FIXME: put your code here
    
    table = Table()

    for line in args.bed:   # read bed file 
        table.add_line(parse_line(line))  

    for line in args.query: # read query file
        lst = line.split("\t")
        chrom = table.get_chrom(lst[0]) 
        for bed_line in chrom:
            if bed_line.chrom_start >= int(lst[1]) and bed_line.chrom_end <= int(lst[2]): 
                print_line(bed_line, args.outfile)

    #args.outfile.close()



if __name__ == '__main__':
    main()