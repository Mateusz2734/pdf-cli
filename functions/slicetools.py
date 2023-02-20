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


def invert_slices(slices: str, page_count: int) -> str:
    """
    It takes a string of page numbers and page ranges, and returns a string of page numbers that are not
    in the original string

    :param slices: a string of comma-separated numbers and ranges of numbers, e.g. "1,3,5:7,9"
    :type slices: str
    :param page_count: the total number of pages in the document
    :type page_count: int
    :return: The pages that are not in the slices.
    :type return: str
    """
    to_delete = []
    for slice in slices.split(","):
        if ":" in slice:
            left = int(slice.split(":")[0])
            right = int(slice.split(":")[1])+1
            [to_delete.append(str(num)) for num in
                range(left, right) if int(num) <= page_count]
        else:
            to_delete.append(slice)
    pages = [str(i+1) for i in range(page_count)]
    return ",".join(list(filter(lambda x: x not in to_delete, pages)))
