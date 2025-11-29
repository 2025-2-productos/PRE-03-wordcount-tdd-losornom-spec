# Ejemplo para casos de uso
# python3 -m homework data/input data/output

import argparse

from homework.src._internals.read_all_files import read_all_files


def parse_args():
    parser = argparse.ArgumentParser(description="Count Word in files.")
    parser.add_argument(
        "input", type=str, help="Path to the input folder containing files to process."
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder containing files to process.",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def preprocess_lines(lines):
    preprocessed = [line.lower() for line in lines]
    return preprocessed


def split_lines_into_words(lines):
    pass


def count_words(words):
    pass


def write_word_counts(output_folder, word_count):
    pass


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_files(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    words = split_lines_into_words(preprocessed_lines)
    word_count = count_words(words)
    write_word_counts(output_folder, word_count)
