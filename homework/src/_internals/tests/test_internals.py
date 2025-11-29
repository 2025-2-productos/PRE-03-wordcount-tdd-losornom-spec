import sys

from ...wordcount import parse_args
from ..read_all_files import read_all_files


def test_parse_args():
    """Llamada en el prompt
    $ python3 -m homework data/input/ data/output/
    """

    test_args = ["homework", "data/input/", "data/output/"]
    sys.argv = test_args
    input_folder, output_folder = parse_args()

    assert input_folder == "data/input/"
    assert output_folder == "data/output/"


def test_read_all_lines():
    input_folder = "data/input/"
    lines = read_all_files(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data" in line
        for line in lines
    )
