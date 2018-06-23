import os
import pandas as pd

# IMPORTANT: prevent truncation of long strings by Pandas
#	useful for sequences embedded in dataframes
pd.set_option('display.max_colwidth', -1)

# convert appropriate strings ('TRUE', 'True', 'true') to boolean value (_True_)
def str_to_bool(s):
	'''
	s = string that should be a boolean value (T or F)
	output = corresponding boolean _True_ or _False_
	'''
    if s.title() == 'True':
         return True
    elif s.title() == 'False':
         return False
    else:
         raise ValueError("Cannot convert {} to a bool".format(s))

# count homopolymer repeats in sequence
def max_char_repeats(word):
    '''
    return maximum number of consecutive character repeats in string
    '''
    counts = []
    count = 1
    for a, b in zip(word, word[1:]):
        if a == b:
            count += 1
        else:
            counts.append(count)
            count = 1
    counts.append(count)
    return max(counts)

# read files into pandas dataframe
def read_default(file):
	'''
	take path to any flat file (.txt, .csv) and return pd.dataframe
	'''
	if os.path.splitext(file)[1]=='.csv':
		out = pd.read_csv(file)

	elif os.path.splitext(file)[1]=='.txt':
		out = pd.read_table(file)

	return out

# read all files from a given directory with
def read_all(filetype, startdir = '.', recursive = True):
	'''
	Read in all files of common type from a folder, concatenate by row into pandas dataframe

	filetype = string denoting which file to look for, including globs
	startdir = directory to start looking in
	recursive = search subdirectories?
	'''
	out = pd.dataframe() # initiate df for output
	for dirpath, dirs, files in os.walk(startdir):
		for file in files:
			contents = read_default(os.path.join(dirpath,file))
			contents['file'] = os.path.basename(file)
			out.append(contents)

	return out
