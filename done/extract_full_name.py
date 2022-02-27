def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [{'first': 'Ada', 'last': 'Lovelace'}, {'first': 'Grace', 'last': 'Hopper'},]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    new_list = []

    for each_dict in people:
        first_name = each_dict['first']
        last_name = each_dict['last']
        first_last = (f"{first_name} {last_name}")
        new_list.append(first_last)
    
    return new_list