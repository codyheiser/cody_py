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

# move column to first position of Pandas dataframe
def movetofirst(df, cols):
    '''
    move a list of columns "cols" to the first position (left) of dataframe "df"
    '''
    return df[cols+list(collections.OrderedDict.fromkeys([x for x in collections.OrderedDict.fromkeys(list(ce.columns)) if x not in collections.OrderedDict.fromkeys(cols)]).keys())]
