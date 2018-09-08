def count_unique(lists):
    """Count the number of distinct elements in a list.

    The list can contain any kind of elements, including duplicates and nulls in any order.

    (In PyDoc there are different formats for parameters and returns. Use what you prefer.)

    :param list:  list of elements to find distinct elements of
    :return: the number of distinct elements in list

    Examples:
    >>> count_unique(['a','b','b','b','a','c','c'])
    3
    >>> count_unique(['a','a','a','a'])
    1
    >>> count_unique([ ])
    0
    """
    lists = set(lists)
    lists = list(lists)
    return  len(lists)

def binary_search(lists, element):
    """Search index of the matching element in a list.

    The list and element can contain any kind of elements.

    :param list:  list of elements to find where is index of element.
    :return: the index of element in list.

    Example:
    >>> binary_search(['a','b','b','b','a','c','c'],"c")
    2
    >>> binary_search(['a','b','b','b','a','c','c'],"d")
    -1
    >>> binary_search(['a','b','b','b','a','c','c'],1)
    -1
    """

    lists = set(lists)
    newlist = list(lists)
    sorts = sorted(newlist)
    if element in lists:
        return sorts.index(element)
    elif element not in lists:
        return -1
    else:
        raise TypeError("Search element must not be none")

