from typing import List
import os
import sys

from pypdf import PdfReader, PdfWriter, PageRange
from pypdf.errors import PdfReadError

from toolABC import Tool
from slicetools import process_slices

sys.path.append('../functions')


class Slicer(Tool):
    def __init__(self, path: str, slices: List[PageRange]) -> None:
        slices = process_slices(slices)
        self.execute(path, slices)

    def execute(self, path: str, slices: List[PageRange]):
        """
        It takes a PDF file and a list of page ranges, and writes a new PDF file with only the pages in
        the ranges
        
        :param path: Path to the PDF file
        :type path: str
        :param slices: The page ranges to extract
        :type slices: List[PageRange]
        """
        DESKTOP = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        filename = os.path.basename(path).split(".")[0]
        out = os.path.join(DESKTOP, f"{filename}-sliced.pdf")
        writer = PdfWriter()
        try:
            reader = PdfReader(path)

        except FileNotFoundError:
            print(f"File {path} does not exist")

        except PdfReadError:
            print(f"File {path} is not valid PDF")

        for slice in slices:
            writer.append(fileobj=reader, pages=slice)

        with open(out, "wb") as file:
            writer.write(file)
