import os
import shutil
import sys

from ...wordcount import (
    count_words,
    parse_args,
    preprocess_lines,
    split_lines_into_words,
    write_word_counts,
)
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


def test_preprocess_lines():
    lines = ["Hello, World!", "This is a TESTLINE."]
    prepoccessed_lines = preprocess_lines(lines)
    assert prepoccessed_lines == ["hello, world!", "this is a testline"]


def test_split_into_words():
    lines = ["hello world", "this is a testline"]
    words = split_lines_into_words(lines)
    assert words == [
        "hello",
        "world",
        "this",
        "is",
        "a",
        "testline",
    ]


def test_count_words():
    words = [
        "hello",
        "world",
        "this",
        "is",
        "a",
        "testline",
        "hello",
        "world",
    ]
    word_count = count_words(words)
    assert word_count == {
        "hello": 2,
        "world": 2,
        "this": 1,
        "is": 1,
        "a": 1,
        "testline": 1,
    }


def test_write_word_counts():
    output_folder = "data/output/"
    word_count = {"hello": 2, "world": 2, "this": 1}

    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    write_word_counts(output_folder, word_count)

    output_file = os.path.join(output_folder, "wordcount.tsv")

    assert os.path.exists(output_file), "Output file was not created."

    with open(output_file, "r") as f:
        lines = f.readlines()
    assert lines == ["hello\t2\n", "world\t2\n", "this\t1\n"]

    assert os.path.exists(output_file), "Output file was not created."

    with open(output_file, "r") as f:
        lines = f.readlines()
    assert lines == ["hello\t2\n", "world\t2\n", "this\t1\n"]
