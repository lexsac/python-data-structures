def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    newlst = []

    for item in lst: 
        if bool(item):
            newlst.append(item)
    return newlst
