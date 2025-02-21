def remove_duplicates_by_property(dict_list: list[dict], property: str) -> list[dict]:
    """
    Remove duplicates from a list of dictionary based on property name

    >>> data = [{'author': 'John', 'country': 'us'},
    ...         {'author': 'John', 'country': 'us'},
    ...         {'author': 'Mike', 'country': 'us'},
    ...         {'author': 'Mike', 'country': 'us'}]
    >>> expected = [{'author': 'John', 'country': 'us'},
    ...             {'author': 'Mike', 'country': 'us'}]
    >>> result = remove_duplicates_by_property(data, "author")
    >>> result == expected
    True
    """
    seen = set()
    unique_dicts = []
    for d in dict_list:
        value = d[property]
        if value not in seen:
            seen.add(value)
            unique_dicts.append(d) 
    return unique_dicts