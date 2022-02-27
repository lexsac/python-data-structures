def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    new_list = []
    idx = 0

    while idx < len(lst):
        new_list.append(lst[idx])
        idx += 2
    
    return new_list
