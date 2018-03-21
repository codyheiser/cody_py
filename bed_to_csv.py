# Turn .bed file into readable .csv
#   metadata columns split out and headers appended

import argparse
import pandas as pd


def read_bed(bedfilepath):
    """
    read bed file into pandas dataframe and assign header names
    default columns are 'contig','start','stop','meta'
    """
    bed = pd.read_table(bedfilepath, names=['contig','start','stop','meta'])
    return bed


def reformat_bed(bedtable):
    """
    split out metadata of bed file loaded as pd.df using read_bed
    name new columns based on info contained in original metadata column
    delimiter of metadata is ';' by default
    """
    # get names of metadata columns you're gonna make
    newcols = bedtable['meta'].str.split(';', expand = True).ix[0].str.split('=', expand = True)[0]
    
    # get metadata into separate columns
    bedtable[newcols] = bedtable['meta'].str.split(';', expand = True)
    
    # get rid of data names from columns broken out of meta entries
    for i in newcols:
        bedtable[i] = bedtable[i].str.split('=',expand = True)[1]
        
    bedtable.drop('meta', axis=1, inplace = True) # drop metadata column
    
    return bedtable


def to_csv(table, outfile):
    """write pandas dataframe to csv file"""
    table.to_csv(outfile, encoding='utf-8', index=False, header=True)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reformat a .bed file into parsed .csv file')
    parser.add_argument('outfile', help='output filename')
    parser.add_argument('-b', '--bed', help='Amplicon Bed File', required=True)
    args = parser.parse_args()

    to_csv(reformat_bed(read_bed(args.bed)), args.outfile)
    
