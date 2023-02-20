from typing import List

from pypdf import PageRange


def to_pagerange(slice: str) -> str:
    """
    It takes a string of the form "1:3" or "1" and returns a string of the form "0:2" or "0"

    :param slice: The page range to extract
    :type slice: str
    :return: str
    """
    if ":" in slice:
        slice_list = slice.split(":")
        slice = f"{int(slice_list[0])-1}:{slice_list[1]}"
    else:
        slice = str(int(slice) - 1)
    return PageRange(slice)


def create_pageranges(slices: str) -> List[PageRange]:
    """
    It takes a string of comma-separated slices, and returns a list of PageRange objects

    :param slices: A comma-separated list of page ranges, e.g. "1,3,5,7:10"
    :type slices: str
    :return: A list of PageRange objects.
    """
    return list(map(to_pagerange, slices.split(',')))
