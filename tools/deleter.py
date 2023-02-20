from typing import List
import os
import sys
sys.path.append('../functions')

from pypdf.errors import PdfReadError
from pypdf import PdfReader, PdfWriter

from functions.slicetools import create_pageranges, invert_slices
from tools.toolABC import Tool


class Deleter(Tool):
    def __init__(self, path: str, slices: str) -> None:
        self.execute(path, slices)

    def execute(self, path: str, slices: str):
        """
        It takes a PDF file and a string of page ranges, and returns a new PDF file with the pages in
        the ranges removed
        
        :param path: Path to the PDF file
        :type path: str
        :param slices: The pages to delete, a string of page ranges, e.g. "1-3,5,7-9"
        :type slices: str
        """
        DESKTOP = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        filename = os.path.basename(path).split(".")[0]
        out = os.path.join(DESKTOP, f"{filename}-deleted.pdf")

        writer = PdfWriter()

        try:
            reader = PdfReader(path)

        except FileNotFoundError:
            print(f"File {path} does not exist")

        except PdfReadError:
            print(f"File {path} is not valid PDF")

        slices = create_pageranges(invert_slices(slices, len(reader.pages)))

        for slice in slices:
            writer.append(fileobj=reader, pages=slice)

        with open(out, "wb") as file:
            writer.write(file)
