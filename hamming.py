def hamming(s1, s2):
    """calculate the Hamming distance between two strings of the same length"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
